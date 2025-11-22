# Contributing to LABsystem Documentation

Thank you for your interest in improving LABsystem documentation!

## How to Contribute

### Reporting Issues

If you find errors or have suggestions:

1. Check if the issue already exists
2. Create a new issue with:
   - Clear description
   - Location in documentation
   - Suggested improvement
   - Screenshots if applicable

### Improving Documentation

1. Fork the repository
2. Create a new branch for your changes
3. Make your improvements
4. Test locally (see below)
5. Submit a pull request

## Documentation Structure

- `docs/*.md` - Main documentation files in Markdown
- `docs/index.rst` - Documentation index in reStructuredText
- `docs/conf.py` - Sphinx configuration

## Testing Locally

Before submitting changes, test the documentation:

```bash
cd docs
pip install -r requirements.txt
make html
```

Open `docs/_build/html/index.html` in your browser to review.

## Style Guidelines

### Writing Style

- Use clear, simple language
- Write for non-technical users
- Include examples where possible
- Be concise but complete
- Use active voice

### Formatting

- Use Markdown for content
- One sentence per line (easier to diff)
- Use proper heading hierarchy (# ## ###)
- Include blank lines between sections
- Use code blocks for commands and code

### Screenshots

- Use high-quality images
- Show relevant UI elements only
- Annotate when helpful
- Optimize file size

## What to Contribute

Helpful contributions include:

- Fixing typos and grammar
- Clarifying confusing sections
- Adding missing information
- Creating workflow examples
- Improving organization
- Translating to other languages

## Questions?

If you have questions about contributing, open an issue and ask!

Thank you for helping make LABsystem documentation better!
