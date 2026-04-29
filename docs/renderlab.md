# RenderLAB

RenderLAB controls **what gets rendered** for any given camera. It does
two things at once:

* Provides four render commands — viewport image, viewport animation,
  selection image, selection animation — each wired to a hotkey and to
  the LABwindow / LABmenu / sidebar.
* Hosts a **per-camera object assignment** system so different cameras
  can render different subsets of the scene without you toggling
  `hide_render` flags by hand.

Both features can be used independently. You can use just the four render
operators without ever touching object assignments — RenderLAB simply
becomes a more ergonomic render shortcut. Or you can lean into the
assignment system and have each camera own its render set.

## Sidebar layout

The RenderLAB sidebar group contains:

* **RenderLAB** (header) — quick render buttons and global toggles.
* **Render Viewport** — viewport image / animation buttons.
* **Render Selection** — selection-only image / animation buttons, with optional include-lights toggle.
* **Viewport Visibility (Eye Icon)** — bulk-toggle eye-icon controls (no hide_render involved).
* **Camera Objects** — per-camera object-assignment list.

A second copy of the RenderLAB header also appears in **Properties → Render
Properties** as a convenience for users who configure renders from there.

## The four render commands

Each render command is exposed in three places: the sidebar, the LABwindow,
and the LABmenu pie. They share the same default hotkeys.

| Command                  | Operator                              | Default hotkey         |
|--------------------------|---------------------------------------|------------------------|
| Render Viewport (image)  | `renderlab.viewport_render`           | `Alt+F12`              |
| Render Viewport Animation| `renderlab.viewport_animation`        | `Alt+Ctrl+F12`         |
| Render Selection         | `renderlab.selection_render`          | `Alt+Shift+F12`        |
| Render Selection Animation | `renderlab.selection_animation`     | `Alt+Ctrl+Shift+F12`   |

Behind the scenes, RenderLAB:

1. Snapshots the current `hide_render` state of every relevant object.
2. Applies its filtering — for selection renders, it hides everything except
   the current selection (and lights, if **Include Lights** is on).
3. Triggers the standard Blender render.
4. **Auto-restores** the original visibility state when the render completes —
   even if it errors out.

If you ever need to manually restore visibility (e.g. you cancelled the
render with the system console closed), use:

* **Manual Restore** — `renderlab.manual_restore` — re-applies the saved snapshot.

## Selection rendering — Include Lights

The **Include Lights** toggle (`renderlab.toggle_include_lights`, exposed
on `Scene.lab_renderlab_ui.include_lights`) decides whether selection
renders also force every scene light to be visible regardless of selection.

* **On** — selection renders always include all lights even if they're not selected.
* **Off** — only selected lights render.

The default is **On**, which is what most users want — it's rare to render
geometry without its lighting.

## Viewport / Render visibility shortcuts

Two banks of bulk operators handle eye-icon (viewport) and camera-icon
(render) visibility separately. They live in **Render Selection** and
**Viewport Visibility** sub-panels.

### Render visibility (camera icon)

| Button                  | Operator                              |
|-------------------------|---------------------------------------|
| Toggle All Render       | `renderlab.toggle_all_render`         |
| Toggle Selected Render  | `renderlab.toggle_selected_render`    |
| Hide Unselected Render  | `renderlab.hide_unselected_render`    |

These flip the `hide_render` flag on mesh / curve / surface / metaball /
font / hair / point cloud / volume / light objects.

### Viewport visibility (eye icon)

| Button                  | Operator                              |
|-------------------------|---------------------------------------|
| Toggle All Viewport     | `renderlab.toggle_all_viewport`       |
| Toggle Selected Viewport| `renderlab.toggle_selected_viewport`  |
| Hide Unselected Viewport| `renderlab.hide_unselected_viewport`  |

These flip the per-object viewport `hide_get()` / `hide_set()` (the eye
icon in the outliner).

### Lights — render and viewport variants

The same six operators exist for lights specifically:

| Action                  | Render variant                                | Viewport variant                                  |
|-------------------------|-----------------------------------------------|---------------------------------------------------|
| Toggle all              | `renderlab.lights_toggle_all`                 | `renderlab.lights_toggle_all_viewport`            |
| Toggle selected         | `renderlab.lights_toggle_selected`            | `renderlab.lights_toggle_selected_viewport`       |
| Hide unselected         | `renderlab.lights_hide_unselected`            | `renderlab.lights_hide_unselected_viewport`       |
| Single light            | `renderlab.toggle_single_light` (`light_name`)| `renderlab.toggle_light_viewport` (`light_name`)  |

The lights list itself is collapsible:

* **Toggle Lights Dropdown** — `renderlab.toggle_lights_dropdown`.

## Camera Objects — per-camera assignment

The **Camera Objects** sub-panel is RenderLAB's signature feature: every
camera gets its own list of "objects this camera renders".

When a camera with object assignments is the active scene camera and a
RenderLAB render is fired, only the assigned objects render — every other
mesh / curve / etc. is automatically hidden, then restored.

