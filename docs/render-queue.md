# Render queue

## Before queuing

- [ ] Use the approved comp and revision.
- [ ] Confirm output dimensions, frame rate, pixel aspect, duration, handles, alpha, and audio.
- [ ] Confirm color-management interpretation and output transform.
- [ ] Remove test layers and disable unnecessary proxies.
- [ ] Select an approved codec/container and write it in the manifest.

## Naming and output

Use `PROJECT_DELIVERABLE_REVISION_DATE` and avoid spaces, for example:

```text
ORBIT_SOCIAL_1080X1080_V003_2026-09-15.mp4
ORBIT_MASTER_ALPHA_V003_2026-09-15.mov
```

Render to a clean folder, then verify duration, frame count, audio channels, alpha behavior, and first/last frames. Open the file on a second machine or player when practical. Keep a checksum for final deliveries when the client process requires it.

## Queue notes

Record render-engine choices, GPU/CPU mode, missing fonts, warnings, and start/end time in the handoff notes. Never silently ignore a warning that can change pixels or timing.

