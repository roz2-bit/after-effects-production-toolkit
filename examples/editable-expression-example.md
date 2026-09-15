# Editable expression example

This is an original, text-only example for training and review. It is not an Adobe project file. Replace `EDITABLE_PLACEHOLDER` values in your own copy.

## Contract

- Control layer: `CTRL_GLOBAL`
- Control: `Progress` (Slider Control, 0-100; default `EDITABLE_PLACEHOLDER`)
- Property: any numeric property that accepts a percentage-like value
- Fallback: `50` if the control is unavailable

```javascript
var fallback = 50;
var control = fallback;
try {
  control = thisComp.layer("CTRL_GLOBAL").effect("Progress")("Slider");
} catch (error) {
  control = fallback;
}
clamp(control, 0, 100);
```

Test with the control removed, renamed, set below zero, and set above 100.
