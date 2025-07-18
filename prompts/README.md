# Claude Code Prompt Analysis Templates

This directory contains ready-to-use prompt templates for analyzing your extracted Claude Code conversation data. Each template transforms your prompt history into insightful and often entertaining visualizations.

## Quick Start

1. First, extract your prompts from the parent directory:
   ```bash
   cd ..
   python3 plunder_prompts.py
   ```

2. Then use any template with Claude Code:
   ```bash
   claude "$(cat prompt_style_tengu.md)"
   ```

## Available Templates

### 🎯 [slash_command_discovery.md](slash_command_discovery.md)
Analyzes your prompts to suggest custom Claude Code slash commands. Identifies repetitive patterns and generates ready-to-use command templates tailored to your workflow.

### 🦸 [prompt_style_tengu.md](prompt_style_tengu.md)
Creates a unique ASCII [Tengu](https://github.com/levindixon/tengu_spinner_words?tab=readme-ov-file#the-tengu-discovery) character representing your prompting personality. Includes stats, special moves, and evolution paths. Perfect for sharing in Slack!

### 📊 [prompt_frequency_chart.md](prompt_frequency_chart.md)
Generates ASCII visualizations of your prompt patterns including:
- Category breakdowns (Git, Files, Code Review, etc.)
- Length distributions
- Most repeated prompts
- Keyword clouds

### 📈 [prompt_evolution_timeline.md](prompt_evolution_timeline.md)
Shows how your prompting style has evolved over time with an ASCII timeline. Tracks skill progression, project transitions, and identifies key growth moments in your Claude Code journey.

### 🎭 [prompt_personality_report.md](prompt_personality_report.md)
Produces a comprehensive personality analysis based on your prompting patterns. Reveals hidden traits, communication style, and predicts your future evolution as a prompt engineer.

## Usage Tips

- All templates expect the `extracted_prompts.json` file to exist in the parent directory
- The more prompts you have, the more accurate and entertaining the analysis
- Results are formatted for easy sharing in Slack or other chat platforms
- Each template can be customized by editing the prompt instructions

## Creating Your Own Templates

Feel free to create new analysis templates! Each template should:
1. Accept the extracted prompts JSON data
2. Provide clear analysis instructions
3. Generate formatted output (ASCII art encouraged!)
4. Include examples of expected output

See the existing templates for patterns and inspiration.