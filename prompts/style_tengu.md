I have extracted prompts from my Claude Code conversation history. These prompts represent the types of requests I commonly make while coding. I want you to analyze these prompts and create a unique ASCII Tengu character that represents my prompting style and personality.

The extracted prompts are located in this directory as both json (extracted_prompts.json) and markdown (extracted_prompts.md). The information in both files is identical, just presented in different formats.

Please analyze the prompts data and create a unique ASCII Tengu character that represents the user's prompting style and personality.

First, calculate these stats (1-10 scale) based on the prompts:

**VERBOSITY**: How detailed/lengthy are the prompts?
- Short prompts (140-180 chars) = Low verbosity
- Medium prompts (180-220 chars) = Medium verbosity
- Long prompts (220-280 chars) = High verbosity

**TECHNICAL**: How technical/code-focused are the prompts?
- Look for: file paths, code terms, git commands, technical jargon

**CREATIVITY**: How creative/unconventional are the requests?
- Look for: unique requests, fun elements, personality in prompts

**PERSISTENCE**: How often do they iterate/follow up?
- Look for: duplicate prompts, follow-up patterns, "now", "also", "update"

**CLARITY**: How clear and well-structured are the prompts?
- Look for: numbered lists, clear instructions, specific details

**COLLABORATION**: How collaborative is their style?
- Look for: "let's", "we", "please", "can you", politeness markers

Based on these stats, create an ASCII Tengu with:
1. A creative name combining their prompting traits
2. Type(s) that match their style (e.g., Technical/Creative, Persistent/Clear)
3. ASCII art (15-20 lines) that reflects their personality
4. Stats display with visual bars
5. Special moves based on their most common prompt patterns
6. Evolution suggestion based on potential growth areas

Format the output for easy sharing in Slack:

```
╔════════════════════════════════════════╗
║          TENGU DISCOVERED!             ║
╚════════════════════════════════════════╝

[ASCII ART HERE]

Name: [Creative Tengu Name]
Type: [Type1]/[Type2]

STATS:
Verbosity    [████████░░] 8/10
Technical    [██████░░░░] 6/10
Creativity   [███████░░░] 7/10
Persistence  [█████████░] 9/10
Clarity      [████████░░] 8/10
Collaboration[██████████] 10/10

SIGNATURE MOVES:
• [Move 1]: Based on most common prompt pattern
• [Move 2]: Based on unique trait
• [Move 3]: Based on collaboration style
• [Move 4]: Ultimate move

TRAINER NOTES:
[2-3 observations about their prompting style]

EVOLUTION PATH:
[Current Form] → [Suggested Evolution]
"To evolve: [specific improvement suggestion]"
```

## Example Output

```
╔════════════════════════════════════════╗
║          TENGU DISCOVERED!             ║
╚════════════════════════════════════════╝

      ╭─────╮
      │ ◉ ◉ │
      │  ▽  │
   ╭──┴─────┴──╮
  │ COMMIT PLZ │
  │ ┌─┐   ┌─┐  │
  │ │G│   │I│  │
  │ │I│   │T│  │
  │ └─┘   └─┘  │
  ╰─┬───────┬──╯
    │  ╱ ╲  │
    ╰─╯   ╰─╯

Name: Commitzard
Type: Technical/Persistent

STATS:
Verbosity    [██████░░░░] 6/10
Technical    [█████████░] 9/10
Creativity   [████░░░░░░] 4/10
Persistence  [██████████] 10/10
Clarity      [████████░░] 8/10
Collaboration[███████░░░] 7/10

SIGNATURE MOVES:
• Git Commit Spam: Uses same commit message 13 times
• Issue Reference: Always includes "intercom/intercom#"
• Branch Mastery: Works across multiple directories
• Ultimate: Well-Written Commit Message

TRAINER NOTES:
• Loves committing but hates pushing
• Has memorized issue #410146
• Values well-structured commit messages

EVOLUTION PATH:
Commitzard → Deployking
"To evolve: Start pushing those commits!"
```