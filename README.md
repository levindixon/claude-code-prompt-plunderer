# Claude Code Prompt Plunderer

A Python utility that extracts and analyzes user prompts from Claude Code conversation history. This tool helps you understand your Claude Code usage patterns by collecting prompts from the locally stored conversation logs and presenting them in both JSON and Markdown formats.

## Features

- 🔍 **Prompt Extraction**: Automatically discovers and extracts user prompts from Claude Code JSONL conversation files
- 📊 **Smart Filtering**: Filter prompts by character length to focus on meaningful interactions
- 🔄 **Deduplication**: Identifies repeated prompts and tracks usage frequency
- 📈 **Statistical Analysis**: Provides insights into prompt length distribution and usage patterns
- 📝 **Multiple Output Formats**: Generates both JSON (for programmatic use) and Markdown (for human reading)
- 🏷️ **Rich Metadata**: Preserves timestamps, working directories, and session information

## Use Cases

- **Command Automation**: Analyze your most frequent prompts to create custom Claude Code commands
- **Usage Analysis**: Understand your interaction patterns with Claude Code
- **Prompt Library**: Build a personal library of effective prompts
- **Workflow Optimization**: Identify repetitive tasks that could be automated
- **Learning Tool**: Review past interactions to improve prompt engineering skills

## Installation

No installation required! This is a standalone Python script that uses only Python standard library modules.

### Requirements

- Python 3.6 or higher
- Access to Claude Code conversation files (typically in `~/.claude/projects`)

## Usage

### Basic Usage

```bash
python3 plunder_prompts.py
```

This will:
- Look for conversation files in the default location (`~/.claude/projects`)
- Extract prompts between 140-280 characters (optimal for identifying meaningful commands)
- Save results to `extracted_prompts.json` and `extracted_prompts.md`

### Advanced Options

```bash
# Specify a custom conversation directory
python3 plunder_prompts.py --base-dir /path/to/claude/projects

# Adjust length filters for different use cases
python3 plunder_prompts.py --min-length 50 --max-length 500

# Save output to a specific location
python3 plunder_prompts.py --output ./analysis/my_prompts.json

# Combine options
python3 plunder_prompts.py --base-dir ~/backups/claude --min-length 100 --max-length 1000 --output ./prompts_analysis.json
```

### Command Line Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--base-dir` | `~/.claude/projects` | Directory containing Claude Code conversation folders |
| `--min-length` | `140` | Minimum character length for prompts to include |
| `--max-length` | `280` | Maximum character length for prompts to include |
| `--output` | `./extracted_prompts.json` | Output file path (Markdown file will use same name with .md extension) |

## Output Format

### JSON Output

The JSON file contains structured data perfect for programmatic analysis:

```json
{
  "metadata": {
    "total_prompts": 150,
    "unique_prompts": 87,
    "extraction_date": "2024-01-15T10:30:00",
    "min_length_filter": 140,
    "max_length_filter": 280
  },
  "prompts": [
    {
      "id": 1,
      "text": "Create a Python function that validates email addresses",
      "count": 3,
      "length": 52,
      "first_timestamp": "2024-01-10T09:15:00",
      "last_timestamp": "2024-01-14T16:22:00",
      "working_directories": ["/home/user/project1", "/home/user/project2"]
    }
  ]
}
```

### Markdown Output

The Markdown file provides a human-readable analysis including:
- Summary statistics
- Length distribution analysis
- Top 10 most frequent prompts
- Complete list of all unique prompts with metadata

## Example Workflow

1. **Extract your prompts**:
   ```bash
   python3 plunder_prompts.py --min-length 50 --max-length 300
   ```

2. **Review the Markdown output** to understand your usage patterns:
   ```bash
   open extracted_prompts.md  # macOS
   # or
   xdg-open extracted_prompts.md  # Linux
   ```

3. **Use the JSON output** for further analysis:
   ```python
   import json

   with open('extracted_prompts.json', 'r') as f:
       data = json.load(f)

   # Find your most complex prompts
   complex_prompts = [p for p in data['prompts'] if p['length'] > 200]

   # Find prompts used in specific projects
   project_prompts = [p for p in data['prompts']
                      if '/myproject' in str(p['working_directories'])]
   ```

## Privacy and Security

- This tool only reads files from your local machine
- No data is sent to external services
- All processing happens locally on your computer
- The tool respects file permissions and will skip files it cannot read

## Example Prompts & Analysis Tools

The `prompts/` directory contains ready-to-use prompt templates that analyze your extracted data in creative and insightful ways. Use them with Claude Code like this:

```bash
# First extract your prompts
python3 plunder_prompts.py

# Then use any analysis prompt
claude "$(cat ./prompts/style_tengu.md)"
```

### Available Analysis Prompts

#### 🎯 [Slash Command Discovery](prompts/slash_command_discovery.md)
Analyzes your prompts to suggest custom Claude Code slash commands tailored to your workflow. Identifies repetitive patterns and generates ready-to-use command templates.

#### 🦸 [Prompt Style Tengu](prompts/style_tengu.md)
Creates a unique ASCII [Tengu](https://github.com/levindixon/tengu_spinner_words?tab=readme-ov-file#the-tengu-discovery) character representing your prompting personality. Includes stats, special moves, and evolution paths. Perfect for sharing in Slack!

#### 📊 [Prompt Frequency Chart](prompts/frequency_chart.md)
Generates ASCII visualizations of your prompt patterns including category breakdowns, length distributions, and keyword clouds. Great for understanding your Claude Code usage at a glance.

#### 📈 [Prompt Evolution Timeline](prompts/evolution_timeline.md)
Shows how your prompting style has evolved over time with an ASCII timeline. Tracks skill progression, project transitions, and identifies key growth moments.

#### 🎭 [Prompt Personality Report](prompts/personality_report.md)
Produces a comprehensive personality analysis based on your prompting patterns. Reveals hidden traits, communication style, and predicts your future evolution as a prompt engineer.

## Future Ideas

While not implemented yet, here are some interesting extensions you could build:

- **Prompt Categorization**: Use LLMs to categorize prompts by intent (debugging, refactoring, documentation, etc.)
- **Command Generation**: Automatically generate Claude Code custom commands for frequent tasks
- **Time Analysis**: Analyze prompt patterns over time to understand productivity trends
- **Project-specific Analysis**: Group prompts by project to understand different coding contexts
- **Prompt Templates**: Extract and generalize prompts into reusable templates

## Contributing

Feel free to fork this repository and adapt the tool to your needs! Some ideas for contributions:

- Add support for additional filtering options
- Implement prompt categorization
- Create visualization tools for the extracted data
- Add export formats (CSV, SQLite, etc.)

## License

MIT License - See LICENSE file for details

## Acknowledgments

Created for the Claude Code community to help users better understand and optimize their AI-assisted coding workflows.