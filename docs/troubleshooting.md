# Troubleshooting

| Symptom | Checks | Safe next step |
| --- | --- | --- |
| Missing footage | Relative paths, filename changes, case, drive mapping | Relink to an approved media root; record the change |
| Expression error | Missing layer/control, renamed property, unsupported API | Restore the contract or use a documented fallback |
| Color differs | Input interpretation, working space, output transform, player | Compare labeled test renders in an agreed viewer |
| Audio drifts | Sample rate, frame rate, time remap, start time | Reconfirm source timecode and render a short sync test |
| Slow render | Heavy effects, 3D, cache, proxies, frame range | Profile a short range; never change quality silently |
| Template control missing | Essential property exposure, host version, unsupported type | Re-export after testing the target host |
| Text reflows | Font availability, paragraph box, locale, line length | Package approved font information or define a fallback |

Always preserve the original before destructive repair. Record symptoms, environment, attempted fix, and outcome in handoff notes.

