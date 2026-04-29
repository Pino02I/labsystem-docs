# LABwindow Popup (`F1`)

LABwindow is a tabbed popup that consolidates the most-used controls of
every module into a single 440-pixel-wide floating window. Press `F1` from
anywhere in the 3D viewport to summon it.

The popup never blocks the viewport — it's a transient dialog that closes
as soon as you click outside or press `Esc`. It's designed to be summoned,
clicked once, and dismissed.

## Hotkey

* **Default**: `F1`
* **Configurable** in the addon preferences under **LABwindow Hotkeys**.

You can require any combination of `Ctrl`, `Alt`, and `Shift` with the
chosen key. To go back to the default after experimenting, click the
**Reset LABwindow Hotkeys** button in the preferences.

## Layout

Five tabs sit along the top, separated by `◀` and `▶` arrows:

```
◀  CameraLAB | RenderLAB | LightLAB | FrameLAB | WorldLAB  ▶
```

Click a tab to switch instantly. The arrow buttons cycle through the tabs
in order. The bottom of the window shows the active camera name and a
camera count.

If a module is disabled in preferences, its tab is hidden — the popup only
shows tabs for active modules.

## CameraLAB tab

Compact controls grouped in vertical rows:

* **Controls**: New Camera from View.
* **Camera Properties**: Perspective / Orthographic toggle, Camera View toggle, Lock Camera To View.
* **Navigate**: Previous / Next, Walk, Fly.
* **Resolution / Camera**: Resolution X / Y inputs, main preset buttons.
* **Quick Actions**: From Current View, Frame Selected, Hero Shot, Vertigo Align, Align At Target, Refine Position, Align To Cursor toggle.
* **Properties**: Focal length / orthographic scale, DOF on/off, Focus Object eyedropper, Focus Distance eyedropper, F-stop, Passepartout alpha.
* **Import / Export**: Export Camera, Import Camera.

## RenderLAB tab

* **Viewport Render**: Image (`Alt+F12`), Animation (`Alt+Ctrl+F12`).
* **Selection Render**: Image (`Alt+Shift+F12`), Animation (`Alt+Ctrl+Shift+F12`).
* **Lights** (when scene has lights): Include Lights toggle with current status.
* **Viewport Visibility (Eye Icon)**: Toggle All Viewport, Toggle Selected Viewport, Hide Unselected Viewport, Toggle Light Viewport, Hide Unselected Lights Viewport.
* **Render Visibility**: Toggle All Render, Toggle Selected Render, Hide Unselected Render, mirrored controls for lights.

## LightLAB tab

* **LightLAB Controls**: Toggle Camera LightLAB (active camera).
* **Light Assignment**: Assign All Lights, Clear All Lights, Hide Unselected, Hide Selected.
* **Intensity**: ×2, ÷2, Reset.
* **Color & Temperature**: Temperature presets, RGB color picker, color apply button.
* **Light Management**: Per-light row with eye, render, selectable, disable controls.

## FrameLAB tab

* **Render Sequence**: Render All Cameras (image), Render Animation All.
* **Selected**: Render Selected Cameras, Render Animation Selected.
* **Sequence Control**: Stop Sequence, Open Output Folder.
* **Camera List**: Per-camera enable / disable / visibility row.
* **Settings**: Auto-Enable New Cameras, Use Camera Resolution.

## WorldLAB tab

* **World Management**: World list with set-active / duplicate / delete / rename.
* **Import HDRI**: file picker.
* **Camera World Assignment**: per-camera assignment row.

## Switch operator

Tab switches use a dedicated operator that you can also bind to a hotkey
or call from a script:

* **Switch Module** — `labsystem.switch_module` with property `module_index = 0..4`.

## Walk and fly variants

The CameraLAB tab includes two helper variants of walk / fly that recenter
the navigation on the active camera at start:

* **Walk Centered** — `labsystem.walk_centered`.
* **Fly Centered** — `labsystem.fly_centered`.

These are equivalent to clicking on the camera in the outliner, then
pressing the standard walk / fly key — but as a one-button shortcut.

## Toggle Active Camera View

A convenience operator that lets you switch the viewport between camera
view and free perspective view without leaving the popup:

* **Toggle Active Camera View** — `labsystem.toggle_active_camera_view`.

## Operator reference

| `bl_idname`                                | Action                       |
|--------------------------------------------|------------------------------|
| `labsystem.popup_window`                   | Open the LABwindow popup     |
| `labsystem.switch_module`                  | Switch to a tab by index     |
| `labsystem.walk_centered`                  | Walk mode centered on camera |
| `labsystem.fly_centered`                   | Fly mode centered on camera  |
| `labsystem.toggle_active_camera_view`      | Camera view toggle           |
