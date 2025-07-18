#!/usr/bin/env python3
import json
import os
import argparse
from pathlib import Path
from typing import List, Dict
from datetime import datetime

def extract_user_prompts(base_dir: str, max_length: int = 280, min_length: int = 140) -> List[Dict]:
    """
    Extract all user prompts from Claude Code JSONL files that are >= min_length and <= max_length characters.
    
    Args:
        base_dir: Base directory containing conversation folders
        max_length: Maximum character length for prompts to include
        min_length: Minimum character length for prompts to include
        
    Returns:
        List of prompt dictionaries with metadata
    """
    prompts = []
    
    # Walk through all directories
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.jsonl'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.strip():
                                try:
                                    data = json.loads(line)
                                    
                                    # Check if this is a user message
                                    if (data.get('type') == 'user' and 
                                        'message' in data and 
                                        isinstance(data['message'], dict) and
                                        data['message'].get('role') == 'user'):
                                        
                                        content = data['message'].get('content', '')
                                        
                                        # Handle both string and list content
                                        if isinstance(content, list):
                                            # Extract text from content list
                                            text_parts = []
                                            for item in content:
                                                if isinstance(item, dict) and item.get('type') == 'text':
                                                    text_parts.append(item.get('text', ''))
                                            content = ' '.join(text_parts)
                                        
                                        # Skip meta messages and command messages
                                        if (data.get('isMeta') or 
                                            '<command-name>' in content or
                                            '<local-command-stdout>' in content or
                                            'Caveat: The messages below were generated' in content):
                                            continue
                                        
                                        # Check length and add to prompts
                                        if content and min_length <= len(content) <= max_length:
                                            prompts.append({
                                                'prompt': content,
                                                'length': len(content),
                                                'timestamp': data.get('timestamp', ''),
                                                'session_id': data.get('sessionId', ''),
                                                'cwd': data.get('cwd', ''),
                                                'file': file_path
                                            })
                                            
                                except json.JSONDecodeError:
                                    print(f"Error parsing JSON line in {file_path}")
                                    continue
                                    
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
                    continue
    
    return prompts

def save_prompts_for_analysis(prompts: List[Dict], output_file: str, max_length: int = 280, min_length: int = 140) -> Dict:
    """
    Save prompts in a format suitable for LLM analysis, deduplicating while maintaining count.
    
    Returns:
        The analysis_data dictionary containing metadata and deduplicated prompts
    """
    # Sort by timestamp
    prompts.sort(key=lambda x: x['timestamp'])
    
    # Deduplicate prompts while maintaining count and metadata
    prompt_map = {}
    for prompt in prompts:
        text = prompt['prompt']
        if text not in prompt_map:
            prompt_map[text] = {
                'text': text,
                'count': 1,
                'length': prompt['length'],
                'first_timestamp': prompt['timestamp'],
                'last_timestamp': prompt['timestamp'],
                'working_directories': [prompt['cwd']],
                'all_timestamps': [prompt['timestamp']]
            }
        else:
            prompt_map[text]['count'] += 1
            prompt_map[text]['last_timestamp'] = prompt['timestamp']
            prompt_map[text]['all_timestamps'].append(prompt['timestamp'])
            if prompt['cwd'] not in prompt_map[text]['working_directories']:
                prompt_map[text]['working_directories'].append(prompt['cwd'])
    
    # Convert to list and sort by count (descending) then by first timestamp
    deduplicated_prompts = list(prompt_map.values())
    deduplicated_prompts.sort(key=lambda x: (-x['count'], x['first_timestamp']))
    
    # Create analysis-friendly format
    analysis_data = {
        'metadata': {
            'total_prompts': len(prompts),
            'unique_prompts': len(deduplicated_prompts),
            'extraction_date': datetime.now().isoformat(),
            'max_length_filter': max_length,
            'min_length_filter': min_length
        },
        'prompts': []
    }
    
    # Add deduplicated prompts with count and metadata
    for i, prompt in enumerate(deduplicated_prompts):
        analysis_data['prompts'].append({
            'id': i + 1,
            'text': prompt['text'],
            'count': prompt['count'],
            'length': prompt['length'],
            'first_timestamp': prompt['first_timestamp'],
            'last_timestamp': prompt['last_timestamp'],
            'working_directories': prompt['working_directories']
        })
    
    # Save as JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_data, f, indent=2, ensure_ascii=False)
    
    # Also save as markdown for easy reading
    markdown_output = output_file.replace('.json', '.md')
    with open(markdown_output, 'w', encoding='utf-8') as f:
        f.write("# Claude Code Prompts Analysis (Deduplicated)\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Total prompts:** {len(prompts)}\n")
        f.write(f"- **Unique prompts:** {len(deduplicated_prompts)}\n")
        f.write(f"- **Duplication rate:** {(1 - len(deduplicated_prompts) / len(prompts)) * 100:.1f}%\n")
        f.write(f"- **Extraction date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Length filters:** {min_length} - {max_length} characters\n\n")
        
        # Add length distribution statistics
        lengths = [p['length'] for p in deduplicated_prompts]
        if lengths:
            f.write("## Length Distribution\n\n")
            f.write(f"- **Shortest prompt:** {min(lengths)} characters\n")
            f.write(f"- **Longest prompt:** {max(lengths)} characters\n")
            f.write(f"- **Average length:** {sum(lengths) // len(lengths)} characters\n\n")
        
        # Add most frequent prompts table
        f.write("## Most Frequent Prompts\n\n")
        top_prompts = sorted(deduplicated_prompts, key=lambda x: x['count'], reverse=True)[:10]
        if top_prompts:
            f.write("| Count | Length | Prompt (truncated to 60 chars) |\n")
            f.write("|-------|--------|--------------------------------|\n")
            for prompt in top_prompts:
                truncated = prompt['text'][:60] + "..." if len(prompt['text']) > 60 else prompt['text']
                truncated = truncated.replace('\n', ' ').replace('|', '\\|')
                f.write(f"| {prompt['count']} | {prompt['length']} | {truncated} |\n")
            f.write("\n")
        
        f.write("## All Prompts\n\n")
        
        for i, prompt in enumerate(deduplicated_prompts):
            f.write(f"### Prompt #{i+1}\n\n")
            f.write(f"**Metadata:**\n")
            f.write(f"- Length: {prompt['length']} characters\n")
            f.write(f"- Times used: {prompt['count']}\n")
            f.write(f"- First seen: `{prompt['first_timestamp']}`\n")
            if prompt['count'] > 1:
                f.write(f"- Last seen: `{prompt['last_timestamp']}`\n")
            f.write(f"- Working directories: `{', '.join(prompt['working_directories'])}`\n\n")
            f.write("**Prompt:**\n\n")
            f.write("```\n")
            f.write(prompt['text'])
            f.write("\n```\n\n")
            f.write("---\n\n")
    
    return analysis_data

