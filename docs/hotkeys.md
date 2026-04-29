# Hotkeys Reference

LABsystem registers ten configurable hotkeys plus a read-only on-screen
hotkey panel that summarises them.

All hotkeys can be reconfigured in the addon preferences — see
{doc}`preferences` for the full UI.

## Default hotkeys

### Universal

| Hotkey                         | Action                              |
|--------------------------------|-------------------------------------|
| `F1`                           | Open the LABwindow popup            |
| `Ctrl+Alt+Shift+Numpad 0`      | Open the LABmenu radial pie         |

### CameraLAB

| Hotkey                         | Action                              |
|--------------------------------|-------------------------------------|
| `Shift+Numpad 0`               | Create camera from current viewport |
| `Alt+Numpad 0`                 | Cycle to next camera                |
| `Alt+Shift+Numpad 0`           | Cycle to previous camera            |
| `Shift+Numpad .`               | Set selected object as active camera |

### RenderLAB

| Hotkey                         | Action                              |
|--------------------------------|-------------------------------------|
| `Alt+F12`                      | Render viewport (image)             |
| `Alt+Ctrl+F12`                 | Render viewport (animation)         |
| `Alt+Shift+F12`                | Render selection (image)            |
| `Alt+Ctrl+Shift+F12`           | Render selection (animation)        |

## Customising hotkeys

Each hotkey above is broken into four fields in the preferences:

* **Key** — the keyboard / numpad / function key.
* **Ctrl** — checkbox.
* **Alt** — checkbox.
* **Shift** — checkbox.

Combine them however you like. To restore defaults for a section, the
preferences expose four reset buttons:

* `labsystem.reset_labwindow_hotkeys` — Reset LABwindow Hotkeys
* `labsystem.reset_labmenu_hotkeys` — Reset LABmenu Hotkeys
* `cameralab.reset_hotkeys` — Reset CameraLAB Hotkeys
* `renderlab.reset_hotkeys` — Reset RenderLAB Hotkeys

When a hotkey is changed, the new binding is registered with Blender's
keymap system immediately — no restart needed.

## On-screen hotkey panel

The LABsystem sidebar tab includes a read-only **Hotkeys** panel at the
bottom that lists every hotkey with its currently-bound combination.
This is useful when you've customised hotkeys and want a quick reminder
of where they all sit.

The panel is auto-generated from the addon preferences — it always
reflects current bindings.

## Conflicts

LABsystem hotkeys default to combinations that don't clash with stock
Blender hotkeys (the modifier-heavy `Alt+...+F12` family for renders,
`Shift+...+Numpad 0` for camera operations). If a different addon you
have installed binds the same combination, change one of them in the
preferences.

To check what's bound where in Blender, open
**Edit → Preferences → Keymap** and use the search box.

## Hotkey scope

* `F1` (LABwindow) and `Ctrl+Alt+Shift+Numpad 0` (LABmenu) are bound to the **3D Viewport** keymap. They only fire when the cursor is over a 3D viewport.
* CameraLAB hotkeys are bound to the **3D Viewport** keymap.
* RenderLAB hotkeys are bound to the **3D Viewport** keymap.

This is intentional — it prevents the hotkeys firing while you're typing
in the text editor, the outliner, etc.

## Disabling individual modules disables their hotkeys

If you uncheck **CameraLAB Module** in the preferences, the CameraLAB
hotkeys are unbound automatically. Same for RenderLAB. The universal
hotkeys (`F1`, `Ctrl+Alt+Shift+Numpad 0`) remain active as long as the
addon itself is enabled.
