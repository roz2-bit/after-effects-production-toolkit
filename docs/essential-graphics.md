# Essential Graphics

Use the Essential Graphics panel to expose a small, purposeful contract to editors.

## Build a resilient template

1. Set the master composition and a descriptive template name.
2. Expose only controls an editor must change: text, colors, media placeholders, and bounded numeric controls.
3. Order controls by editorial workflow, not by layer order.
4. Rename controls in plain language and include units, for example `Headline - text` or `Accent color`.
5. Define font, line-break, duration, and media-replacement behavior.
6. Test the exported template in the target host and record host/version compatibility.

## Acceptance checklist

- [ ] No private client names, absolute paths, or machine-specific fonts are required.
- [ ] Text resizing and line breaks work at minimum and maximum content lengths.
- [ ] Essential properties retain sensible defaults after replacement.
- [ ] Media placeholders have the intended frame rate, color, and crop behavior.
- [ ] A reviewer can identify every control without opening the timeline.

See the [template manifest](../templates/mogrt-manifest.json) for a neutral metadata shape. It is not an Adobe binary.

