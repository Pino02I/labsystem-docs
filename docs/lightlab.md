# LightLAB

LightLAB introduces **per-camera light assignment**. You associate a set of
lights with each camera, and when that camera is active LightLAB enforces
that only the assigned lights are enabled — automatically, without you ever
toggling visibility by hand.

This is the core idea: in a multi-camera scene the camera *is* the
lighting unit. Lights for shot A might be wrong for shot B; LightLAB makes
that explicit and one-click manageable.

## How it works

LightLAB stores two pieces of state per camera:

* **Enabled flag** — whether LightLAB manages this camera's lighting at all.
* **Assigned lights** — a list of names of lights that should be on for this camera.

When a camera becomes active and LightLAB is enabled for it, every scene
light is set to `hide_render = (light not in assigned_lights)`. The
existing visibility state is restored when you switch to a non-managed
camera, so cameras you haven't touched continue to use the standard scene
lighting.

You can enable LightLAB management for an individual camera or skip it
entirely — only the cameras you opt-in are affected.

## Sidebar layout

LightLAB lives below CameraLAB in the LABsystem sidebar tab. It contains:

* **LightLAB** (header) — overview and module enable status.
* **Light Management** — scene-wide light list with per-light controls.
* **Camera-Light Management** — per-camera light assignment.
* **Quick Actions** — bulk operations and intensity helpers.
* **Light Properties** — power / color / temperature for the selected light.

## Light Management

The **Light Management** sub-panel lists every light in the scene as a row
with the following per-light buttons:

| Icon              | Action                                       | Operator                              |
|-------------------|----------------------------------------------|---------------------------------------|
| ☑ checkbox        | Toggles selection state for batch actions    | `lightlab.toggle_light_check`         |
| Eye               | Toggles viewport visibility                  | `lightlab.toggle_light_eye`           |
| Camera-render     | Toggles render visibility                    | `lightlab.toggle_light_render`        |
| Selectable        | Toggles whether the light can be selected    | `lightlab.toggle_light_selectable`    |
| Disable viewport  | Disable the light only in viewport           | `lightlab.toggle_light_disable_viewport` |
| Rename            | Rename the light                             | `lightlab.rename_light`               |
| Collection        | Move the light to a collection               | `lightlab.move_light_to_collection`   |
| Trash             | Delete the light                             | `lightlab.delete_light`               |

At the bottom of the list:

* **Search** — filters by name (uses the same filter property as the camera search).
* **Select All Lights** — `lightlab.select_all_lights`.
* **Cleanup Lights** — `lightlab.cleanup_lights` — removes orphan light data blocks.

## Camera-Light Management

The **Camera-Light Management** sub-panel lists every scene camera. Each
camera row has:

* **Enable LightLAB** toggle — `lightlab.toggle_camera_lightlab` — turns on per-camera management for this camera.
* **Expand** caret — `lightlab.toggle_camera_lights_list` — shows the camera's assigned-lights list inline.

Inside each expanded row:

* The list of lights assigned to that camera, with a per-light unassign toggle (`lightlab.toggle_light_assignment`).
* **Assign All** — `lightlab.assign_all_to_camera`.
* **Clear All** — `lightlab.clear_camera_assignments`.
* **Toggle Selected** — `lightlab.toggle_selected_to_camera` — assigns selected scene lights, or unassigns them if already assigned.

## Quick Actions

Quick Actions targets the **active camera**. These are the same as the
named-camera operations above but always work on whichever camera is
currently active.

| Button             | Operator                                          |
|--------------------|---------------------------------------------------|
| Assign All Lights  | `lightlab.assign_all_to_active_camera`            |
| Clear All Lights   | `lightlab.clear_active_camera_assignments`        |
| Hide Unselected    | `lightlab.toggle_selected_to_active_camera`       |
| Hide Selected      | `lightlab.unassign_selected_from_active_camera`   |
| Select Camera Lights | `lightlab.select_camera_lights`                 |

> **Hide Unselected** assigns the *selected* lights and unassigns the rest
> — i.e. the selected lights become the camera's lighting setup, the
> non-selected ones are removed from the assignment list.
>
> **Hide Selected** does the opposite: it removes only the *selected*
> lights from the camera's assignment list, leaving the rest untouched.

### Intensity multipliers

* **×2** — `lightlab.multiply_strength` (factor 2.0) — doubles the power of all selected lights.
* **÷2** — `lightlab.multiply_strength` (factor 0.5) — halves the power of all selected lights.
* **Apply Intensity Multiplier** — `lightlab.apply_intensity_multiplier` (property `factor`, optional `light_name`) — multiplies the power by an arbitrary factor.
* **Set Intensity Preset** — `lightlab.set_intensity_preset` (property `intensity_value`) — sets the power directly.
* **Reset Strength** — `lightlab.reset_strength` (optional `light_name`) — sets the power to 1000 W.

### Visibility shortcuts

| Button                      | Operator                                  |
|-----------------------------|-------------------------------------------|
| Show All Lights             | `lightlab.show_all_lights_quick`          |
| Hide All Lights             | `lightlab.hide_all_lights_quick`          |
| Show Selected Lights        | `lightlab.show_selected_lights`           |
| Isolate Selected Lights     | `lightlab.isolate_selected_lights`        |

