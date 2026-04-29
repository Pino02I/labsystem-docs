# Interface Tour

LABsystem exposes its features through three surfaces. They're not
mutually exclusive — every operator is reachable from at least two of them,
so you can pick whichever fits your current task.

## The Sidebar (N panel)

Press `N` in the 3D viewport, then choose the **LABsystem** tab on the right
edge. This is the persistent home of every LABsystem control.

Top to bottom, the sidebar contains:

**LABsystem v1.0.0** — version banner and tagline. Click the small icon to
verify the addon is loaded.

**CameraLAB** — main panel with sub-panels:

* **Collection Cameras** — list of every scene camera with per-camera buttons (set active, view, eye, lock, rename, move to collection, export, delete) plus search.
* **Resolution / Camera** — width × height inputs and a row of preset buttons (DCI, 4K, 9:16, 1:1, plus an expandable list of 15+ extra presets).
* **Viewport & Depth of Field** — perspective/orthographic toggle, focal length / orthographic scale, lock-camera-to-view, full DOF section (focus object, focus distance, F-stop, aperture presets, optional aperture-shape controls).
* **Quick Actions (Align Camera)** — alignment helpers: Hero Shot, From Current View, Vertigo Align, Align At Target, Refine Position, Frame Selected.
* **Import / Export** — JSON export/import for the active camera.

**LightLAB** — main panel with sub-panels:

* **Light Management** — every scene light listed with per-light icons (visibility, render, selectable, disable) plus search and Select All / Cleanup.
* **Camera-Light Management** — per-camera assignment list. Each camera shows its assigned lights and a toggle to enable/disable LightLAB management for that camera.
* **Quick Actions** — Assign All / Clear All / Hide Unselected / Hide Selected, plus power multipliers (×2, ÷2) and color/temperature presets.
* **Light Properties** — power, RGB color, temperature presets for the selected light.

**RenderLAB** — main panel with sub-panels:

* **Render Viewport** — Render Image and Render Animation buttons for the active camera.
* **Render Selection** — Render Image and Render Animation buttons that automatically isolate selected objects.
* **Viewport Visibility (Eye Icon)** — quick toggles for all/selected/hide-unselected.
* **Camera Objects** — per-camera object assignment list (which objects are rendered for each camera).

**FrameLAB** — main panel with sub-panels:

* **Render Sequence** — Render All / Render Selected (image and animation), Stop Sequence, output folder controls.
* **Output** — output path, filename format, auto-enable-new-cameras toggle, use-camera-resolution toggle.
* **Camera Management** — list of cameras with per-camera enable/disable, visibility toggle, and a Sync With CameraLAB button.

**WorldLAB** — main panel with sub-panels:

* **World Management** — every Blender world listed with duplicate / delete / rename / set active actions, plus Import HDRI.
* **Camera World Assignment** — per-camera world assignment list.

**Hotkeys** — read-only summary of currently bound hotkeys, sourced from the
addon preferences. Useful as a reminder.

Each module panel can be enabled or disabled in the addon preferences — if
you turn off LightLAB, the **LightLAB** panel and its sub-panels disappear
from the sidebar entirely.

## LABwindow popup (default `F1`)

A floating 440-pixel-wide tabbed popup that summons the most-used controls
from every module without leaving the viewport.

Five tabs along the top: **CameraLAB | RenderLAB | LightLAB | FrameLAB | WorldLAB**.

Switch with the tab buttons or the ◀ / ▶ arrows. The active camera and
camera count appear at the bottom of the window.

The LABwindow is documented in detail at {doc}`labwindow`. The popup mirrors
the most-used sidebar controls — if a panel is disabled in preferences, its
tab disappears from the popup.

## LABmenu radial pie (default `Ctrl+Alt+Shift+Numpad 0`)

A gesture-driven radial pie menu. The centre shows four sub-pies arranged
on the cardinal directions:

```
              CameraLAB (N)
                  ▲
                  │
LightLAB (W) ◀───────▶ RenderLAB (E)
                  │
                  ▼
              FrameLAB (S)
```

Move the mouse in a direction and click — or release in that direction with
gesture mode — to enter that sub-pie. The sub-pie shows up to 8 directional
operators specific to that module. Click the centre to return to the main
pie. Click outside the pie or press `Esc` to cancel.

Full layout of every direction in every sub-pie is in {doc}`labmenu`.

## How the three surfaces relate

Use the **sidebar** when you're configuring a scene — it's persistent and
shows every control with its full label.

Use the **LABwindow popup** when you want a compact overlay during active
work — it's faster to summon than the sidebar and doesn't take screen space.

Use the **LABmenu pie** when speed matters and you know what you want — it's
gesture-based, so with muscle memory you can fire common operations in well
under a second.

All three surfaces operate on the same scene state, so toggling something
in the LABmenu is reflected in the sidebar and vice versa.
