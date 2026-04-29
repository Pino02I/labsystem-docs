# Addon Preferences

Open **Edit → Preferences → Add-ons → LABsystem** and you'll see a panel
with module toggles, hotkey configuration, and debug controls.

## Module enable / disable

The five top-level checkboxes turn each module on or off independently:

| Toggle             | Default | Effect when off                                    |
|--------------------|---------|----------------------------------------------------|
| CameraLAB Module   | On      | CameraLAB sidebar group + CameraLAB hotkeys hidden |
| RenderLAB Module   | On      | RenderLAB sidebar group + RenderLAB hotkeys hidden |
| LightLAB Module    | On      | LightLAB sidebar group hidden                      |
| FrameLAB Module    | On      | FrameLAB sidebar group hidden                      |
| WorldLAB Module    | On      | WorldLAB sidebar group hidden                      |

Disabling a module also hides its tab from the LABwindow popup. Toggling
modules takes effect immediately — no restart needed.

## LABwindow hotkeys

Configure the popup hotkey:

| Field             | Default      | Type                                                |
|-------------------|--------------|-----------------------------------------------------|
| Key               | `F1`         | Any keyboard / function / numpad key                |
| Ctrl              | Off          | Boolean                                             |
| Alt               | Off          | Boolean                                             |
| Shift             | Off          | Boolean                                             |

**Reset LABwindow Hotkeys** — `labsystem.reset_labwindow_hotkeys` — restores `F1`.

## LABmenu hotkeys

Configure the pie hotkey:

| Field             | Default      | Type                                                |
|-------------------|--------------|-----------------------------------------------------|
| Key               | `Numpad 0`   | Any keyboard / function / numpad key                |
| Ctrl              | On           | Boolean                                             |
| Alt               | On           | Boolean                                             |
| Shift             | On           | Boolean                                             |

**Reset LABmenu Hotkeys** — `labsystem.reset_labmenu_hotkeys` — restores `Ctrl+Alt+Shift+Numpad 0`.

## CameraLAB hotkeys

Four bindings, each with key / Ctrl / Alt / Shift fields:

| Action                       | Default              |
|------------------------------|----------------------|
| Create Camera from Viewport  | `Shift+Numpad 0`     |
| Cycle Next Camera            | `Alt+Numpad 0`       |
| Cycle Previous Camera        | `Alt+Shift+Numpad 0` |
| Set Selected as Camera       | `Shift+Numpad .`     |

**Reset CameraLAB Hotkeys** — `cameralab.reset_hotkeys`.

## RenderLAB hotkeys

Four bindings:

| Action                  | Default                |
|-------------------------|------------------------|
| Viewport Render         | `Alt+F12`              |
| Viewport Animation      | `Alt+Ctrl+F12`         |
| Selection Render        | `Alt+Shift+F12`        |
| Selection Animation     | `Alt+Ctrl+Shift+F12`   |

**Reset RenderLAB Hotkeys** — `renderlab.reset_hotkeys`.

## FrameLAB settings

Two persistent settings live in preferences (not per-scene):

| Field                          | Default | Effect                                                    |
|--------------------------------|---------|-----------------------------------------------------------|
| Auto-Enable New Cameras        | On      | New cameras added to the scene auto-join the FrameLAB queue |
| Use Camera Resolution          | On      | FrameLAB applies each camera's CameraLAB-stored resolution before render |

**Reset FrameLAB Settings** — `framelab.reset_settings`.

## Debug & utilities

* **Debug Mode** — `debug_mode` toggle. When on, every LABsystem operator prints diagnostic messages to the system console (Window → Toggle System Console on Windows; the terminal on macOS / Linux).
* **Print Debug Info** — `labsystem.print_debug_info` — operator that prints current addon configuration, registered classes, and Blender version. Useful when reporting a bug.

## Operator reference

| `bl_idname`                              | Action                              |
|------------------------------------------|-------------------------------------|
| `labsystem.reset_labwindow_hotkeys`      | Reset LABwindow Hotkeys             |
| `labsystem.reset_labmenu_hotkeys`        | Reset LABmenu Hotkeys               |
| `cameralab.reset_hotkeys`                | Reset CameraLAB Hotkeys             |
| `renderlab.reset_hotkeys`                | Reset RenderLAB Hotkeys             |
| `framelab.reset_settings`                | Reset FrameLAB Settings             |
| `labsystem.print_debug_info`             | Print Debug Info                    |
