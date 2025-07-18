I have extracted prompts from my Claude Code conversation history. These prompts represent the types of requests I commonly make while coding. I want you to analyze these prompts to:

1. Identify recurring patterns, themes, or types of requests
2. Group similar prompts together
3. Suggest custom Claude Code slash commands (documentation provided below) that would save me time
4. Save each of the suggested custom Claude Code slash commands in a new directory named custom-command-suggestions ready to be placed into the user's ~/.claude/commands directory.

For each suggested slash command:
- Provide a command name (e.g., /refactor-component)
- Write a clear, comprehensive prompt template that Claude Code would use
- Include placeholders for variable parts using {{variable_name}} syntax
- Explain what pattern you identified that led to this suggestion

The extracted prompts are located in this directory as both json (extracted_prompts.json) and markdown (extracted_prompts.md). The information in both files is identical, just presented in different formats.

Please analyze these and suggest 5-10 custom slash commands that would be most valuable based on my usage patterns. Focus on commands that would:
- Save me from typing similar requests repeatedly
- Standardize my common workflows
- Ensure I don't forget important steps in recurring tasks

````markdown
# Claude Code Slash Commands Guide

## Overview

Claude Code supports custom slash commands - reusable prompts stored as Markdown files that can be executed with arguments. Commands start with `/` and can be project-specific or user-level.

## Command Structure

### File Locations
- **Project commands**: `.claude/commands/` (shared with team, marked as "(project)")
- **User commands**: `~/.claude/commands/` (personal, marked as "(user)")

### File Format
Commands are Markdown files (`.md` extension) with:
- **Filename**: Becomes the command name (e.g., `optimize.md` → `/optimize`)
- **YAML frontmatter**: Metadata configuration
- **Main content**: The prompt instructions

### Basic Template
```markdown
---
description: Brief description shown in /help
allowed-tools: [Bash, Read, Write, Edit]  # Required for tool usage
argument-hint: <optional-hint>  # Shows during auto-complete
---

Your prompt instructions here...
```

## Key Features

### 1. Arguments
Use `$ARGUMENTS` placeholder to accept dynamic input:
```markdown
---
description: Generate a React component
allowed-tools: [Write]
argument-hint: <component-name>
---

Create a React component named $ARGUMENTS with proper TypeScript types.
```

### 2. Bash Command Execution
Prefix with `!` to run bash commands before the prompt:
```markdown
---
description: Analyze current git status
allowed-tools: [Bash]
---

!git status
!git diff --stat

Based on the git status above, suggest the next steps.
```

### 3. File References
Use `@` to include file contents:
```markdown
---
description: Review code structure
allowed-tools: [Read]
---

Review the following files:
@src/main.ts
@src/config.json

Provide recommendations for improvements.
```

### 4. Namespacing
Organize commands in subdirectories:
- `.claude/commands/frontend/component.md` → `/frontend:component`
- `.claude/commands/backend/api.md` → `/backend:api`

## Example Commands

### Simple Command
```markdown
---
description: Format and lint code
allowed-tools: [Bash]
---

!npm run lint
!npm run format

Fix any linting errors found above.
```

### Command with Arguments
```markdown
---
description: Create a new feature module
allowed-tools: [Write, Edit]
argument-hint: <module-name>
---

Create a new feature module named "$ARGUMENTS" with:
- Module file at src/modules/$ARGUMENTS/index.ts
- Test file at src/modules/$ARGUMENTS/test.ts
- Follow existing module patterns in the codebase
```

### Complex Command with Multiple Features
```markdown
---
description: Security audit for a file
allowed-tools: [Read, Bash]
argument-hint: <file-path>
---

!file $ARGUMENTS

@$ARGUMENTS

Perform a security audit on the file above, checking for:
- Hardcoded credentials
- SQL injection vulnerabilities
- XSS vulnerabilities
- Insecure dependencies
- Other security best practices
```

## Best Practices

1. **Always specify `allowed-tools`** when using tools
2. **Use clear `description`** for discoverability in `/help`
3. **Add `argument-hint`** when expecting arguments
4. **Keep commands focused** on a single task
5. **Use namespacing** to organize related commands
6. **Test commands** before sharing with team

## Usage

- Execute: `/command-name [arguments]`
- List all commands: `/help`
- Commands auto-complete after typing `/`
````