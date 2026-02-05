# LABsystem Documentation

User-focused documentation for LABsystem - Professional Camera & Render Ecosystem for Blender.

## Documentation Structure

This documentation is designed for **users**, not developers. It focuses on **what buttons do**, not how they work internally.

### Contents

- **Installation** - Quick setup guide
- **Interface** - Three ways to access LABsystem
- **Module Reference** - What each command does:
  - CameraLAB - Camera management and resolution presets
  - RenderLAB - Smart rendering with backups
  - LightLAB - Centralized lighting control
  - FrameLAB - Frame range presets
- **Tips & Workflows** - Practical usage examples
- **Troubleshooting** - Solutions to common issues

## Building Locally

```bash
pip install -r requirements.txt
cd docs
make html
```

Output will be in `_build/html/`

## Read the Docs

This documentation is designed for Read the Docs hosting.

Upload the entire repository to Read the Docs and it will automatically build.

## Philosophy

- **User-oriented**: Written for artists, not programmers
- **Action-focused**: Explains what buttons do, not technical details
- **Concise**: No unnecessary explanations
- **Practical**: Real workflows and examples
