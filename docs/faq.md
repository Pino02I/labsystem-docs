# Frequently Asked Questions

## Compatibility

### Which Blender versions does LABsystem support?

LABsystem v1.0.0 requires **Blender 4.2 or newer**. It uses the
extension manifest format (`blender_manifest.toml`) introduced in 4.2,
and several APIs the addon relies on (typed `PropertyGroup` storage,
`gpu` module, modal pie support) only stabilised at that version.

It works on Windows, macOS, and Linux without any platform-specific
configuration.

### Does LABsystem work with both Cycles and EEVEE?

Yes. Every render operator calls Blender's standard render pipeline, so
the engine in use (Cycles, EEVEE, Workbench, or any third-party engine
that registers with `bpy.ops.render.render`) works identically.

### Does LABsystem work alongside other camera addons?

In general, yes. LABsystem stores its state on dedicated typed
PropertyGroups (`Object.lab_cameralab`, `Scene.lab_cameralab_ui`, etc.)
that don't conflict with any other addon. The four configurable hotkeys
(`Alt+...+F12`) and the camera-creation hotkey (`Shift+Numpad 0`) may
clash with other addons — change one of them in the preferences if
needed.

## Per-camera systems

### How do per-camera lights work? Are my lights duplicated?

No, LightLAB does not duplicate lights. Each Blender light is a single
data block. LightLAB stores per-camera **assignment lists** that say
"camera A uses lights X, Y, Z". When camera A becomes active, every
*other* light in the scene is hidden from render; when you switch to
camera B, that filter is updated to camera B's list. Lights you never
mention in any list are unaffected.

### How does LightLAB / RenderLAB / WorldLAB pick which camera is "the active camera"?

They all read `bpy.context.scene.camera`. That's the camera Blender
itself considers active for rendering. CameraLAB's **Set Active Camera**
buttons (and the cycle / set-from-selected operators) all update this
property.

### What happens if I assign the same light to multiple cameras?

It works exactly as you'd expect — the light stays visible whenever any
of those cameras is active.

### Will my per-camera assignments survive when I save and reload the file?

Yes. All assignments are stored on regular Blender data (typed
PropertyGroups on Object and Scene), so they're saved into the `.blend`
file and persist across sessions and Blender restarts.

### Will my assignments survive an addon update?

Yes. LABsystem has a typed-property migration system that recognises
data from older versions and upgrades it on first load.

## CameraLAB

### Can I disable resolution memory?

The resolution memory only updates when CameraLAB-managed operators
write it. If you set the scene resolution by hand without clicking
**Store Current Resolution**, the camera's stored resolution is not
modified — and CameraLAB only re-applies it when you switch cameras.
If you want a camera to stop applying its stored resolution at all,
clear the values manually via the camera's Object Properties.

### Can I export my camera setup to share with someone else?

Yes. **Import / Export** in the CameraLAB sidebar (or the
`cameralab.export_camera` operator) writes the active camera's data —
position, rotation, lens, DOF, resolution — to a JSON file.
`cameralab.import_camera` reconstructs a camera from the JSON. The same
file format works across Blender versions.

### Why do my F6 "Adjust Last Operation" panels not show after using LABmenu?

This is a Blender architectural limitation, not a bug. Operators fired
from a custom modal pie menu are technically invoked by the modal — not
by the user — so Blender does not attach the F6 redo panel.

If you need the redo panel for an alignment operator (e.g. **Vertigo
Align**, **Refine Position**), fire it from the **CameraLAB sidebar**,
where F6 works as expected.

## RenderLAB

### What's the difference between Render Viewport and Render Selection?

* **Render Viewport** renders whatever the scene currently shows — every
  un-hidden object visible in the viewport, plus any per-camera object
  assignments from RenderLAB's Camera Objects system.
* **Render Selection** automatically hides everything except the
  currently-selected objects (and lights, if **Include Lights** is on),
  renders, and restores visibility.

Use Viewport renders for normal shots; use Selection renders for
isolation passes, AOVs by selection, or quick previews of a specific
object.

### My lights aren't included in selection renders. Why?

The **Include Lights** toggle is probably off. Open the
**RenderLAB → Render Selection** sub-panel and turn it on, or use the
LABmenu pie's **W → Light Enable / Disable** entry.

### What if a render crashes mid-way? Will my hide_render flags be lost?

RenderLAB uses an auto-restore handler that fires both on completion
*and* on cancel. If something goes truly catastrophic (e.g. Blender
crashes), the snapshot is also persisted to scene properties — so on
the next launch you can use **Manual Restore**
(`renderlab.manual_restore`) to recover your visibility state.

## FrameLAB

### What's the order of cameras in a sequence render?

The same order they appear in the camera list — which is Blender's
collection / outliner order. To control it, rename or reorder cameras
in the outliner.

### Can I render only some cameras?

Yes — toggle each camera's Enable / Disable checkbox in the FrameLAB
camera list, then use **Render All Cameras** (which respects the
checkboxes), or select specific cameras and use **Render Selected
Cameras**.

### What output filename pattern does FrameLAB use?

The pattern is configurable in the **Output** sub-panel using standard
tokens (camera name, frame number, scene name). Default is the camera
name plus the frame number, written to the configured output folder.

### How do I stop a long sequence render?

Click **Stop Sequence** (`framelab.stop_sequence`) in the FrameLAB
sidebar. The currently-rendering frame finishes, then the queue stops.

## Customisation

### Can I change the LABwindow hotkey?

Yes — open the addon preferences, find the **LABwindow Hotkeys**
section, and set the key + modifiers you want. Click **Reset LABwindow
Hotkeys** to go back to `F1`.

### Can I add my own operator to the LABmenu pie?

Not via the UI in v1.0.0. Pie configuration is data-driven inside the
addon source (the pie layouts are dictionaries in
`marking_menu/menu.py`), so a Python-savvy user can edit them, but
there's no graphical editor for it. A future version may expose this.

### Can I turn off a module without uninstalling LABsystem?

Yes. Open the addon preferences and uncheck the module's checkbox. Its
sidebar panels and hotkeys disappear immediately. See {doc}`preferences`.

## Performance

### Does LABsystem add overhead while rendering?

Negligible. The auto-restore system saves a list of object names and
their `hide_render` flags before rendering and restores them after.
That's a constant-time operation on the order of microseconds for a
typical scene.

### Does LABsystem slow down my viewport?

No measurable cost. The sidebar panels redraw on demand and the
camera-active-change handler only fires when you actually switch
cameras.

## Pricing, licensing, support

### What licence is LABsystem under?

GPL-3.0-or-later, the same licence as Blender itself. The addon
manifest declares this explicitly.

### Where do I get help?

For installation issues see {doc}`installation`. For bug reports and
common runtime issues see {doc}`troubleshooting`. To ask the developer
directly, email **iulianogiuseppe14@gmail.com**.

When reporting a bug, please include:

* Your Blender version.
* The output of **Print Debug Info** (`labsystem.print_debug_info`) from the addon preferences.
* Steps to reproduce.
