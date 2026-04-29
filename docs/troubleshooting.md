# Troubleshooting

This page covers the most common runtime issues. If you don't find
your answer here, see the {doc}`faq` or contact
**iulianogiuseppe14@gmail.com**.

Before anything else, take three steps to gather diagnostics:

1. Open **Window → Toggle System Console** (Windows) or launch Blender from a terminal (macOS / Linux).
2. Reproduce the issue. Note any red error lines printed to the console.
3. In **Edit → Preferences → Add-ons → LABsystem**, click **Print Debug Info** and copy the output.

That information is what fixes most reports in seconds.

## Installation issues

### The LABsystem sidebar tab doesn't appear after install

* Confirm the addon is enabled in **Edit → Preferences → Get Extensions** (or **Add-ons**).
* Make sure your Blender version is **4.2.0 or newer**.
* Check the system console for a registration error during the install.
* Try restarting Blender — extension hot-reload sometimes leaves stale state.

If the addon imports successfully but the panels don't show, all five
modules might be disabled in preferences. Open the LABsystem preferences
and ensure at least one module is checked.

### Install fails with a manifest error

Make sure you're using the official `LABsystem 1.0.0.zip` package and
not a re-zipped or partial copy. The manifest must be at the root of
the ZIP. If you've extracted and re-zipped the addon, the structure may
have changed.

### "labsystem" is greyed out in the extensions list

This usually means Blender detected the manifest but failed to import
the package. Check the system console — there's almost always a Python
exception printed there. Common causes:

* Trying to install the addon on a Blender version below 4.2.
* A leftover folder from a previous install with the same id. Remove via the extension list and try again.

## Hotkey issues

### F1 doesn't open the LABwindow popup

* The F1 binding is module-aware — it only fires while the cursor is in a 3D Viewport. Move the cursor to the viewport and try again.
* Another addon may have bound F1. Open **Edit → Preferences → Keymap**, search for F1, and look for conflicts.
* Check **LABsystem preferences → LABwindow Hotkeys** — perhaps the key was changed inadvertently. Click **Reset LABwindow Hotkeys**.

### Ctrl+Alt+Shift+Numpad 0 doesn't open the LABmenu

* Make sure your keyboard has a numpad. Many laptop keyboards require a Function-key combination to engage Numpad 0.
* If you're on a laptop without a real numpad, change the binding in **LABsystem preferences → LABmenu Hotkeys** to something else (e.g. `Ctrl+Alt+Shift+Q`).
* The pie hotkey is bound to the 3D Viewport keymap — the cursor must be over a viewport.

### My CameraLAB / RenderLAB hotkey doesn't fire

* The relevant module may be disabled in preferences — re-enable it.
* The hotkey is bound to the 3D Viewport — move the cursor to the viewport.
* Another addon or your custom keymap may be intercepting the same combination. Search **Edit → Preferences → Keymap** for the keys.

### Accidentally bound a hotkey to a key Blender already uses

Click the **Reset** button for the relevant section in the addon
preferences (`Reset CameraLAB Hotkeys`, `Reset RenderLAB Hotkeys`,
etc.).

## CameraLAB

### A camera switched, but the resolution didn't update