Per-camera controls in the list:

* **Toggle Camera Obj Enabled** — `renderlab.toggle_camera_obj_enabled` — turns object-assignment management on or off for this camera.
* **Toggle Camera Obj List** / **Toggle Camera Obj Dropdown** — `renderlab.toggle_camera_obj_list` / `renderlab.toggle_camera_obj_dropdown` — expand or collapse the per-camera list.
* **Assign All To Camera** — `renderlab.assign_all_to_camera` — assigns every renderable object to the camera.
* **Clear Camera Obj Assignments** — `renderlab.clear_camera_obj_assignments` — empties the list.
* **Toggle Selected To Camera** — `renderlab.toggle_selected_to_camera` — assigns the currently-selected objects, or unassigns them if already assigned.
* **Toggle Obj Assignment** — `renderlab.toggle_obj_assignment` — single-object toggle (used by per-row buttons).

The **Type Filter** above the list (`Scene.renderlab_obj_type_filter`)
lets you narrow the list to: All / Mesh / Curve / Metaball / Text / GP v2 /
GP v3 / Armature / Lattice / Empty / Hair Curves / Volume.

The **Search** field (`Scene.renderlab_obj_search`) filters by name.

> **Tip**: combine the per-camera **object** assignment in RenderLAB with
> per-camera **light** assignment in LightLAB to get truly independent
> shots in a shared scene — different objects rendered, different lights
> on, different world environment, all driven by which camera is active.

## Operator reference (alphabetical)

| `bl_idname`                                          | Label                              |
|------------------------------------------------------|------------------------------------|
| `renderlab.assign_all_to_camera`                     | Assign All To Camera               |
| `renderlab.clear_camera_obj_assignments`             | Clear Camera Object Assignments    |
| `renderlab.hide_unselected_render`                   | Hide Unselected from Render        |
| `renderlab.hide_unselected_viewport`                 | Hide Unselected Viewport           |
| `renderlab.lights_hide_unselected`                   | Hide Unselected Lights (Render)    |
| `renderlab.lights_hide_unselected_viewport`          | Hide Unselected Lights (Viewport)  |
| `renderlab.lights_toggle_all`                        | Toggle All Lights (Render)         |
| `renderlab.lights_toggle_all_viewport`               | Toggle All Lights (Viewport)       |
| `renderlab.lights_toggle_selected`                   | Toggle Selected Lights (Render)    |
| `renderlab.lights_toggle_selected_viewport`          | Toggle Selected Lights (Viewport)  |
| `renderlab.manual_restore`                           | Manual Restore Visibility          |
| `renderlab.selection_animation`                      | Render Selection Animation         |
| `renderlab.selection_render`                         | Render Selection                   |
| `renderlab.toggle_all_render`                        | Toggle All Render Visibility       |
| `renderlab.toggle_all_viewport`                      | Toggle All Viewport                |
| `renderlab.toggle_camera_obj_dropdown`               | Toggle Camera Obj Dropdown         |
| `renderlab.toggle_camera_obj_enabled`                | Toggle Camera Obj Enabled          |
| `renderlab.toggle_camera_obj_list`                   | Toggle Camera Obj List             |
| `renderlab.toggle_include_lights`                    | Toggle Include Lights              |
| `renderlab.toggle_light_viewport`                    | Toggle Light Viewport              |
| `renderlab.toggle_lights_dropdown`                   | Toggle Lights Dropdown             |
| `renderlab.toggle_obj_assignment`                    | Toggle Object Assignment           |
| `renderlab.toggle_selected_render`                   | Toggle Selected Render Visibility  |
| `renderlab.toggle_selected_to_camera`                | Toggle Selected To Camera          |
| `renderlab.toggle_selected_viewport`                 | Toggle Selected Viewport           |
| `renderlab.toggle_single_light`                      | Toggle Single Light (Render)       |
| `renderlab.viewport_animation`                       | Render Viewport Animation          |
| `renderlab.viewport_render`                          | Render Viewport                    |

## Stored properties

`Object.lab_renderlab` (any renderable object):

| Property        | Type | Meaning                              |
|-----------------|------|--------------------------------------|
| `user_disabled` | bool | Explicitly excluded from RenderLAB toggles |

`Object.lab_renderlab_camera` (camera objects):

| Property            | Type      | Meaning                                  |
|---------------------|-----------|------------------------------------------|
| `obj_enabled`       | bool      | Object-assignment management is on       |
| `obj_list_expanded` | bool      | Per-camera object list is expanded       |
| `obj_assigned`      | name list | Names of objects assigned to this camera |

`Scene.lab_renderlab_ui`:

| Property              | Type | Meaning                              |
|-----------------------|------|--------------------------------------|
| `camera_obj_dropdown` | bool | Camera-to-object dropdown expanded   |
| `include_lights`      | bool | Include lights in selection render   |
| `lights_dropdown`     | bool | Lights list expanded                 |

`Scene.renderlab_obj_search` and `Scene.renderlab_obj_type_filter` are top-level
scene properties used by the object list filter.
