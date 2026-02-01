# Error handling and recovery

- Do not ignore errors; handle or propagate explicitly.
- Prefer actionable error messages with context.
- Avoid catching broad exceptions without rethrowing or logging.
- Handle syntax, compile, and runtime errors at the source.
- Do not suppress compiler errors; fix the underlying issue.
- Validate inputs at boundaries and fail fast.