CameraLAB only applies the stored resolution when **the camera has
stored resolution data**. If the camera was created outside LABsystem
(for example by Blender's Add menu or by a different addon), it has no
stored data on first switch.

To stamp the current scene resolution onto every camera at once:

* Open **CameraLAB → Resolution / Camera**.
* Click **Store All Resolutions**.

From then on, switching to that camera applies the resolution
correctly.

### "Vertigo Align" or "Refine Position" don't show the F6 redo panel from LABmenu

This is a Blender architectural limitation. Operators fired from a
custom modal pie menu cannot attach the F6 panel because Blender
considers the operator invoked by the modal, not by the user.

Workaround: fire the alignment from the **CameraLAB sidebar** instead —
F6 works there.

### Camera created from viewport is wrong / inverted

The viewport view direction is captured at the moment of camera
creation. If you've just orbited and the operator captured a transient
state, click **Quick Camera View** (in the camera's row in the list) to
align the camera with the viewport again, or recreate the camera.

## LightLAB

### Lights aren't being filtered when I switch cameras

* Make sure LightLAB is **enabled for that camera**. Each camera has its own enable toggle (`lightlab.toggle_camera_lightlab`). If you've never enabled it on this camera, LightLAB won't manage it.
* Check that the camera actually has assigned lights. An empty assignment list means *no* lights are visible — that may not be what you want. Use **Assign All Lights** as a starting point.

### Hide Selected isn't hiding the selected lights

**Hide Selected** removes the currently-selected lights from the active
camera's assignment list — it does *not* hide them in the viewport. To
make a light invisible in the viewport, use the standard Blender eye
icon or `lightlab.toggle_light_eye`.

The naming is consistent with the LABmenu's gesture vocabulary:
**Hide Selected** = "stop showing these in this camera's render".

### My lights have wrong intensity after using ×2 / ÷2

`lightlab.multiply_strength` operates on the **selected** lights — every
selected light's power is multiplied. If unrelated lights were selected
when you clicked, they were affected too. Click **Reset Strength**
(`lightlab.reset_strength`) on each light to restore power to 1000 W.

## RenderLAB

### After a render, some objects are still hidden

The auto-restore should always fire, but if Blender crashes mid-render
the snapshot may not have been written. Open the **RenderLAB** sidebar
and click **Manual Restore** (`renderlab.manual_restore`) — it
re-applies the saved visibility state.

If even Manual Restore doesn't help (the snapshot was lost), the
fastest recovery is **Object → Show Hidden Objects** (`Alt+H`) followed
by re-running RenderLAB on the cameras you actually wanted.

### Selection render renders nothing / is black

* You may not have anything selected. Select at least one object before triggering a selection render.
* The selected objects may be entirely off-camera. Check that they're inside the camera frustum.
* If lights aren't included (the **Include Lights** toggle is off), the scene may have no lighting and produce a near-black image. Turn the toggle on.

### Camera Objects list is empty

The list is populated for the **active camera**. If no camera is active,
the list is empty. Set a camera active via CameraLAB or directly in the
outliner.

You also need to **enable** the per-camera object management for that
camera (`renderlab.toggle_camera_obj_enabled`) — until then, the list is
shown but inactive.

## FrameLAB

### Stop Sequence doesn't seem to do anything

The currently-rendering frame finishes before the queue stops — that's
intentional, otherwise mid-frame cancellation could leave broken output
files. After the current frame, the sequence stops cleanly.

### A FrameLAB animation render skipped some cameras

Check the camera list. Disabled cameras are skipped. If they look
enabled but were skipped:

* The camera may have been hidden in the viewport (`framelab.toggle_camera_visibility`). Hidden cameras are skipped.
* If "Use Camera Resolution" is on and the camera has no stored resolution, FrameLAB falls back to scene resolution but may emit a console warning.

### Output folder doesn't exist

FrameLAB doesn't create the output folder for you — make sure the path
in **Output** is a valid existing folder before launching the sequence.

## WorldLAB

### World doesn't change when I switch cameras

* Confirm WorldLAB management is **enabled** for that camera (the toggle next to its row in **Camera World Assignment**).
* Confirm the camera actually has a world assigned. Without an assignment, the active world remains whatever it was before the camera switch.

### HDRI imported but not visible in render

The HDRI is loaded into a new world. You still need to **assign** that
world to the active camera (or set it as the scene's active world)
before rendering. The world list shows every available world; click
**Set Active** to use it directly.

## General

### "Print Debug Info" — what does it report and where does it go?

It prints to the system console:

* LABsystem version.
* Blender version.
* Each module's enable state.
* Number of registered classes per module.
* Current hotkey bindings.

Use this output when reporting bugs.

### How do I find the system console?

* **Windows**: **Window → Toggle System Console**.
* **macOS**: launch Blender from `Terminal.app` — the console is your terminal window.
* **Linux**: launch Blender from a terminal — same as macOS.

### How do I report a bug?

Email **iulianogiuseppe14@gmail.com** with:

1. Your Blender version.
2. LABsystem version (1.0.0).
3. Output of **Print Debug Info**.
4. Console output containing any red error lines.
5. Steps to reproduce.
