# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains a Python utility for analyzing Claude Code conversation history stored in JSONL files. The tool extracts user prompts from conversation logs and provides analysis capabilities including deduplication and statistical summaries.

## Project Structure

- `plunder_prompts.py` - Main Python script that extracts and analyzes user prompts from Claude Code conversation JSONL files
- `prompts/` - Directory containing 5 creative prompt analysis templates
  - `slash_command_discovery.md` - Suggests custom Claude Code slash commands based on usage patterns
  - `style_tengu.md` - Creates ASCII Tengu character representing prompting personality
  - `frequency_chart.md` - Generates ASCII visualizations of prompt patterns
  - `evolution_timeline.md` - Shows prompting style evolution over time
  - `personality_report.md` - Produces personality analysis based on prompting patterns
  - `README.md` - Documentation for using the prompt templates
- `examples/` - Sample output files demonstrating the tool's capabilities
  - `sample_output.json` - Example JSON output from the extraction tool
  - `sample_output.md` - Example Markdown analysis output

## Commands

### Running the Script

```bash
# Basic usage (uses default settings)
python3 plunder_prompts.py

# Specify custom base directory for Claude conversations
python3 plunder_prompts.py --base-dir /path/to/claude/projects

# Filter prompts by length
python3 plunder_prompts.py --min-length 100 --max-length 500

# Specify custom output file
python3 plunder_prompts.py --output ./my_prompts.json
```

### Using Prompt Analysis Templates

After extracting prompts, use the analysis templates with Claude Code:

```bash
# Discover potential slash commands from your usage patterns
claude "$(cat prompts/slash_command_discovery.md)"

# Generate ASCII Tengu character representing your style
claude "$(cat prompts/style_tengu.md)"

# Create frequency charts and visualizations
claude "$(cat prompts/frequency_chart.md)"

# View your prompting evolution timeline
claude "$(cat prompts/evolution_timeline.md)"

# Get personality analysis based on prompts
claude "$(cat prompts/personality_report.md)"
```

### Script Arguments

- `--base-dir`: Directory containing Claude Code conversation folders (default: `~/.claude/projects`)
- `--max-length`: Maximum character length for prompts to include (default: 280)
- `--min-length`: Minimum character length for prompts to include (default: 140)
- `--output`: Output JSON file path (default: `./extracted_prompts.json`)

## Code Architecture

The script processes Claude Code conversation history by:

1. Walking through all JSONL files in the specified base directory
2. Parsing each line as JSON and identifying user messages
3. Filtering out meta messages and command output
4. Applying length filters to extract prompts within specified character limits
5. Deduplicating prompts while maintaining usage count and metadata
6. Generating both JSON and Markdown output files with analysis

### Key Functions

- `extract_user_prompts()`: Extracts user prompts from JSONL files with length filtering
- `save_prompts_for_analysis()`: Deduplicates prompts and generates analysis output

## Output Format

The script generates two output files:
- JSON file with structured prompt data including metadata and deduplication statistics
- Markdown file with readable analysis including summary statistics and all prompts

## Dependencies

No external dependencies required - uses only Python 3.6+ standard library.

## Recent Updates

- Added creative prompt analysis templates for personality analysis, visualization, and slash command discovery
- Enhanced with example output files demonstrating tool capabilities
- Refactored templates for direct Claude Code CLI usage