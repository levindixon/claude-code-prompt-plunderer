# Slash Command Discovery Prompt

Use this prompt with an LLM to analyze your extracted Claude Code prompts and discover opportunities for custom slash commands.

## Prompt Template

```
I have extracted [X] prompts from my Claude Code conversation history. These prompts represent the types of requests I commonly make while coding. I want you to analyze these prompts to:

1. Identify recurring patterns, themes, or types of requests
2. Group similar prompts together
3. Suggest custom Claude Code slash commands that would save me time

For each suggested slash command:
- Provide a command name (e.g., /refactor-component)
- Write a clear, comprehensive prompt template that Claude Code would use
- Include placeholders for variable parts using {{variable_name}} syntax
- Explain what pattern you identified that led to this suggestion

Here are my extracted prompts:

[PASTE YOUR EXTRACTED PROMPTS JSON OR MARKDOWN HERE]

Please analyze these and suggest 5-10 custom slash commands that would be most valuable based on my usage patterns. Focus on commands that would:
- Save me from typing similar requests repeatedly
- Standardize my common workflows
- Ensure I don't forget important steps in recurring tasks
```

## How to Use This Prompt

1. Run the prompt plunderer to extract your Claude Code prompts:
   ```bash
   python3 plunder_prompts.py
   ```

2. Copy the contents of either:
   - `extracted_prompts.json` (for structured data)
   - `extracted_prompts_analysis.md` (for readable format)

3. Paste the prompt template above into your preferred LLM (Claude, ChatGPT, etc.)

4. Replace `[PASTE YOUR EXTRACTED PROMPTS JSON OR MARKDOWN HERE]` with your extracted prompts

5. Review the suggested slash commands and create the ones you find useful

## Example Slash Command Format

Based on the analysis, the LLM might suggest commands like:

### /test-and-fix
```markdown
Run all tests for the current project and automatically fix any failing tests. Follow these steps:

1. Identify the test command from package.json or project configuration
2. Run the full test suite
3. For each failing test:
   - Read the test file and understand what it's testing
   - Examine the error message and stack trace
   - Fix the underlying issue (not just the test)
   - Re-run that specific test to confirm the fix
4. Run the full test suite again to ensure no regressions
5. Provide a summary of what was fixed

Focus on fixing the actual bugs, not just making tests pass artificially.
```

### /add-feature
```markdown
Implement a new feature: {{feature_description}}

1. First understand the existing codebase structure
2. Create a TodoWrite list for the implementation steps
3. Follow existing patterns and conventions in the codebase
4. Add appropriate error handling and validation
5. Create or update tests for the new functionality
6. Update any relevant documentation
7. Run linting and type checking

Component/Module name: {{component_name}}
Location: {{file_location}}
```

## Tips for Better Results

- Include as many prompts as possible for better pattern recognition
- If you have specific workflows you want to optimize, mention them in your request
- Consider creating multiple specialized prompts for different aspects of your work (frontend, backend, testing, etc.)
- Iterate on the suggested commands based on your actual usage