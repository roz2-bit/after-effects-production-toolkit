# Expressions

Expressions are small programs attached to properties. Treat them as production code: readable, deterministic, and safe when a control is missing.

## Rules

- Prefer named controls on a documented control layer over hard-coded magic numbers.
- Keep expressions short; move complex logic to a reviewed helper pattern.
- Guard optional layers and properties, and provide a sensible fallback.
- Avoid time-dependent randomness unless a fixed seed and review expectation are documented.
- Note required APIs and host-version assumptions in the handoff manifest.
- Disable or bake expressions when the recipient cannot maintain them.

## Editable example

This expression uses a slider named `Progress` on `CTRL_GLOBAL` and clamps the result. It contains no external file or plugin dependency:

```javascript
var control = thisComp.layer("CTRL_GLOBAL").effect("Progress")("Slider");
linear(clamp(control, 0, 100), 0, 100, 0, 100);
```

Before delivery, test missing controls, duplicate layer names, negative values, and a non-zero composition start time. Store the expression text in a review note when it is business-critical.

