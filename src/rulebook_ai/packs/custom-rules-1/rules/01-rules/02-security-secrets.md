# Security and secrets

- Never commit secrets or tokens to version control.
- Use environment variables or secrets managers.
- Prefer least-privilege credentials for each service.
- Rotate credentials immediately if exposed.
- Avoid printing secrets in logs or stack traces.
- Treat clipboard or chat output as public unless protected.
- Store API keys in environment files (e.g., .env) and commit only examples.

## Privileged operations
- Avoid sudo or root actions unless explicitly requested.
- Use non-destructive commands by default.
- Document any elevated action and its purpose.
