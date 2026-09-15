# Version compatibility

After Effects projects and templates can change behavior across releases, operating systems, render engines, fonts, codecs, and plugins.

## Compatibility record

Record host version, OS, renderer, third-party plugins, fonts, scripting assumptions, and color-management settings in the manifest. Use the earliest supported version as the test target when a team shares work.

## Before sharing

- [ ] Save a revision and keep an untouched fallback.
- [ ] Open and inspect the project on the recipient's target version.
- [ ] Identify unsupported effects, expressions, fonts, and media codecs.
- [ ] Test an Essential Graphics export/import if applicable.
- [ ] Provide a flattened review render for visual comparison.

If a downgrade or cross-version save is unavailable, do not promise editability. Deliver the native source plus a render, manifest, and a clear limitation note.

