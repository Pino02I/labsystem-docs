# LABmenu Radial Pie (`Ctrl+Alt+Shift+Numpad 0`)

LABmenu is a radial pie menu designed for muscle-memory operation. The
pie has a main wheel with four directional sub-pies (one per module) and
each sub-pie has up to 8 directional operators.

With practice you can fire common operations as gestures — for example,
*"render the active camera"* becomes `<hotkey>` → flick right (RenderLAB)
→ flick up (Viewport Render) and you're rendering, without ever looking at
the menu.

## Summoning the pie

* **Default hotkey**: `Ctrl+Alt+Shift+Numpad 0`
* **Configurable** in the addon preferences under **LABmenu Hotkeys**.

The pie appears at the cursor location. Move the cursor in a direction
and click — or release in that direction with gesture mode — to fire that
direction's action.

* The **centre** of a sub-pie always returns you to the main pie (or
  cancels, when on the main pie).
* Pressing `Esc` or clicking outside the pie cancels.

## Main pie

The main wheel has four directions:

```
                CameraLAB
                    ▲ N
                    │
   LightLAB W ◀──────────▶ E RenderLAB
                    │
                    ▼ S
                FrameLAB
```

| Direction | Sub-pie         |
|-----------|-----------------|
| N         | CameraLAB       |
| E         | RenderLAB       |
| S         | FrameLAB        |
| W         | LightLAB        |
| Centre    | Cancel          |

## CameraLAB sub-pie

| Direction | Label                | Operator                                    |
|-----------|----------------------|---------------------------------------------|
| N         | Create Camera        | `cameralab.create_camera_from_viewport`     |
| NE        | Set Active           | `cameralab.set_active_from_selected`        |
| E         | Next Camera          | `cameralab.cycle_camera` (NEXT)             |
| S         | Align To View        | `view3d.camera_to_view`                     |
| W         | Previous Camera      | `cameralab.cycle_camera` (PREVIOUS)         |
| NW        | Walk Mode            | `labmenu.cameralab_walk_mode`               |
| Centre    | Back                 | (return to main pie)                        |

## RenderLAB sub-pie

| Direction | Label                  | Operator                                  |
|-----------|------------------------|-------------------------------------------|
| N         | Viewport Render        | `renderlab.viewport_render`               |
| E         | Viewport Animation     | `renderlab.viewport_animation`            |
| SE        | Selection Render       | `renderlab.selection_render`              |
| SW        | Selection Animation    | `renderlab.selection_animation`           |
| W         | Light Enable / Disable | `labmenu.toggle_include_lights_status`    |
| Centre    | Back                   | (return to main pie)                      |

The **W** entry has a dynamic label that reflects the current state of
**Include Lights** — `Lights: Enabled` or `Lights: Disabled`.

## LightLAB sub-pie

| Direction | Label                   | Operator                                          |
|-----------|-------------------------|---------------------------------------------------|
| N         | Enable LightLAB         | `labmenu.toggle_camera_lightlab_safe`             |
| NE        | Assign All Lights       | `labmenu.assign_all_lights_refresh`               |
| E         | Clear All Lights        | `labmenu.clear_all_lights_refresh`                |
| SE        | Hide Unselected         | `labmenu.toggle_selected_lights_refresh`          |
| S         | Hide Selected           | `labmenu.unassign_selected_lights_refresh`        |
| SW        | Light Power ×2          | `lightlab.multiply_strength` (factor 2.0)         |
| W         | Light Power ÷2          | `lightlab.multiply_strength` (factor 0.5)         |
| NW        | RGB Color               | `labmenu.light_color_picker`                      |
| Centre    | Back                    | (return to main pie)                              |

The **N** entry has a dynamic label depending on whether LightLAB is
already enabled for the active camera (`Enable LightLAB` /
`Disable LightLAB`).

## FrameLAB sub-pie

| Direction | Label                       | Operator                                       |
|-----------|-----------------------------|------------------------------------------------|
| N         | Render All Cameras          | `framelab.render_all_cameras`                  |
| NE        | Animation All               | `framelab.render_animation_all_cameras`        |
| E         | Render Selected             | `framelab.render_selected_cameras`             |
| SE        | Animation Selected          | `framelab.render_animation_selected_cameras`   |
| S         | Stop Sequence               | `framelab.stop_sequence`                       |
| W         | Viewport Render Mode        | `labmenu.toggle_viewport_render_mode`          |
| Centre    | Back                        | (return to main pie)                           |

The **W** entry has a dynamic label reflecting the current viewport-mode
state.

## Marking-menu specific operators

The LABmenu uses several thin wrapper operators that exist only to be
fired from the pie. They handle UI refreshing and dynamic labels that
don't make sense as standalone sidebar buttons.

| `bl_idname`                                              | Purpose                                      |
|----------------------------------------------------------|----------------------------------------------|
| `labsystem.marking_menu`                                 | The main radial pie modal                    |
| `labmenu.invoke_via_modal`                               | Internal wrapper for redo support            |
| `labmenu.toggle_camera_lightlab_safe`                    | Wrapper for `lightlab.toggle_camera_lightlab` |
| `labmenu.assign_all_lights_refresh`                      | Wrapper for `lightlab.assign_all_to_active_camera` |
| `labmenu.clear_all_lights_refresh`                       | Wrapper for `lightlab.clear_active_camera_assignments` |
| `labmenu.toggle_selected_lights_refresh`                 | Wrapper for `lightlab.toggle_selected_to_active_camera` |
| `labmenu.unassign_selected_lights_refresh`               | Wrapper for `lightlab.unassign_selected_from_active_camera` |
| `labmenu.toggle_include_lights_status`                   | Wrapper for `renderlab.toggle_include_lights` |
| `labmenu.toggle_viewport_render_mode`                    | Wrapper for `framelab.toggle_viewport_mode`  |
| `labmenu.cameralab_align_at_target`                      | Wrapper for `cameralab.align_at_target`      |
| `labmenu.cameralab_walk_mode`                            | Wrapper for `cameralab.walk_navigation`      |
| `labmenu.light_color_picker`                             | Color picker dialog for selected lights      |

## Customising the pie hotkey

Open **Edit → Preferences → Add-ons → LABsystem → LABmenu Hotkeys**. You
can change:

* The trigger key (default `Numpad 0`).
* Whether `Ctrl`, `Alt`, `Shift` are required (defaults: all three).

A **Reset LABmenu Hotkeys** button restores the default. See
{doc}`preferences` for screenshots.

## A note on the F6 redo panel

Blender's "Adjust Last Operation" (F6) panel attaches to the **last
user-invoked operator**. Operators fired from a custom modal pie menu —
such as LABmenu — are technically invoked by the modal itself, not by the
user, so Blender does not attach the redo panel to them.

This is a Blender architectural limitation, not a LABsystem bug. If you
need to interactively tweak parameters of an alignment operator (e.g.
**Vertigo Align**, **Refine Position**), fire it from the **CameraLAB
sidebar** — there F6 works as expected.
