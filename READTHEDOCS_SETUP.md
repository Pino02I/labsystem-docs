# LABsystem - Read the Docs Setup Guide

This guide explains how to set up your LABsystem documentation on Read the Docs.

## What You Have

Your documentation package includes:

- `docs/` - Complete documentation folder
- `.readthedocs.yaml` - Configuration file for Read the Docs
- All markdown files with content
- Sphinx configuration
- Requirements file

## Prerequisites

1. A GitHub account (or GitLab/Bitbucket)
2. A Read the Docs account (free at https://readthedocs.org)
3. Your documentation files

## Step 1: Create Repository

### On GitHub:

1. Go to https://github.com
2. Click "New repository"
3. Name it: `labsystem-docs` (or any name you prefer)
4. Make it public (for free Read the Docs hosting)
5. Don't initialize with README (you already have one)
6. Create repository

## Step 2: Upload Documentation

### Option A: Using GitHub Web Interface

1. Go to your new repository
2. Click "Add file" > "Upload files"
3. Upload the entire `docs/` folder
4. Upload `.readthedocs.yaml` to root
5. Commit changes

### Option B: Using Git Command Line

```bash
# Initialize git in your documentation folder
cd /path/to/your/docs/parent/folder
git init
git add docs/
git add .readthedocs.yaml
git commit -m "Initial documentation"

# Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/labsystem-docs.git
git branch -M main
git push -u origin main
```

## Step 3: Connect to Read the Docs

1. Go to https://readthedocs.org
2. Sign in (or sign up with GitHub)
3. Click "Import a Project"
4. If connected to GitHub, your repository should appear
5. Click the "+" button next to your repository
6. Or manually import:
   - Repository URL: `https://github.com/YOUR_USERNAME/labsystem-docs`
   - Repository type: Git

## Step 4: Configure Project

### Basic Settings:

1. **Project Name**: LABsystem
2. **Language**: English
3. **Programming Language**: Python
4. **Project Homepage**: (your website/github)
5. **Repository URL**: (your GitHub URL)
6. **Default Branch**: main (or master)

### Advanced Settings:

The `.readthedocs.yaml` file handles most configuration, but verify:

1. Go to your project on Read the Docs
2. Click "Admin" > "Advanced Settings"
3. Check:
   - Documentation type: Sphinx
   - Python version: 3.11
   - Requirements file: docs/requirements.txt

## Step 5: Build Documentation

1. Go to "Builds" tab
2. Click "Build Version"
3. Wait for build to complete
4. Check for any errors in build log
5. Once successful, click "View Docs"

## Your Documentation URL

Your documentation will be available at:
```
https://labsystem.readthedocs.io
```

Or:
```
https://YOUR_PROJECT_NAME.readthedocs.io
```

## Updating Documentation

Every time you push changes to your GitHub repository, Read the Docs automatically rebuilds:

1. Edit files locally or on GitHub
2. Commit changes
3. Push to GitHub
4. Read the Docs rebuilds automatically
5. New version appears in ~2-5 minutes

## File Structure Explanation

```
your-repo/
├── .readthedocs.yaml          # Read the Docs configuration
└── docs/                       # Documentation folder
    ├── conf.py                 # Sphinx configuration
    ├── index.rst               # Main page (reStructuredText)
    ├── requirements.txt        # Python dependencies
    ├── Makefile               # Build commands
    ├── README.md              # Docs README
    ├── installation.md        # Installation guide
    ├── quickstart.md          # Quick start
    ├── user_guide.md          # User manual
    ├── documentation.md       # Feature reference
    ├── cameralab.md           # CameraLAB module
    ├── renderlab.md           # RenderLAB module
    ├── lightlab.md            # LightLAB module
    ├── framelab.md            # FrameLAB module
    ├── workflows.md           # Workflow examples
    ├── changelog.md           # Version history
    ├── license.md             # License
    └── support.md             # Support & troubleshooting
```

## Customization

### Change Theme Colors

Edit `docs/conf.py`:

```python
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    # Add custom colors, fonts, etc.
}
```

### Add Logo

1. Add logo image to `docs/_static/` folder
2. Edit `docs/conf.py`:
```python
html_logo = '_static/your_logo.png'
```

### Change Project Info

Edit `docs/conf.py`:
```python
project = 'LABsystem'
copyright = '2025, Giuseppe Iuliano'
author = 'Giuseppe Iuliano'
release = '1.0.0'
```

## Adding New Pages

1. Create new `.md` file in `docs/` folder
2. Add content in Markdown format
3. Add to `docs/index.rst`:

```rst
.. toctree::
   :maxdepth: 2
   
   your_new_page
```

4. Commit and push

## Troubleshooting

### Build Fails

**Check build log:**
1. Go to "Builds" tab
2. Click failed build
3. Read error messages
4. Common issues:
   - Missing files
   - Syntax errors in RST/MD
   - Missing dependencies

**Solutions:**
- Verify all files are committed
- Check file paths in index.rst
- Validate YAML syntax
- Check requirements.txt

### Documentation Not Updating

1. Check if build succeeded
2. Clear browser cache
3. Check correct version is "Active"
4. May take a few minutes to propagate

### 404 Error

1. Verify build completed successfully
2. Check default version is set
3. Clear cache and reload
4. Check URL is correct

### Formatting Issues

- Markdown files need blank lines between sections
- Check heading levels (# ## ###)
- Verify links are correct
- Images need proper paths

## Making Documentation Private

Free tier: Public only

For private documentation:
1. Upgrade to Read the Docs for Business
2. Or self-host Sphinx documentation
3. Or use GitHub Pages with authentication

## Versions and Languages

### Multiple Versions

Read the Docs automatically builds all branches and tags:
- `main` branch → "latest" version
- `v1.0.0` tag → "1.0.0" version
- Set default version in Admin

### Translations

For multilingual documentation:
1. Create translation files
2. Configure in `.readthedocs.yaml`
3. Manage in Read the Docs admin

## Best Practices

1. **Keep it updated**: Update docs with each release
2. **Test locally**: Build locally before pushing
3. **Use semantic versioning**: Tag releases properly
4. **Write clear titles**: Help users navigate
5. **Add examples**: Show, don't just tell
6. **Link between pages**: Create connected documentation
7. **Check builds**: Monitor build status
8. **Fix warnings**: Keep build clean

## Local Testing

Test documentation locally before pushing:

```bash
cd docs
pip install -r requirements.txt
make html
```

Open `docs/_build/html/index.html` in browser.

## Support

- Read the Docs docs: https://docs.readthedocs.io
- Sphinx docs: https://www.sphinx-doc.org
- MyST Parser (Markdown): https://myst-parser.readthedocs.io

## Quick Commands Reference

```bash
# Build documentation locally
cd docs && make html

# Clean build files
cd docs && make clean

# Check for broken links
cd docs && make linkcheck

# Build PDF (if configured)
cd docs && make latexpdf
```

## Next Steps

After setup:
1. Verify all pages display correctly
2. Test all internal links
3. Check navigation works
4. Customize theme if desired
5. Set up custom domain (optional)
6. Add search functionality (automatic)
7. Enable versioning (if needed)

Your LABsystem documentation is now live and accessible to users worldwide!
