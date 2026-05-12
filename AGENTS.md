# Agent Instructions (Repo-Wide)

- Do not edit/add/delete any files unless the user explicitly asks you to code (e.g. “go
  ahead”, “implement”, “make the changes”).
- You may read files, inspect code, and propose approaches first; ask for explicit
  confirmation before applying patches.
- Confirm intended scope before starting; if a request expands, call it out and
  reconfirm before proceeding.
- For multi-step changes, first define the phases with the user. Then handle one
  phase at a time: discuss the design, confirm the scope, inspect the current
  state, and only then implement that phase.
- If a request is ambiguous, ask clarifying questions instead of guessing.
- When searching code, exclude cache/generated directories by default: `.mypy_cache`,
  `__pycache__`, `.ruff_cache`, `.pytest_cache`.
- Use the project virtualenv for Python/Django commands. Prefer `.venv/bin/python`
  over relying on an activated shell environment.
- Request escalated access before running Django commands that need database
  connectivity, since local Postgres may be unreachable from the sandbox.
- Do not run test suites by default; the user runs tests manually. Only run tests when
  explicitly requested.

## Regression Handling

- If the user reports that a change broke the app, do not guess and do not apply
  speculative fixes.
- First obtain the concrete failure signal: traceback, failing request, failing test,
  or exact endpoint/action.
- Identify the specific change that caused the regression before editing code.
- If multiple recent edits are suspects, inspect and explain the likely candidates, but
  do not modify code until the failure is localized.
- Reverts must be evidence-based, not speculative.
- When a regression is reported, never make a code change before seeing either:
  - the traceback
  - the failing test
  - or the exact runtime error and reproduction path

## Code Quality

- Write for readability first: clear names, small focused functions, and straightforward
  control flow over cleverness.
- Prefer composition and separation of concerns; avoid large multi-responsibility
  functions/classes.
- Keep methods short; extract helpers when branching/nesting grows.
- Follow SOLID where practical, especially Single Responsibility and Dependency
  Inversion at service boundaries.
- Use Pythonic patterns and standard library idioms when they improve clarity.
- Avoid duplication; factor repeated logic into shared utilities with clear interfaces.
- Add type hints for public functions and non-trivial internal APIs.
- Raise specific exceptions with actionable messages; avoid broad `except` unless
  re-raising with context.
- Minimize side effects; keep pure logic separate from I/O, ORM writes, and network
  calls.
- Preserve existing behavior unless explicitly requested to change it; when behavior
  changes, add or update tests.
- Keep comments concise and intent-focused; avoid comments that restate obvious code.
- Prefer incremental, testable changes over broad rewrites.
- Do not create or edit Django migration files manually; generate them using
  `makemigrations`.
- Always place classes in their proper module files (for example, permission classes in
  `permissions.py`), not inline in unrelated files.

## Code Review Guidelines

When the user asks for "do a review", perform a pragmatic code review focused on
clarity, correctness, and maintainability rather than stylistic preferences.

The review should prioritize the following principles:

### 1. Explicit behavior over hidden magic

Flag code where behavior is hidden in:

- framework hooks
- signals
- implicit side effects
- overly clever abstractions

Prefer code where execution flow is easy to follow.

### 2. Clear separation of responsibilities

Check that:

- models handle persistence
- serializers handle data structure / validation
- services contain business logic
- views orchestrate requests

Flag business logic placed in serializers, model `save()`, signals, or views.

### 3. Readability over abstraction

Prefer simple and explicit code over generic or highly abstract solutions.

Flag:

- unnecessary indirection
- over-engineered patterns
- abstractions that obscure behavior.

### 4. Traceable data flow

Ensure it is easy to understand:

- where data enters the system
- how it is transformed
- what side effects occur.

Flag hidden mutations or unclear state changes.

### 5. Database behavior should remain understandable

Highlight:

- inefficient queries
- N+1 problems
- unnecessary queries
- ORM usage that hides what SQL will execute.

### 6. Naming clarity

Names should describe intent clearly.
Flag vague names such as:

- `process`
- `handle`
- `do_stuff`
- `data`

Prefer descriptive function and variable names.

### 7. Avoid premature abstraction

Flag code that introduces unnecessary generalization or frameworks before
they are needed.

Prefer concrete implementations first.

### 8. Deterministic behavior

Code should behave predictably and be easy to mentally simulate.
Flag implicit state changes or unclear execution order.

---

### Review output format

Structure the review as:

1. **Critical issues** (bugs, correctness, security, performance)
2. **Architectural concerns**
3. **Readability / maintainability issues**
4. **Minor suggestions**

For each issue:

- explain *why* it is problematic
- propose a concrete improvement when possible

Avoid purely stylistic comments unless they impact readability.
Do not propose architectural rewrites unless a clear problem exists.
Prefer minimal changes that improve the current design.
