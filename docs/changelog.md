# Changelog

This is the public release history of LABsystem.

## v1.0.0 — Initial public release

LABsystem v1.0.0 is the first stable release of the addon, packaged as
a Blender 4.2+ extension.

### Modules

Five modular sub-systems, each independently enable-able from preferences:

* **CameraLAB** — camera creation, navigation, resolution memory, depth-of-field, alignment helpers, JSON import / export.
* **LightLAB** — per-camera light assignment, intensity multipliers, color and temperature presets.
* **RenderLAB** — viewport / selection image and animation render commands, per-camera object assignment, auto-restore visibility system.
* **FrameLAB** — multi-camera sequence rendering with per-camera enable, stop control, output folder management.
* **WorldLAB** — per-camera HDRI / world environment override, HDRI import, JSON import / export.

### Universal entry points

* **LABwindow popup** (default `F1`) — tabbed compact UI with one tab per module.
* **LABmenu radial pie** (default `Ctrl+Alt+Shift+Numpad 0`) — main pie with four sub-pies (CameraLAB, RenderLAB, LightLAB, FrameLAB), 6–8 directional operators each.

### Sidebar

* Persistent **LABsystem** category in the 3D Viewport Sidebar (`N`) with one panel group per module plus a Hotkeys reference panel.
* All sidebar panels are populated only when their owning module is enabled in preferences.

### Hotkeys

Ten configurable hotkeys (LABwindow, LABmenu, four CameraLAB, four
RenderLAB) plus a read-only on-screen hotkey panel that always reflects
the current bindings.

### Architecture

* Blender 4.2 extension manifest format (`blender_manifest.toml`).
* Typed `PropertyGroup` storage for all per-camera and per-scene state, with automatic migration from earlier internal data shapes.
* Modular auto-split source layout — every module sub-package follows the same pattern (`__init__.py` registers, sub-files contain operator/UI classes).
* Centralised `debug_logger` for diagnostics, controllable via the **Debug Mode** preference.

### Known limitations

* Operators fired from the LABmenu pie cannot show Blender's F6 "Adjust Last Operation" redo panel. This is a Blender architectural limitation — pie-fired operators are considered invoked by the modal, not by the user. Fire alignment operators from the CameraLAB sidebar instead.
* Pie configuration is data-driven inside the source code; there is no graphical editor for the pie layout in v1.0.0. A future release may expose this in preferences.

### Compatibility

* **Blender**: 4.2.0 or newer.
* **Platform**: Windows / macOS / Linux.
* **Render engines**: Cycles, EEVEE, Workbench, third-party engines that integrate with `bpy.ops.render.render`.
* **Permissions**: none required at runtime — no network, no filesystem outside Blender's own scope, no clipboard.

### Author

Maintained by **Pino Iulio** — `iulianogiuseppe14@gmail.com`.

Released under **GPL-3.0-or-later**.
