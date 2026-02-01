# Core principles

## Content ethics and compliance
- Use only original or properly licensed assets.
- Document licenses for every external asset.
- No unlicensed reuploads or direct copies.
- Follow platform ToS and API rate limits.
- Do not bypass authentication or safety systems.
- Respect upload size, duration, and format limits.

## Automation safety
- Require explicit approval for publishing in early tests.
- Log every workflow run and upload result.
- Keep secrets out of repo and logs.

## Modularity and swap-ability
- Centralize defaults in configuration files.
- Allow per-run overrides in inputs.
- Keep providers behind thin adapters.
- Avoid hard dependencies on a single model or vendor.

## Engineering discipline
- Avoid brittle fixes that reduce maintainability.
- Prefer well-scoped, durable changes.
- Address root causes over surface symptoms.
