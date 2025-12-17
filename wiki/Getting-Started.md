# Getting Started with Rulebook-AI

This guide will help you get started with Rulebook-AI, from installation to your first synced environment.

## Table of Contents

- [What You'll Learn](#what-youll-learn)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Understanding the Basics](#understanding-the-basics)
- [Your First Pack](#your-first-pack)
- [Working with Memory Files](#working-with-memory-files)
- [Common Workflows](#common-workflows)
- [Next Steps](#next-steps)

## What You'll Learn

By the end of this guide, you'll understand:
- How to install and set up Rulebook-AI
- What packs are and how to use them
- How to sync your environment to AI assistants
- How the Memory Bank system works
- Basic workflows for planning, coding, and debugging

## Prerequisites

### Required
- **Python 3.9+**: Rulebook-AI requires Python 3.9 or higher
- **uv**: Package manager for Python (recommended installation method)

### Recommended
- **Git**: For version control and GitHub pack sources
- **AI Assistant**: One or more supported AI coding assistants (Cursor, Copilot, etc.)

### Supported AI Assistants

Rulebook-AI supports the following AI assistants:
- Cursor
- Windsurf
- Cline
- RooCode
- Kilo Code
- GitHub Copilot
- Gemini CLI
- Claude Code
- Codex CLI
- Warp

See [Supported Assistants](../memory/docs/user_guide/supported_assistants.md) for detailed compatibility information.

## Installation

### Option 1: Using uvx (Recommended)

The quickest way to get started is using `uvx`, which runs Rulebook-AI without installing it:

```bash
# Install uv if you don't have it
curl -fsSL https://astral.sh/uv/install.sh | bash

# Verify uv installation
uv --version

# Use Rulebook-AI via uvx (no installation needed)
uvx rulebook-ai --help
```

### Option 2: Install with uv

To install Rulebook-AI globally:

```bash
uv tool install rulebook-ai

# Verify installation
rulebook-ai --version
```

### Option 3: Install with pip

Traditional pip installation:

```bash
pip install rulebook-ai

# Verify installation
rulebook-ai --version
```

### Verify Installation

Test that Rulebook-AI is working:

```bash
# If using uvx
uvx rulebook-ai --help

# If installed
rulebook-ai --help
```

You should see the help message with available commands.

## Quick Start

Let's set up your first project with Rulebook-AI in 3 steps:

### Step 1: Add a Pack

Navigate to your project directory and add the `light-spec` pack:

```bash
cd /path/to/your/project

# Add the light-spec pack
uvx rulebook-ai packs add light-spec
```

**What this does**:
- Adds the `light-spec` pack to your project's pack library
- Does NOT yet modify your project files

### Step 2: Sync Your Environment

Sync the pack to your project:

```bash
uvx rulebook-ai project sync
```

**What this does**:
- Creates `.rulebook-ai/` directory (management state)
- Creates `memory/` directory with documentation templates
- Creates `tools/` directory with helper scripts
- Generates `.cursor/rules/` (default assistant)

### Step 3: Verify Setup

Check that everything was created:

```bash
ls -la

# You should see:
# .rulebook-ai/    (should be in .gitignore)
# .cursor/         (should be in .gitignore)
# memory/          (commit this to version control)
# tools/           (commit this to version control)
```

**That's it!** Your AI assistant now has structured rules and a memory system.

## Understanding the Basics

### The Three Pillars

Rulebook-AI environments consist of three components:

#### 1. Rules
**Location**: Generated in assistant-specific directories (`.cursor/rules/`, `GEMINI.md`, etc.)

**Purpose**: Instructions that guide AI behavior and workflows

**Categories**:
- Meta-rules: Focus determination
- Memory structure: Documentation system
- General principles: Best practices
- Workflows: Planning, coding, debugging

**Example**:
```markdown
# From .cursor/rules/06-rules_v1.md
## Core Principles
- Clarity First: Seek clarification on ambiguities
- Context is Key: Gather relevant context before work
- Structured Interaction: Provide clear responses
```

#### 2. Context (Memory Bank)
**Location**: `memory/` directory in your project

**Purpose**: Your project's persistent knowledge base

**Core Files**:
1. `memory/docs/product_requirement_docs.md` - What and why
2. `memory/docs/architecture.md` - How it works
3. `memory/docs/technical.md` - Tech stack and setup
4. `memory/tasks/tasks_plan.md` - Task backlog
5. `memory/tasks/active_context.md` - Current state
6. `memory/docs/error-documentation.md` - Known issues
7. `memory/docs/lessons-learned.md` - Learning journal

**These files ARE your environment** - keep them updated!

#### 3. Tools
**Location**: `tools/` directory in your project

**Purpose**: Helper scripts the AI can use

**Examples**:
- `tools/llm_api.py` - Call other LLMs
- `tools/web_scraper.py` - Scrape web content
- `tools/search_engine.py` - Search the web

### What Goes Where

```
your-project/
├── src/                    # Your code (you own this)
├── tests/                  # Your tests (you own this)
│
├── memory/                 # Project context (COMMIT THIS)
│   ├── docs/
│   └── tasks/
│
├── tools/                  # Helper scripts (COMMIT THIS)
│
├── .rulebook-ai/          # Pack state (IGNORE THIS)
├── .cursor/               # Generated rules (IGNORE THIS)
└── .gitignore             # Update to ignore generated files
```

### Version Control

**Commit These**:
- `memory/` - Your project's knowledge
- `tools/` - Helper scripts
- `.rulebook-ai/packs.yaml` - Pack configuration

**Ignore These** (add to `.gitignore`):
```gitignore
# Rulebook-AI generated files
.rulebook-ai/state/
.cursor/
.windsurf/
.clinerules/
.roo/
.kilocode/
GEMINI.md
CODEX_RULES.md
.claude/
.warp/
.github/copilot-instructions.md
```

## Your First Pack

### What is a Pack?

A **pack** is a pre-configured environment bundle containing:
- **Rules**: AI instructions
- **Memory starters**: Documentation templates
- **Tool starters**: Helper scripts

### Choosing Your First Pack

For most projects, start with **light-spec**:

```bash
uvx rulebook-ai packs add light-spec
```

**Why light-spec?**
- ✅ Best balance of guidance and flexibility
- ✅ Comprehensive but not overwhelming
- ✅ Works for most project types
- ✅ Easy to understand and customize

### Other Pack Options

```bash
# For more structure and validation
uvx rulebook-ai packs add medium-spec

# For maximum rigor (large projects)
uvx rulebook-ai packs add heavy-spec

# For tasks without context needs
uvx rulebook-ai packs add no_memory_interation_rules
```

See [Packs Overview](Packs-Overview.md) for detailed comparisons.

### Pack Management Commands

```bash
# List available packs
uvx rulebook-ai packs list

# Add a pack
uvx rulebook-ai packs add <pack-name>

# Remove a pack
uvx rulebook-ai packs remove <pack-name>

# Show pack details
uvx rulebook-ai packs info <pack-name>
```

## Working with Memory Files

The Memory Bank is the heart of Rulebook-AI. It gives your AI long-term memory.

### Initial Setup

After your first sync, you'll have template files in `memory/`:

```bash
memory/
├── docs/
│   ├── product_requirement_docs.md  # Empty template
│   ├── architecture.md               # Empty template
│   └── technical.md                  # Empty template
└── tasks/
    ├── tasks_plan.md                 # Empty template
    └── active_context.md             # Empty template
```

### Filling Out Memory Files

#### 1. Product Requirements (`product_requirement_docs.md`)

Start here! This defines your project:

```markdown
# Product Requirements

## Project Overview
Brief description of what you're building...

## Problem Statement
What problem does this solve?

## Goals
- Goal 1
- Goal 2

## Core Requirements
- Requirement 1
- Requirement 2
```

#### 2. Architecture (`architecture.md`)

Describe your system design:

```markdown
# Architecture

## System Overview
High-level architecture...

## Components
### Frontend
- Technology: React
- Responsibilities: UI, user interaction

### Backend
- Technology: FastAPI
- Responsibilities: API, business logic

## Data Flow
Request → Frontend → API → Database → Response
```

#### 3. Technical (`technical.md`)

Document your tech stack:

```markdown
# Technical Documentation

## Technology Stack
- Language: Python 3.11
- Framework: FastAPI
- Database: PostgreSQL
- Testing: pytest

## Development Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Key Technical Decisions
- Using FastAPI for async performance
- PostgreSQL for relational data
```

#### 4. Tasks Plan (`tasks_plan.md`)

Track your work:

```markdown
# Tasks Plan

## Completed
- [x] Set up project structure
- [x] Create database schema

## In Progress
- [ ] Implement user authentication

## Planned
- [ ] Add API rate limiting
- [ ] Set up monitoring
```

#### 5. Active Context (`active_context.md`)

Current state:

```markdown
# Active Context

## Current Focus
Implementing user authentication with JWT tokens

## Recent Changes
- Added User model
- Created authentication endpoints

## Next Steps
- Add token refresh
- Implement role-based access
```

### Memory File Tips

1. **Start Simple**: Fill in the basics, expand as you go
2. **Keep Updated**: Update after major changes
3. **Be Specific**: Concrete details > vague descriptions
4. **Ask AI to Help**: Let your AI assistant help document
5. **Trigger Updates**: Say "update memory files" to your AI

## Common Workflows

### Workflow 1: Planning a Feature

```bash
# 1. Talk to your AI assistant
"I want to add user authentication. Let's plan it out. FOCUS = PLANNING"

# The AI will:
# - Read your Memory Files
# - Analyze requirements
# - Propose a detailed plan
# - Request your approval

# 2. Approve the plan
"Looks good, let's implement it"
```

### Workflow 2: Implementing Code

```bash
# 1. Request implementation
"Implement the authentication endpoints. FOCUS = IMPLEMENTATION"

# The AI will:
# - Follow the approved plan
# - Write code with best practices
# - Add tests
# - Update documentation

# 2. Review and iterate
"The login endpoint works, but add password hashing"
```

### Workflow 3: Debugging Issues

```bash
# 1. Report the bug
"The /api/login endpoint returns 500 error. FOCUS = DEBUGGING"

# The AI will:
# - Analyze the error
# - Check error-documentation.md
# - Diagnose the issue
# - Propose a fix
# - Update error documentation

# 2. Verify the fix
"Test the fix with curl"
```

### Workflow 4: Switching Assistants

```bash
# Sync for a different assistant
uvx rulebook-ai project sync --assistant copilot

# Now use GitHub Copilot with the same rules!
```

### Workflow 5: Updating Memory

```bash
# Ask AI to update memory files
"We just finished authentication. Update memory files."

# The AI will:
# - Review all core files
# - Update tasks_plan.md
# - Update active_context.md
# - Document lessons learned
```

## Next Steps

### Learn More

1. **Explore Packs**: [Packs Overview](Packs-Overview.md)
   - Understand different pack levels
   - Learn when to use each pack

2. **Understand Rules**: [Rules Categories](Rules-Categories.md)
   - Deep dive into rule categories
   - Learn how workflows work

3. **Advanced Topics**: [Advanced Topics](Advanced-Topics.md)
   - Create custom packs
   - Use profiles
   - Contribute to community

### Best Practices

1. **Commit Memory Files**: They're your project's knowledge base
2. **Keep Memory Updated**: Accurate context = better AI assistance
3. **Start with Light-Spec**: Upgrade to medium/heavy only if needed
4. **Use Explicit Focus**: Add `FOCUS = PLANNING` when needed
5. **Document Errors**: Update `error-documentation.md` after fixes

### Common Questions

**Q: Do I need to use all seven Memory Bank files?**  
A: Start with the core ones (product_requirement_docs, architecture, technical, tasks_plan). Add others as your project grows.

**Q: Can I use multiple packs?**  
A: Yes! Combine packs to create the perfect environment.

**Q: What if my AI assistant isn't supported?**  
A: File an issue on GitHub. We're always adding support for new assistants.

**Q: Can I customize the rules?**  
A: Absolutely! Create a custom pack or modify generated rules.

**Q: Do I need to re-sync after every change?**  
A: Only when you add/remove packs. Memory file updates don't require syncing.

### Troubleshooting

**Rules not working?**
- Check that you ran `project sync`
- Verify assistant is configured to use rules
- Check generated files are in correct location

**AI not using Memory Files?**
- Ensure files are filled out
- Try "read memory files" or "update memory files"
- Check file paths are correct

**Pack not found?**
- Verify pack name with `packs list`
- Check network connection for community packs
- Ensure local paths are correct for local packs

### Get Help

- **Discord**: [Join our Discord](https://discord.gg/aNmQB7JWPe)
- **Issues**: Report bugs on GitHub
- **Book a Chat**: [Schedule a demo](https://calendar.app.google/xx3S3CuKSBAt9d9Y7)

---

**You're ready!** Start building with your AI assistant powered by Rulebook-AI. Remember: the Memory Bank is your project's second brain—keep it updated and watch your AI assistance improve over time.

**Next**: Deep dive into [Packs Overview](Packs-Overview.md) or [Rules Categories](Rules-Categories.md).
