# LABsystem Documentation

Source for the official **LABsystem v1.0.0** documentation, hosted on Read the Docs.

LABsystem is a professional camera and render ecosystem for Blender 4.2+ composed of five
modular sub-systems: **CameraLAB**, **LightLAB**, **RenderLAB**, **FrameLAB**, **WorldLAB**.

## Building locally

```bash
cd docs
pip install -r requirements.txt
make html
```

The rendered site appears in `docs/_build/html/index.html`.

## Read the Docs

The site is configured via `.readthedocs.yaml` at the repository root.
Build target is `docs/conf.py`. The theme is `sphinx_rtd_theme` and Markdown
files are parsed by `myst-parser`.

## License

LABsystem is released under GPL-3.0-or-later. See `LICENSE` in the addon
distribution.

---

Maintained by **Pino Iulio** — `iulianogiuseppe14@gmail.com`
