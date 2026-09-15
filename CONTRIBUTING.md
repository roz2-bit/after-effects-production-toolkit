# Contributing

Thanks for improving the After Effects Production Toolkit. Contributions should make a real production decision easier to repeat and should remain usable without proprietary project files.

## Before opening a pull request

1. Read the [Code of Conduct](CODE_OF_CONDUCT.md).
2. Keep examples editable and original; do not add Adobe binaries, client media, fonts, plugin installers, or unlicensed assets.
3. Use ASCII unless a technical term requires otherwise.
4. Keep local Markdown links valid and update the relevant table of contents or repository map.
5. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.

## Documentation style

Use short sections, imperative checklist items, and concrete acceptance criteria. State assumptions about frame rate, color, audio, and host version. Prefer placeholders such as `CLIENT_LOGO_PLACEHOLDER` over copied brand material.

## Pull requests

Explain the production problem, the proposed workflow change, validation performed, and any compatibility impact. One focused change per pull request is preferred. Maintainers may request a small example or checklist update when behavior is ambiguous.