def main():
    parser = argparse.ArgumentParser(description='Extract user prompts from Claude Code conversations')
    parser.add_argument('--max-length', type=int, default=280, 
                       help='Maximum character length for prompts to include (default: 280)')
    parser.add_argument('--min-length', type=int, default=140,
                       help='Minimum character length for prompts to include (default: 140)')
    parser.add_argument('--base-dir', default='~/.claude/projects',
                       help='Base directory containing conversation folders (default: ~/.claude/projects)')
    parser.add_argument('--output', default='./extracted_prompts.json',
                       help='Output JSON file path (default: ./extracted_prompts.json)')
    
    args = parser.parse_args()
    
    # Expand user home directory and convert to absolute path
    args.base_dir = os.path.abspath(os.path.expanduser(args.base_dir))
    args.output = os.path.abspath(os.path.expanduser(args.output))
    
    # Check if base directory exists
    if not os.path.exists(args.base_dir):
        print(f"Error: Base directory '{args.base_dir}' does not exist.")
        print("Please specify a valid directory using --base-dir")
        return
    
    print(f"Extracting prompts from Claude Code conversations in {args.base_dir}...")
    prompts = extract_user_prompts(args.base_dir, args.max_length, args.min_length)
    
    print(f"Found {len(prompts)} prompts between {args.min_length} and {args.max_length} characters")
    
    if prompts:
        analysis_data = save_prompts_for_analysis(prompts, args.output, args.max_length, args.min_length)
        print(f"Saved prompts to {args.output}")
        print(f"Also saved readable version to {args.output.replace('.json', '.md')}")
        
        # Print some statistics
        lengths = [p['length'] for p in prompts]
        print(f"\nStatistics:")
        print(f"  Total prompts: {len(prompts)}")
        print(f"  Unique prompts: {analysis_data['metadata']['unique_prompts']}")
        print(f"  Duplication rate: {(1 - analysis_data['metadata']['unique_prompts'] / len(prompts)) * 100:.1f}%")
        print(f"  Shortest prompt: {min(lengths)} chars")
        print(f"  Longest prompt: {max(lengths)} chars")
        print(f"  Average length: {sum(lengths) // len(lengths)} chars")
    else:
        print("No prompts found!")

if __name__ == "__main__":
    main()