These operate on the standard Blender visibility flags — they don't change
LightLAB's per-camera assignments. Use them for quick scene tweaks
independent of the assignment system.

## Light Properties

The **Light Properties** sub-panel exposes per-light controls for whatever
light is currently selected.

* **Power** — direct slider on the light's data.
* **Color** — RGB picker.
* **Apply Light Color** — `lightlab.apply_light_color` (property `color`, optional `light_name`).
* **Color Temperature** — Kelvin slider.
* **Apply Temperature** — `lightlab.apply_temperature` / `lightlab.apply_temperature_preset` (property `temperature_k` or `preset_name`).
* **Set Temperature Preset** — `lightlab.set_temperature_preset` — quick K-value buttons (Tungsten, Halogen, Daylight, Overcast, etc.).

## Advanced operators

* **Copy Light Settings** — `lightlab.copy_light_settings` (property `source_light_name`) — copies type, power, color, and temperature from one light to all selected lights.
* **Convert Light Type** — `lightlab.convert_light_type` (property `light_type`) — switches a light between POINT / SUN / SPOT / AREA while preserving compatible parameters.
* **Align Light At Target** — `lightlab.align_light_at_target` (modal) — interactively place a light pointing at a target.

## Operator reference (alphabetical)

| `bl_idname`                                              | Label                              |
|----------------------------------------------------------|------------------------------------|
| `lightlab.align_light_at_target`                         | Align Light at Target              |
| `lightlab.apply_intensity_multiplier`                    | Apply Intensity Multiplier         |
| `lightlab.apply_light_color`                             | Apply Light Color                  |
| `lightlab.apply_temperature`                             | Apply Temperature                  |
| `lightlab.apply_temperature_preset`                      | Apply Temperature Preset           |
| `lightlab.assign_all_to_active_camera`                   | Assign All to Active Camera        |
| `lightlab.assign_all_to_camera`                          | Assign All to Camera               |
| `lightlab.cleanup_lights`                                | Cleanup Lights                     |
| `lightlab.clear_active_camera_assignments`               | Clear Active Camera Assignments    |
| `lightlab.clear_camera_assignments`                      | Clear Camera Assignments           |
| `lightlab.convert_light_type`                            | Convert Light Type                 |
| `lightlab.copy_light_settings`                           | Copy Light Settings                |
| `lightlab.delete_light`                                  | Delete Light                       |
| `lightlab.hide_all_lights_quick`                         | Hide All Lights                    |
| `lightlab.isolate_selected_lights`                       | Isolate Selected Lights            |
| `lightlab.move_light_to_collection`                      | Move Light to Collection           |
| `lightlab.multiply_strength`                             | Multiply Strength                  |
| `lightlab.rename_light`                                  | Rename Light                       |
| `lightlab.reset_strength`                                | Reset Strength                     |
| `lightlab.select_all_lights`                             | Select All Lights                  |
| `lightlab.select_camera_lights`                          | Select Camera Lights               |
| `lightlab.set_intensity_preset`                          | Set Intensity Preset               |
| `lightlab.set_temperature_preset`                        | Set Temperature Preset             |
| `lightlab.show_all_lights_quick`                         | Show All Lights                    |
| `lightlab.show_selected_lights`                          | Show Selected Lights               |
| `lightlab.toggle_camera_lights_list`                     | Toggle Camera Lights List          |
| `lightlab.toggle_camera_list_dropdown`                   | Toggle Camera List Dropdown        |
| `lightlab.toggle_camera_lightlab`                        | Toggle Camera LightLAB             |
| `lightlab.toggle_light_assignment`                       | Toggle Light Assignment            |
| `lightlab.toggle_light_check`                            | Toggle Light Checkbox              |
| `lightlab.toggle_light_disable_viewport`                 | Toggle Light Disable Viewport      |
| `lightlab.toggle_light_eye`                              | Toggle Light Eye                   |
| `lightlab.toggle_light_render`                           | Toggle Light Render                |
| `lightlab.toggle_light_selectable`                       | Toggle Light Selectable            |
| `lightlab.toggle_light_viewport`                         | Toggle Light Viewport              |
| `lightlab.toggle_lights_dropdown`                        | Toggle Lights Dropdown             |
| `lightlab.toggle_selected_to_active_camera`              | Hide Unselected (Active Camera)    |
| `lightlab.toggle_selected_to_camera`                     | Toggle Selected to Camera          |
| `lightlab.unassign_selected_from_active_camera`          | Hide Selected (Active Camera)      |

## Stored properties

LightLAB stores state on:

`Object.lab_lightlab` (for light objects):

| Property        | Type | Meaning                              |
|-----------------|------|--------------------------------------|
| `checked`       | bool | UI checkbox state                    |
| `user_disabled` | bool | Explicitly disabled by the user      |

`Object.lab_lightlab_camera` (for camera objects):

| Property         | Type      | Meaning                                  |
|------------------|-----------|------------------------------------------|
| `enabled`        | bool      | LightLAB management is on for this camera |
| `lights_expanded`| bool      | Per-camera lights list is expanded       |
| `assigned_lights`| name list | Names of lights assigned to this camera  |

`Scene.lab_lightlab_ui`:

| Property               | Type | Meaning                              |
|------------------------|------|--------------------------------------|
| `lights_dropdown`      | bool | Light list expanded                  |
| `camera_list_dropdown` | bool | Camera list expanded                 |
