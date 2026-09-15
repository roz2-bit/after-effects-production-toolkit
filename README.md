# After Effects Production Toolkit

An editable, legal-safe operating system for building, reviewing, rendering, and handing off Adobe After Effects work. This repository contains documentation, checklists, naming conventions, and machine-readable templates - not Adobe project files, fonts, plugins, or other proprietary assets.

## What is included

- A production workflow for compositions, expressions, Essential Graphics, render queues, color, audio, and team handoff.
- Version-agnostic templates in `templates/` and editable examples in `examples/`.
- Practical checklists and troubleshooting guidance in `docs/`.
- A package-free validator that checks required files, local Markdown links, JSON/YAML templates, and example metadata.
- Contribution, conduct, issue, pull request, and CI conventions.

## Quick start

1. Read [the workflow overview](docs/workflow.md) and [naming conventions](docs/naming-conventions.md).
2. Copy a relevant template from `templates/` into a production project or tracker.
3. Follow the checklists for [compositions](docs/compositions.md), [rendering](docs/render-queue.md), and [handoff](docs/team-handoff.md).
4. Run the validator:

   ```text
   python scripts/validate.py
   ```

   Python 3.9 or newer is recommended. The validator uses only the standard library.
5. Review [version compatibility](docs/version-compatibility.md) before sharing a project across machines.

## Repository map

| Path | Purpose |
| --- | --- |
| `docs/` | Production guidance and checklists |
| `templates/` | Editable manifests and review forms |
| `examples/` | Original, text-only examples and placeholders |
| `scripts/validate.py` | Dependency-free repository checks |
| `tests/` | Lightweight tests for the validator |
| `.github/` | CI and contribution templates |

## Scope and legal note

This is an independent workflow toolkit. It does not include Adobe software, Adobe project binaries, third-party plugins, fonts, stock media, or proprietary brand assets. Replace every placeholder with media and licenses approved by your organization. Adobe After Effects and Essential Graphics are trademarks of Adobe; references are descriptive only.

## License

Released under the [MIT License](LICENSE).

