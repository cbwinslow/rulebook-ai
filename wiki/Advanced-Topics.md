# Advanced Topics

This page covers advanced features, customization options, and pack development for experienced Rulebook-AI users.

## Table of Contents

- [Profiles](#profiles)
- [Custom Packs](#custom-packs)
- [Pack Development](#pack-development)
- [Rule Customization](#rule-customization)
- [Multi-Assistant Workflows](#multi-assistant-workflows)
- [Integration Patterns](#integration-patterns)
- [Community Packs](#community-packs)
- [Troubleshooting](#troubleshooting)

## Profiles

Profiles are named groups of packs that let you switch between different configurations instantly.

### What are Profiles?

A profile is a named collection of packs for a specific purpose or context. For example:
- `backend` profile: Python, FastAPI, PostgreSQL rules
- `frontend` profile: React, TypeScript, testing rules
- `devops` profile: Docker, Kubernetes, AWS rules

### Creating Profiles

```bash
# Create a profile with packs
uvx rulebook-ai profiles create backend light-spec

# Add more packs to a profile
uvx rulebook-ai profiles add backend github:community/python-expert

# Create different profiles
uvx rulebook-ai profiles create frontend light-spec
uvx rulebook-ai profiles add frontend github:community/react-expert
```

### Using Profiles

```bash
# List all profiles
uvx rulebook-ai profiles list

# Activate a profile
uvx rulebook-ai profiles activate backend

# This loads all packs from the 'backend' profile
# and syncs your environment

# Switch to another profile
uvx rulebook-ai profiles activate frontend
```

### Profile Management

```bash
# Show current profile
uvx rulebook-ai profiles current

# Remove a pack from a profile
uvx rulebook-ai profiles remove backend github:community/python-expert

# Delete a profile
uvx rulebook-ai profiles delete backend
```

### Use Cases

**Multi-Language Project**:
```bash
# Backend work
uvx rulebook-ai profiles create backend light-spec
uvx rulebook-ai profiles activate backend

# Frontend work
uvx rulebook-ai profiles create frontend light-spec
uvx rulebook-ai profiles activate frontend
```

**Different Project Phases**:
```bash
# Planning phase
uvx rulebook-ai profiles create planning heavy-spec
uvx rulebook-ai profiles activate planning

# Development phase
uvx rulebook-ai profiles create dev light-spec
uvx rulebook-ai profiles activate dev

# Code review phase
uvx rulebook-ai profiles create review medium-spec
uvx rulebook-ai profiles activate review
```

## Custom Packs

### When to Create Custom Packs

Create custom packs when you need:
- Organization-specific rules
- Framework-specific guidelines
- Team conventions
- Private/proprietary instructions
- Specialized workflows

### Quick Custom Pack

The fastest way to create a custom pack:

```bash
# 1. Add the pack authoring guide
uvx rulebook-ai packs add pack-authoring-guide

# 2. Create pack structure
mkdir -p my-custom-pack/rules/01-rules
mkdir -p my-custom-pack/memory_starters/docs
mkdir -p my-custom-pack/tool_starters

# 3. Add a README
cat > my-custom-pack/README.md << 'EOF'
# My Custom Pack

Custom rules for my organization/project.

## Purpose
Description of what this pack provides...

## When to Use
When working on projects that...
EOF

# 4. Add your first rule
cat > my-custom-pack/rules/01-rules/01-custom.md << 'EOF'
---
description: Custom organizational rules
alwaysApply: true
---

# Custom Rules

Your custom instructions here...
EOF

# 5. Test it locally
uvx rulebook-ai packs add local:./my-custom-pack
uvx rulebook-ai project sync
```

### Custom Pack Structure

```
my-custom-pack/
├── README.md                      # Pack documentation
├── rules/                         # Rule files
│   ├── 01-rules/                 # Core rules
│   │   ├── 01-custom-principles.md
│   │   └── 02-team-conventions.md
│   ├── 02-rules-architect/       # Optional: planning rules
│   ├── 03-rules-code/            # Optional: coding rules
│   └── 04-rules-debug/           # Optional: debug rules
├── memory_starters/              # Documentation templates
│   ├── docs/
│   │   └── custom-doc.md
│   └── tasks/
│       └── custom-task.md
└── tool_starters/                # Helper scripts
    └── custom-tool.py
```

### Example Custom Pack

**Organization Standards Pack**:

```markdown
# my-org-pack/rules/01-rules/01-org-standards.md
---
description: Organization coding standards and conventions
alwaysApply: true
---

# Organization Standards

## Code Review Requirements
- All code must have tests
- Maximum function length: 50 lines
- Follow PEP 8 for Python

## Documentation Requirements
- All public APIs must have docstrings
- README for every package

## Security Requirements
- Never commit secrets
- Use environment variables for config
- Follow OWASP guidelines
```

### Sharing Custom Packs

**Option 1: GitHub Repository**
```bash
# Create a GitHub repo
gh repo create my-org/custom-pack --public

# Push your pack
cd my-custom-pack
git init
git add .
git commit -m "Initial custom pack"
git remote add origin https://github.com/my-org/custom-pack.git
git push -u origin main

# Others can use it
uvx rulebook-ai packs add github:my-org/custom-pack
```

**Option 2: Internal Git Server**
```bash
# Push to internal server
git remote add origin https://git.internal.company/custom-pack.git
git push -u origin main

# Team members use it
uvx rulebook-ai packs add github:company/custom-pack
```

**Option 3: File Share**
```bash
# Share via network drive
cp -r my-custom-pack /shared/packs/

# Team members use it
uvx rulebook-ai packs add local:/shared/packs/my-custom-pack
```

## Pack Development

For comprehensive pack development, consult these resources:

### Essential Documentation

1. **Pack Developer Guide**: `memory/docs/features/community_packs/pack_developer_guide.md`
   - Complete guide to creating packs
   - Best practices
   - Publishing process

2. **Pack Structure Spec**: Available via `pack-authoring-guide` pack
   - Detailed structure requirements
   - File format specifications

3. **Platform Rules Spec**: Available via `pack-authoring-guide` pack
   - Assistant-specific format details
   - Output generation rules

### Development Workflow

```bash
# 1. Start with pack authoring guide
uvx rulebook-ai packs add pack-authoring-guide

# 2. Review the documentation
cat memory/docs/pack_structure_spec.md
cat memory/docs/pack_developer_guide.md

# 3. Create your pack structure
mkdir my-pack && cd my-pack
mkdir -p rules/01-rules memory_starters tool_starters

# 4. Write your rules
vim rules/01-rules/01-core.md

# 5. Test locally
uvx rulebook-ai packs add local:.
uvx rulebook-ai project sync --assistant cursor

# 6. Validate
uvx rulebook-ai packs validate .

# 7. Iterate based on feedback
vim rules/01-rules/01-core.md
uvx rulebook-ai project sync --assistant cursor
```

### Pack Testing

**Test with Multiple Assistants**:
```bash
# Test with Cursor
uvx rulebook-ai project sync --assistant cursor

# Test with Copilot
uvx rulebook-ai project sync --assistant copilot

# Test with all
uvx rulebook-ai project sync --all
```

**Test in Isolation**:
```bash
# Remove other packs
uvx rulebook-ai packs remove light-spec

# Add only your pack
uvx rulebook-ai packs add local:./my-pack

# Sync and test
uvx rulebook-ai project sync
```

### Pack Validation

```bash
# Validate pack structure
uvx rulebook-ai packs validate /path/to/pack

# Common validation checks:
# - README.md exists
# - rules/ directory exists
# - At least one rule file
# - Valid YAML frontmatter
# - Proper directory structure
```

## Rule Customization

### Extending Built-in Rules

Add to existing rules without modifying them:

```bash
# Create extension pack
mkdir rule-extensions
mkdir -p rule-extensions/rules/01-rules

# Add extension rule
cat > rule-extensions/rules/01-rules/10-extensions.md << 'EOF'
---
description: Extensions to light-spec rules
alwaysApply: true
---

# Rule Extensions

## Additional Code Quality Rules
- Use type hints in all Python functions
- Maximum cognitive complexity: 10

## Additional Testing Rules
- Minimum test coverage: 80%
- Integration tests required for APIs
EOF

# Use it
uvx rulebook-ai packs add light-spec
uvx rulebook-ai packs add local:./rule-extensions
uvx rulebook-ai project sync
```

### Overriding Rules

Replace specific rules with your own:

```bash
# Create override pack
mkdir rule-overrides
mkdir -p rule-overrides/rules/01-rules

# Override a rule (same filename)
cat > rule-overrides/rules/01-rules/06-rules_v1.md << 'EOF'
---
description: Custom principles overriding defaults
alwaysApply: true
---

# Custom Principles

These replace the default principles...
EOF

# Load overrides AFTER original pack
uvx rulebook-ai packs add light-spec
uvx rulebook-ai packs add local:./rule-overrides
uvx rulebook-ai project sync
```

### Conditional Rules

Create rules that apply only in specific contexts:

```markdown
---
description: Python-specific rules
globs: ["*.py", "**/*.py"]
alwaysApply: false
---

# Python-Specific Rules

These rules only apply when working with Python files:

- Use Black for formatting
- Follow PEP 8
- Use type hints
```

### Dynamic Rules

Create rules that adapt based on conditions:

```markdown
# In meta-rules or custom rule

## Project Type Detection
If project contains `package.json`:
    → Load JavaScript/Node.js rules
If project contains `requirements.txt`:
    → Load Python rules
If project contains `go.mod`:
    → Load Go rules
```

## Multi-Assistant Workflows

### Using Multiple Assistants

Different assistants have different strengths. Use the right tool for each task:

```bash
# Sync for all your assistants
uvx rulebook-ai project sync --assistant cursor copilot gemini

# Now use:
# - Cursor for complex refactoring
# - Copilot for quick completions
# - Gemini for research and exploration
```

### Assistant-Specific Rules

Create rules that work better with specific assistants:

```markdown
# rules/01-rules/10-assistant-specific.md
---
description: Assistant-specific guidance
alwaysApply: true
---

# Assistant-Specific Guidance

## For Cursor Users
When in Cursor, use the Command+K for inline edits...

## For Copilot Users
When using Copilot, leverage inline suggestions...

## For Gemini Users
When using Gemini CLI, provide full context...
```

### Team Workflows

**Scenario**: Team uses different assistants

```bash
# Commit pack configuration
git add .rulebook-ai/packs.yaml
git commit -m "Add Rulebook-AI configuration"

# Each team member syncs for their assistant
# Team member 1 (uses Cursor):
uvx rulebook-ai project sync --assistant cursor

# Team member 2 (uses Copilot):
uvx rulebook-ai project sync --assistant copilot

# Everyone has the same rules in their preferred format!
```

## Integration Patterns

### CI/CD Integration

Validate rules in CI/CD:

```yaml
# .github/workflows/validate-rules.yml
name: Validate Rulebook-AI Configuration

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Install uv
        run: curl -fsSL https://astral.sh/uv/install.sh | bash
      
      - name: Install Rulebook-AI
        run: uv tool install rulebook-ai
      
      - name: Validate packs
        run: |
          for pack in custom-packs/*; do
            uvx rulebook-ai packs validate "$pack"
          done
```

### Pre-commit Hooks

Sync rules before commits:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: sync-rules
        name: Sync Rulebook-AI Rules
        entry: uvx rulebook-ai project sync
        language: system
        pass_filenames: false
        always_run: true
```

### Docker Integration

Include rules in Docker images:

```dockerfile
# Dockerfile
FROM python:3.11

# Install uv
RUN curl -fsSL https://astral.sh/uv/install.sh | bash

# Install Rulebook-AI
RUN uv tool install rulebook-ai

# Copy project
COPY . /app
WORKDIR /app

# Sync rules
RUN uvx rulebook-ai project sync --all
```

### VS Code Integration

Add tasks to VS Code:

```json
// .vscode/tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Sync Rulebook-AI",
      "type": "shell",
      "command": "uvx rulebook-ai project sync",
      "problemMatcher": []
    },
    {
      "label": "Update Memory Files",
      "type": "shell",
      "command": "code memory/",
      "problemMatcher": []
    }
  ]
}
```

## Community Packs

### Finding Community Packs

```bash
# Search community index (when available)
uvx rulebook-ai packs search react

# Browse GitHub
# Search for "rulebook-ai-pack" topic
https://github.com/topics/rulebook-ai-pack
```

### Using Community Packs

```bash
# Add from GitHub
uvx rulebook-ai packs add github:username/pack-name

# Add specific version/branch
uvx rulebook-ai packs add github:username/pack-name@v1.0.0
uvx rulebook-ai packs add github:username/pack-name@main
```

### Contributing Community Packs

1. **Create Your Pack**:
   ```bash
   uvx rulebook-ai packs add pack-authoring-guide
   # Follow the guide to create your pack
   ```

2. **Test Thoroughly**:
   ```bash
   uvx rulebook-ai packs add local:./my-pack
   uvx rulebook-ai project sync --all
   # Test with multiple assistants
   ```

3. **Publish to GitHub**:
   ```bash
   gh repo create my-pack --public
   git add .
   git commit -m "Initial pack"
   git push -u origin main
   
   # Add topic for discoverability
   gh repo edit --add-topic rulebook-ai-pack
   ```

4. **Submit to Community Index** (when available):
   - Follow contribution guidelines
   - Submit PR to community index repo

### Pack Quality Guidelines

**Good Packs**:
- ✅ Clear README with purpose and usage
- ✅ Well-organized rules
- ✅ Tested with multiple assistants
- ✅ Versioned and maintained
- ✅ Examples and documentation

**Avoid**:
- ❌ Overly specific rules (unless intentional)
- ❌ Hardcoded paths or credentials
- ❌ Conflicting with common packs
- ❌ Poor documentation

## Troubleshooting

### Pack Issues

**Pack not found**:
```bash
# Verify pack exists
uvx rulebook-ai packs list

# Check pack name spelling
uvx rulebook-ai packs search <name>

# For GitHub packs, verify repo exists
curl https://github.com/username/pack-name
```

**Pack validation fails**:
```bash
# Check validation errors
uvx rulebook-ai packs validate /path/to/pack

# Common issues:
# - Missing README.md
# - Invalid YAML frontmatter
# - Missing rules/ directory
# - Improper file structure
```

### Sync Issues

**Rules not generating**:
```bash
# Check sync output for errors
uvx rulebook-ai project sync --verbose

# Verify assistant name
uvx rulebook-ai project sync --assistant cursor  # Not "Cursor"

# Check file permissions
ls -la .cursor/
```

**Rules not being used**:
```bash
# Verify assistant configuration
# For Cursor: Check .cursor/rules/ exists
# For Copilot: Check .github/copilot-instructions.md exists

# Re-sync
uvx rulebook-ai project sync --assistant <assistant>
```

### Memory File Issues

**AI not using memory files**:
```bash
# Check file paths in rules
grep "memory/" .cursor/rules/*.md

# Verify files exist
ls -la memory/docs/
ls -la memory/tasks/

# Try explicit command
"Read all memory files"
```

**Memory files outdated**:
```bash
# Ask AI to update
"Update all memory files"

# Manual update
vim memory/tasks/active_context.md
```

### Performance Issues

**Slow sync**:
```bash
# Sync only needed assistant
uvx rulebook-ai project sync --assistant cursor

# Instead of:
uvx rulebook-ai project sync --all
```

**Large generated files**:
```bash
# Check size
du -sh .cursor/rules/

# Consider splitting rules if files are large
# Remove unnecessary packs
uvx rulebook-ai packs remove unused-pack
```

## Best Practices Summary

### For Pack Users
1. Start with light-spec
2. Keep memory files updated
3. Commit memory/ and tools/
4. Ignore generated files
5. Use profiles for different contexts

### For Pack Developers
1. Follow pack structure spec
2. Test with multiple assistants
3. Document your pack well
4. Version your releases
5. Respond to user feedback

### For Teams
1. Share pack configuration
2. Standardize on packs
3. Create org-specific packs
4. Document team conventions
5. Review memory files together

---

**Additional Resources**:
- [Pack Developer Guide](../memory/docs/features/community_packs/pack_developer_guide.md)
- [Contributing Guide](../CONTRIBUTING.md)
- [Discord Community](https://discord.gg/aNmQB7JWPe)

**Back to**: [Home](Home.md) | [Getting Started](Getting-Started.md) | [Packs Overview](Packs-Overview.md)
