# Prompt Frequency ASCII Chart Generator

This prompt creates an ASCII visualization showing the most frequent prompt types and patterns from your Claude Code usage history.

## Instructions

Use this prompt with the extracted prompts JSON data from claude-code-prompt-plunderer. The LLM will analyze your prompts and create ASCII charts showing frequency patterns.

## Prompt

```
Analyze the following extracted Claude Code prompts data and create ASCII charts showing the most frequent prompt types and patterns.

Create the following visualizations:

1. **TOP PROMPT CATEGORIES** (Horizontal Bar Chart)
   Categorize prompts into types and show frequency:
   - Git Operations (commit, push, branch, etc.)
   - File Operations (read, write, search, etc.)
   - Code Review/Analysis
   - Documentation
   - Testing/Debugging
   - Project Setup
   - Other

2. **PROMPT LENGTH DISTRIBUTION** (Histogram)
   Show distribution of prompt lengths in character ranges

3. **TIME-BASED ACTIVITY** (If timestamps available)
   Show activity patterns by hour/day

4. **MOST REPEATED PROMPTS** (Top 5)
   Show exact prompts that were used multiple times

5. **KEYWORD CLOUD** (ASCII Style)
   Visualize most common words/phrases

Format as shareable ASCII art:

```
═══════════════════════════════════════════════════════════
     CLAUDE CODE PROMPT ANALYSIS - FREQUENCY CHARTS
═══════════════════════════════════════════════════════════

📊 TOP PROMPT CATEGORIES
────────────────────────────────────────────────────────────
Git Operations    ████████████████████████░░░░░░ 42% (35)
File Operations   ███████████████░░░░░░░░░░░░░░░ 25% (21)
Code Review       ████████░░░░░░░░░░░░░░░░░░░░░░ 13% (11)
Documentation     ██████░░░░░░░░░░░░░░░░░░░░░░░░ 10% (8)
Testing           ████░░░░░░░░░░░░░░░░░░░░░░░░░░  7% (6)
Project Setup     ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░  3% (3)

📏 PROMPT LENGTH DISTRIBUTION
────────────────────────────────────────────────────────────
140-160 chars  ████████░░░░░░░░ 16 prompts
160-180 chars  ████████████░░░░ 24 prompts
180-200 chars  ██████░░░░░░░░░░ 12 prompts
200-220 chars  ████████████████ 32 prompts
220-240 chars  ██████████░░░░░░ 20 prompts
240-260 chars  ████████░░░░░░░░ 16 prompts
260-280 chars  ████░░░░░░░░░░░░  8 prompts

🔁 MOST REPEATED PROMPTS (Top 5)
────────────────────────────────────────────────────────────
[13x] "Commit your changes but don't push them..."
[2x]  "Now give me a new prompt that I can give..."
[1x]  (All other prompts used only once)

🏷️ KEYWORD CLOUD
────────────────────────────────────────────────────────────
         commit     git       changes
    file      CODE       prompt    
         create          search
   update    READ     document   push
      test        branch    
   please     new      analyze

📈 INSIGHTS
────────────────────────────────────────────────────────────
• Total Prompts: 84 (71 unique)
• Average Length: 196 characters
• Most Active Directory: /Users/levindixon/src/embercom-*
• Favorite Issue: intercom/intercom#410146
• Politeness Score: High (frequent "please", "let's")
```

Analyze the data and provide specific numbers and percentages based on the actual prompt patterns found.

Here's the prompts data to analyze:
[INSERT JSON DATA]
```

## Example Categories to Look For

When categorizing prompts, consider these patterns:

**Git Operations:**
- Keywords: commit, push, git, branch, merge, stage, diff, log
- Patterns: issue references, commit messages

**File Operations:**
- Keywords: read, write, create, search, find, grep, update, edit
- Patterns: file paths, extensions

**Code Review/Analysis:**
- Keywords: review, analyze, check, validate, evaluate
- Patterns: asking for feedback, code quality

**Documentation:**
- Keywords: document, README, markdown, docs, explain
- Patterns: .md files, documentation requests

**Testing/Debugging:**
- Keywords: test, debug, error, fix, run, execute
- Patterns: error messages, test commands

**Project Setup:**
- Keywords: create, initialize, setup, configure, install
- Patterns: new projects, configuration

## Tips for Best Results

1. Provide the complete JSON data including counts and timestamps
2. The chart will be more accurate with more prompt data
3. Look for subtle patterns in language use and repetition
4. ASCII bars should be proportional to actual percentages