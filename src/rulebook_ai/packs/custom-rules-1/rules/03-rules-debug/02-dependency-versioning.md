# Dependency, versioning, and package management

- Use the existing package manager for the repo.
- Keep lockfiles in sync with dependency changes.
- Do not change versions without a stated reason.
- Address version conflicts by aligning constraints, not by pinning blindly.
- If a dependency error appears, confirm the correct runtime and environment.
- Prefer semver-compatible ranges and document breaking upgrades.
