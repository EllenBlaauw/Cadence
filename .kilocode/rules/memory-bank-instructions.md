# Project Instructions

## 🔄 Project Awareness & Context

- **At the very beginning of each new conversation or interaction**, always read `PROJECT.md` to understand the context of the project, the project's goals, constraints, architecture, etc.
- **At the very beginning of each new conversation or interaction**, always read `PLANNING.md` to understand the plan how to implement the project in, milestones, risks and resources.
- **Check `TASK.md` before starting a new task.** If the task isn’t explicitly listed, **it must be added** to `TASK.md` with a brief description and the current date before beginning work on it.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`. If `PLANNING.md` doesn't specify a convention for a particular element, follow widely accepted best practices for JavaScript/HTML/CSS, etc.
- Before implementing a complex feature or making significant changes, perform a quick mental check (or internal 'thought' process if applicable) to identify potential conflicts with existing architecture or known limitations. If potential issues are identified, raise them for clarification before proceeding.

## 🧱 Code Structure & Modularity

- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Use clear, consistent imports.** Prefer relative imports for modules within the same logical package/feature group, and absolute paths (if defined for the project) for top-level libraries or shared utilities.
- When refactoring by splitting a file into modules or helper files, include a brief inline comment in the original file (or a README for the new module) explaining the rationale for the split (e.g., `# Reason: Refactored for better separation of concerns: handling X functionality`).

## ✅ Task Completion

- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.
- If the “Discovered During Work” section does not exist yet create it at the bottom of the `TASK.md` file

## 📎 Style & Conventions

- (Consider adding specific formatting rules here if not in `PLANNING.md`, e.g., indentation, brace style)

## 📚 Documentation & Explainability

- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified. When documenting new features, include brief examples of their usage if applicable.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what. Apply this principle not only to complex logic but also to design choices, significant API usage, or non-obvious function parameters.
- **Document the project incrementally as work progresses**, rather than as a final step.

## 🧠 AI Behavior Rules

- If any instruction is ambiguous, incomplete, or contradicts a previous rule or project document, **immediately ask for clarification** before proceeding.
- **Never hallucinate libraries or functions** – only use known, verified JavaScript libraries.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code without explicit user confirmation, even if it appears to be part of a `TASK.md` item.** Always present the proposed changes for review first.

## 💻 Development Environment

- **Operating System:** Windows 11 (64-bit)
