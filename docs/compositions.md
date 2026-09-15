# Composition checklist

## Setup

- [ ] Name the comp with `TYPE_SEQUENCE_SHOT_VERSION`, for example `MST_LAUNCH_010_V003`.
- [ ] Set width, height, pixel aspect, duration, frame rate, and start time from the brief.
- [ ] Choose a deliberate working-space policy; document it in the manifest.
- [ ] Keep guides, rulers, and safe margins useful but do not rely on them in the final render.
- [ ] Put global controls in `CTRL_GLOBAL` and label them with units and ranges.

## Structure

- [ ] Use precomps for repeated or independently reviewed units.
- [ ] Keep layers in logical blocks: `CTRL`, `TXT`, `GFX`, `MEDIA`, `FX`, `AUDIO`.
- [ ] Avoid hidden dependencies and unused solids, footage, cameras, and effects.
- [ ] Use shy layers for convenience only; reveal them before handoff.
- [ ] Check motion blur, frame blending, collapse transformations, and 3D switches intentionally.

## Review

- [ ] Confirm the first and last frame, handles, safe areas, and text legibility.
- [ ] Scrub at full resolution and at the intended delivery frame rate.
- [ ] Test disabled, missing, and replaced media where appropriate.
- [ ] Record known limitations in `06_HANDOFF/NOTES.md`.

