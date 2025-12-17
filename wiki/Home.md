# Rulebook-AI Wiki

Welcome to the Rulebook-AI wiki! This documentation provides comprehensive information about the rules, categories, groupings, and pack system used in Rulebook-AI.

## Quick Navigation

### Getting Started
- [Getting Started Guide](Getting-Started.md) - Quick start instructions and basic concepts
- [Tutorial](../memory/docs/user_guide/tutorial.md) - Step-by-step tutorial from the main documentation

### Core Concepts
- [Packs Overview](Packs-Overview.md) - Comprehensive guide to all available packs
- [Rules Categories](Rules-Categories.md) - Detailed documentation of rule categories and groupings
- [Rule Structure](Rule-Structure.md) - Understanding the rule file organization and hierarchy

### Advanced Topics
- [Advanced Topics](Advanced-Topics.md) - Advanced configuration, customization, and pack development
- [Supported Assistants](../memory/docs/user_guide/supported_assistants.md) - AI assistants compatibility

## What is Rulebook-AI?

`rulebook-ai` is a command-line tool for packaging and deploying consistent, expert environments—**rules, context, and tools**—to your favorite AI coding assistants.

### The Three Pillars

1. **Rules**: The AI's operating instructions and workflows
2. **Context**: A persistent knowledge base (your project's "memory")
3. **Tools**: Helper scripts the AI can use to perform tasks

These are packaged into versionable, shareable **Packs** that can be deployed across different AI assistants.

## Key Features

- **Portability Across Assistants**: Define once, deploy anywhere (Cursor, Gemini, Copilot, etc.)
- **Deep Specialization**: Create or use role-specific packs (Product Manager, DevOps, etc.)
- **Composable Context**: Mix and match packs to build the perfect setup
- **Community-Driven**: Share and discover packs from the community
- **Clean Workspace**: Separates user content from generated artifacts

## Documentation Structure

### Core Documentation
This wiki focuses on the **rules system**, pack structure, and categories. For other topics:

- **User Guide**: See [memory/docs/user_guide/](../memory/docs/user_guide/) for tutorials and guides
- **Feature Documentation**: See [memory/docs/features/](../memory/docs/features/) for detailed feature docs
- **Architecture**: See [memory/docs/architecture.md](../memory/docs/architecture.md) for system design

### Wiki Pages

1. **[Getting Started](Getting-Started.md)**: Quick start guide for new users
2. **[Packs Overview](Packs-Overview.md)**: Detailed information about all built-in packs
3. **[Rules Categories](Rules-Categories.md)**: Complete guide to rule categories and their purposes
4. **[Rule Structure](Rule-Structure.md)**: Understanding how rules are organized and loaded
5. **[Advanced Topics](Advanced-Topics.md)**: Pack development, custom rules, and advanced features

## Quick Start

```bash
# 1. Install uv if you don't have it yet
curl -fsSL https://astral.sh/uv/install.sh | bash

# 2. Add a pack to your project
uvx rulebook-ai packs add light-spec

# 3. Sync the environment to your workspace
uvx rulebook-ai project sync
```

## Support & Community

- **Discord**: [Join our Discord](https://discord.gg/aNmQB7JWPe) for real-time support
- **Issues**: Report bugs or request features on GitHub
- **Demos**: [Book a chat](https://calendar.app.google/xx3S3CuKSBAt9d9Y7) for personalized help

## Contributing

We welcome contributions! See:
- [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines
- [Pack Developer Guide](../memory/docs/features/community_packs/pack_developer_guide.md) for creating packs
- [Pack Authoring Guide Pack](Packs-Overview.md#pack-authoring-guide) for conversion assistance

---

**Next Steps**: Start with the [Getting Started Guide](Getting-Started.md) or dive into [Packs Overview](Packs-Overview.md) to learn about available packs.
