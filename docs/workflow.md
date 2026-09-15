# Production workflow

Use this sequence for every shot, master, or motion-graphics package:

1. **Brief:** record deliverables, duration, dimensions, frame rate, audio, color space, language, deadline, and review owner.
2. **Ingest:** copy approved media into a predictable project structure; preserve source names and record licenses.
3. **Build:** create a master composition and precomps with the [naming convention](naming-conventions.md). Keep controls in one documented control layer.
4. **Review:** export a lightweight review movie, note timecode-based feedback, and increment the revision.
5. **Package:** check dependencies, expressions, Essential Graphics controls, and render settings.
6. **Deliver:** render through the [render queue checklist](render-queue.md), verify the output, and complete the [handoff checklist](team-handoff.md).

Keep work-in-progress, review, and approved outputs separate. Never treat a rendered movie as the only source of truth.

## Suggested project folders

```text
PROJECT/
  00_ADMIN/          brief, approvals, license notes
  01_FOOTAGE/        camera, plates, client-supplied media
  02_AUDIO/          dialogue, music, effects
  03_DESIGN/         vector and still source
  04_AE/             project files and autosaves
  05_RENDERS/        review and delivery outputs
  06_HANDOFF/        manifests, reports, final package
```

