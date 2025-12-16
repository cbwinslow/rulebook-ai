# Packs Overview

This page provides comprehensive documentation of all available packs in Rulebook-AI, including their purpose, structure, and when to use them.

## Table of Contents

- [What is a Pack?](#what-is-a-pack)
- [Pack Selection Guide](#pack-selection-guide)
- [Built-in Packs](#built-in-packs)
  - [Light-Spec](#light-spec)
  - [Medium-Spec](#medium-spec)
  - [Heavy-Spec](#heavy-spec)
  - [No Memory Interaction Rules](#no-memory-interaction-rules)
  - [Pack Authoring Guide](#pack-authoring-guide)
  - [Test Set](#test-set)
- [Pack Structure](#pack-structure)
- [Using Packs](#using-packs)

## What is a Pack?

A **Pack** is a self-contained bundle that defines an AI environment. Each pack contains:

1. **Rules** (`rules/`): Instruction files that guide AI behavior and workflows
2. **Memory Starters** (`memory_starters/`): Template documentation for your project's knowledge base
3. **Tool Starters** (`tool_starters/`): Helper scripts and utilities

Packs are versionable, shareable, and can be sourced from:
- Built-in packs (bundled with Rulebook-AI)
- Community packs (public index)
- GitHub repositories (`github:user/repo`)
- Local filesystem (`local:/path/to/pack`)

## Pack Selection Guide

Choose the right pack based on your project needs:

| Pack | Best For | Overhead | Detail Level |
|------|----------|----------|--------------|
| **light-spec** | Most projects, individual developers, prototypes | Low | Concise |
| **medium-spec** | General-purpose, moderate complexity | Medium | Balanced |
| **heavy-spec** | Large projects, strict compliance, new teams | High | Very detailed |
| **no_memory_interation_rules** | Tasks without context requirements | Minimal | Context-free |
| **pack-authoring-guide** | Pack developers, contributors | N/A | Reference |

### Decision Tree

```
Do you need maximum rigor and traceability?
├─ Yes → heavy-spec
└─ No
   └─ Is this a moderately complex project?
      ├─ Yes → medium-spec
      └─ No → light-spec (recommended default)
```

## Built-in Packs

### Light-Spec

**Purpose**: The recommended starting point for any project. Transforms your AI into a junior developer with structured workflows.

**When to Use**:
- Individual developers & small teams
- Most general-purpose projects
- Prototyping and innovation
- When you want minimal overhead with maximum benefit

**Key Features**:
- ✅ Structured Memory Bank system
- ✅ Systematic workflows for planning, coding, and debugging
- ✅ Foundational software engineering principles
- ✅ Context-aware AI behavior

**Pack Contents**:
```
light-spec/
├── rules/
│   ├── 01-rules/
│   │   ├── 00-meta-rules.md          # Focus determination & mode logic
│   │   ├── 01-memory.md              # Memory files structure
│   │   ├── 02-error-documentation.md # Error tracking
│   │   ├── 03-lessons-learned.md     # Learning journal
│   │   ├── 04-archiecture-understanding.md # Architecture guidelines
│   │   ├── 05-directory-structure.md # Project structure
│   │   └── 06-rules_v1.md           # General best practices
│   ├── 02-rules-architect/
│   │   └── 01-plan_v1.md            # Planning workflow
│   ├── 03-rules-code/
│   │   └── 01-code_v1.md            # Implementation workflow
│   └── 04-rules-debug/
│       └── 01-debug_v1.md           # Debugging workflow
├── memory_starters/
│   ├── docs/
│   │   ├── product_requirement_docs.md
│   │   ├── architecture.md
│   │   └── technical.md
│   └── tasks/
│       ├── tasks_plan.md
│       └── active_context.md
└── tool_starters/
    └── (various helper scripts)
```

**Rule Categories**:
1. **Meta-Rules** (00): Focus determination and operational mode logic
2. **Context Files** (01-05): Project structure and memory management
3. **General Principles** (06): Core best practices
4. **Workflow-Specific** (02-04 directories): Planning, coding, debugging

**Installation**:
```bash
uvx rulebook-ai packs add light-spec
uvx rulebook-ai project sync
```

### Medium-Spec

**Purpose**: Balanced ruleset that trims verbosity while maintaining clear structure and validation points.

**When to Use**:
- General-purpose projects with moderate complexity
- Teams comfortable with AI but wanting clear structure
- When heavy-spec feels too cumbersome
- When light-spec seems too loose

**Key Differences from Light-Spec**:
- ⚖️ More explicit guidance and validation checkpoints
- ⚖️ Additional clarification in workflow steps
- ⚖️ More verbose explanations of processes
- ⚖️ Stricter guardrails

**Pack Structure**: Same directory structure as light-spec, but with more detailed rule files.

**Installation**:
```bash
uvx rulebook-ai packs add medium-spec
uvx rulebook-ai project sync
```

### Heavy-Spec

**Purpose**: Most detailed and prescriptive ruleset for maximum rigor and traceability.

**When to Use**:
- Large, complex projects requiring maximum rigor
- Teams new to human-AI collaboration
- Less capable AI models needing explicit instructions
- Strict compliance or validation requirements
- When predictability is paramount

**Key Features**:
- 📋 Maximum guardrails and explicit workflow steps
- 📋 Detailed validation at each step
- 📋 Comprehensive documentation requirements
- 📋 Extensive context gathering procedures

**Target Scenarios**:
- Enterprise projects with compliance requirements
- Mission-critical systems
- Educational environments learning AI collaboration
- Projects using less capable AI models

**Pack Structure**: Same directory structure as light-spec and medium-spec, but with significantly more detailed and prescriptive rules.

**Installation**:
```bash
uvx rulebook-ai packs add heavy-spec
uvx rulebook-ai project sync
```

### No Memory Interaction Rules

**Purpose**: Rules that operate without interacting with the Memory Bank system.

**When to Use**:
- One-off tasks not requiring project context
- Stateless operations
- Quick prototypes or experiments
- When Memory Bank overhead is unnecessary

**Key Features**:
- 🚀 Minimal overhead
- 🚀 No memory file dependencies
- 🚀 Context-free operation
- 🚀 Fast setup

**Use Cases**:
- Standalone scripts
- Generic coding tasks
- External tool integration
- Temporary or disposable projects

**Installation**:
```bash
uvx rulebook-ai packs add no_memory_interation_rules
uvx rulebook-ai project sync
```

### Pack Authoring Guide

**Purpose**: Built-in pack to assist contributors in creating new packs that conform to Rulebook-AI specifications.

**When to Use**:
- Creating a new pack
- Converting existing rules to pack format
- Contributing to the community
- Learning pack structure

**Includes**:
- 📚 Step-by-step conversion guide
- 📚 Validation checklist
- 📚 Reference documentation (pack_structure_spec.md, platform_rules_spec.md)
- 📚 Validation scripts

**Pack Contents**:
```
pack-authoring-guide/
├── rules/
│   └── 01-rules/
│       ├── 01-conversion-guide.md
│       ├── 02-validation-checklist.md
│       └── 03-operational-notes.md
├── memory_starters/
│   └── docs/
│       ├── pack_structure_spec.md
│       ├── pack_developer_guide.md
│       └── platform_rules_spec.md
└── tool_starters/
    └── validate_pack.py
```

**Usage**:
```bash
# Add the guide
uvx rulebook-ai packs add pack-authoring-guide

# Validate your pack
uvx rulebook-ai packs add /path/to/your/pack
```

**See Also**: [Pack Developer Guide](../memory/docs/features/community_packs/pack_developer_guide.md)

### Test Set

**Purpose**: Minimal pack for testing CLI functionality and core logic.

**When to Use**:
- Internal testing
- Continuous integration
- Development and debugging of Rulebook-AI itself

**Note**: Not intended for production use.

## Pack Structure

All packs follow a consistent structure:

```
pack-name/
├── README.md                 # Pack documentation
├── rules/                    # Rule instruction files
│   ├── 01-rules/            # Core rules and context
│   ├── 02-rules-architect/  # Planning workflow (optional)
│   ├── 03-rules-code/       # Implementation workflow (optional)
│   └── 04-rules-debug/      # Debugging workflow (optional)
├── memory_starters/         # Template documentation
│   ├── docs/               # Documentation templates
│   └── tasks/              # Task management templates
└── tool_starters/          # Helper scripts
```

### Directory Purposes

| Directory | Purpose | When Deployed |
|-----------|---------|---------------|
| `rules/` | AI instructions and workflows | Generated into assistant-specific formats |
| `memory_starters/` | Project documentation templates | Copied to `memory/` on first sync |
| `tool_starters/` | Helper scripts and utilities | Copied to `tools/` on first sync |

### Rule Loading Order

Rules are loaded in alphanumeric order by filename:
1. `01-rules/00-meta-rules.md` - First (if exists)
2. `01-rules/01-*.md` through `01-rules/99-*.md` - In order
3. `02-rules-architect/` - Workflow-specific
4. `03-rules-code/` - Workflow-specific
5. `04-rules-debug/` - Workflow-specific

See [Rule Structure](Rule-Structure.md) for detailed information.

## Using Packs

### Adding Packs

```bash
# Built-in pack
uvx rulebook-ai packs add light-spec

# From GitHub
uvx rulebook-ai packs add github:username/repo-name

# From local filesystem
uvx rulebook-ai packs add local:/path/to/pack
```

### Listing Packs

```bash
uvx rulebook-ai packs list
```

### Removing Packs

```bash
uvx rulebook-ai packs remove pack-name
```

### Syncing to Project

```bash
# Sync with default assistant (Cursor)
uvx rulebook-ai project sync

# Sync with specific assistant
uvx rulebook-ai project sync --assistant cursor

# Sync for multiple assistants
uvx rulebook-ai project sync --assistant cursor copilot

# Sync for all supported assistants
uvx rulebook-ai project sync --all
```

### Using Profiles

Profiles are named groups of packs for instant configuration switching:

```bash
# Create a profile
uvx rulebook-ai profiles create backend light-spec

# Switch profiles
uvx rulebook-ai profiles activate backend

# List profiles
uvx rulebook-ai profiles list
```

## Combining Packs

You can add multiple packs to create a customized environment:

```bash
# Core development pack
uvx rulebook-ai packs add light-spec

# Add specialized packs
uvx rulebook-ai packs add github:community/react-expert
uvx rulebook-ai packs add github:community/aws-devops

# Sync everything
uvx rulebook-ai project sync
```

When multiple packs are active:
- Rules are merged in the order packs were added
- Later packs can override earlier ones
- Memory and tool starters are combined

## Creating Custom Packs

To create your own pack:

1. Add the pack authoring guide:
   ```bash
   uvx rulebook-ai packs add pack-authoring-guide
   ```

2. Follow the structure and guidelines in the guide

3. Test locally:
   ```bash
   uvx rulebook-ai packs add local:/path/to/your/pack
   uvx rulebook-ai project sync
   ```

4. Share via GitHub or contribute to community index

See [Advanced Topics](Advanced-Topics.md) for detailed pack development instructions.

---

**Next**: Learn about [Rules Categories](Rules-Categories.md) to understand how individual rules are organized and categorized.
