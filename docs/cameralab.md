# CameraLAB

CameraLAB centralises every operation that has to do with cameras as
objects: creating them, navigating between them, remembering their
resolution, controlling depth of field and focal length, and aligning them
to specific scene targets.

## Sidebar layout

Open the sidebar (`N`), choose the **LABsystem** tab, and CameraLAB is the
first module panel. It contains six sub-panels:

* **Collection Cameras** — the list of every scene camera with per-camera actions.
* **Resolution / Camera** — width / height inputs and resolution presets.
* **Viewport & Depth of Field** — perspective / ortho toggle, focal length, DOF.
* **Quick Actions (Align Camera)** — alignment helpers.
* **Import / Export** — JSON export and import of camera settings.

Plus the main header which contains **Create Camera from Viewport** and
**Previous / Next** navigation buttons.

## Camera creation and navigation

### Create Camera from Viewport

Creates a new camera that exactly matches the current 3D viewport view —
position, rotation, focal length. The camera is set as the active scene
camera and stamped with metadata: the scene frame at creation, and the
current scene resolution as its remembered resolution.

* **Operator**: `cameralab.create_camera_from_viewport`
* **Default hotkey**: `Shift+Numpad 0`
* **Sidebar**: top of the CameraLAB panel.

### Set Selected as Active Camera

Promotes the currently selected camera object to be the scene's active
camera (`Scene.camera`).

* **Operator**: `cameralab.set_selected_as_camera` / `cameralab.set_active_from_selected`
* **Default hotkey**: `Shift+Numpad .`

### Cycle Cameras

Cycles forward or backward through every camera in the scene.

* **Operators**: `cameralab.cycle_camera` and `cameralab.cycle_cameras` with property `direction = NEXT | PREVIOUS`
* **Default hotkeys**: `Alt+Numpad 0` (next) and `Alt+Shift+Numpad 0` (previous)

### Walk and Fly Navigation

Enter Blender's walk or fly camera-navigation modal. Useful for fine-tuning
a camera's pose interactively.

* **Operators**: `cameralab.walk_navigation`, `cameralab.fly_navigation`

## Collection Cameras list

The **Collection Cameras** sub-panel lists every camera in the scene
grouped by collection. Each row carries the following per-camera buttons:

| Button             | What it does                                                              | Operator                                |
|--------------------|---------------------------------------------------------------------------|-----------------------------------------|
| ☑ checkbox         | Toggles the camera's selection state for FrameLAB / batch operations      | `cameralab.toggle_camera_check`         |
| Camera icon        | Sets the camera as active                                                 | `cameralab.set_active_camera`           |
| View icon          | Switches the viewport to that camera's view                               | `cameralab.quick_camera_view`           |
| Eye icon           | Toggles viewport visibility of the camera object                          | `cameralab.toggle_camera_visibility`    |
| Lock icon          | Locks / unlocks the camera object's transform                             | `cameralab.toggle_camera_lock`          |
| Rename icon        | Opens a rename dialog for the camera                                      | `cameralab.rename_camera`               |
| Collection icon    | Moves the camera to a different collection                                | `cameralab.collection_switcher` / `cameralab.move_camera_to_collection` |
| Export icon        | Exports the camera settings to a JSON file                                | `cameralab.export_single_camera`        |
| Trash icon         | Deletes the camera                                                        | `cameralab.delete_single_camera`        |

At the bottom of the list:

* **Search** field — `cameralab.camera_search` — filters the list by name.
* **Select All Cameras** — `cameralab.select_all_cameras` — selects every camera in the outliner.
* **Cleanup All Cameras** — `cameralab.cleanup_all_cameras` — removes orphan camera data.
* **Toggle Camera Dropdown** — `cameralab.toggle_camera_dropdown` — collapses or expands the list.

## Resolution

The **Resolution / Camera** sub-panel controls the scene render resolution
and stores per-camera resolution memory.

### Resolution memory

Every CameraLAB-created camera carries its own remembered width and height.
When you switch to a camera (via cycle, the list, or set-active), CameraLAB
applies the camera's stored resolution to the scene automatically — so a
4K cinematic camera and a 1080×1920 social-media camera can sit in the
same scene without you ever editing scene resolution by hand.

To save the current scene resolution onto cameras explicitly:

* **Store Current Resolution** — `cameralab.store_current_resolution` — copies the scene resolution onto the active camera.
* **Store All Resolutions** — `cameralab.store_all_resolutions` — copies the scene resolution onto every camera.
* **Update Scene Resolution** — `cameralab.update_scene_resolution` — applies the active camera's stored resolution to the scene (the same thing CameraLAB does automatically on camera switch).

### Resolution presets

Two operators handle the preset buttons:

* `cameralab.set_resolution_preset_main` — main row presets:
  * **DCI 4K** (4096 × 2160)
  * **4K UHD** (3840 × 2160)
  * **9:16** (1080 × 1920)
  * **1:1** (1080 × 1080)
* `cameralab.set_resolution_preset_extended` — extended row presets:
  * **HD** (1366 × 768) and **Full HD** (1920 × 1080)
  * **QHD** (2560 × 1440) and **DCI 2K** (2048 × 1080)
  * **Cinema Scope** (4096 × 1716), **DCI Flat** (3996 × 2160)
  * **Instagram 4:5** (1080 × 1350), **Square** (1080 × 1080), **Vertical 9:16** (1080 × 1920)
  * **Social HD** / **Presentation** (1280 × 720)
  * **Ultrawide FHD** (2560 × 1080), **Ultrawide QHD** (3440 × 1440), **Premium Ultrawide** (3840 × 1600), **Super Ultrawide** (5120 × 1440)
  * **ARRI 4.6K** (4608 × 3164), **RED 8K** (8192 × 4320)
  * **Widescreen 2.4** (1920 × 800)

The **Toggle More Presets** button (`cameralab.toggle_more_presets`) shows
or hides the extended row.

## Viewport and Depth of Field

The **Viewport & Depth of Field** sub-panel groups every per-camera
optical control.

### Camera type and lens

* Perspective / Orthographic radio.
* Focal length (perspective) or Orthographic scale (ortho) slider.
* **Reset Focal Length** — `cameralab.reset_focal_length` with property `target = CAMERA | ORTHO | VIEWPORT` — resets the value back to defaults (50 mm focal length, 6.0 ortho scale).
* **Toggle Active Camera View** — `cameralab.toggle_active_camera_view` — switches the viewport between camera view and free perspective view.
* **Lock Camera To View** — Blender's built-in toggle, exposed here for convenience.

### Depth of Field

* **Toggle DOF** — `cameralab.toggle_dof` — turns DOF on or off. When turning on, sane defaults are applied if the camera was at zero (focus distance becomes 10 m, F-stop 2.8, blades 6).
* **Focus Object** — pickable from the eyedropper button: `cameralab.focus_object_eyedropper` (uses the selected object).
* **Focus Distance** — eyedropper variant: `cameralab.focus_distance_eyedropper` measures distance from the active camera to the selected object (or active object, or 3D cursor).
* **F-Stop** — direct slider, plus a **Reset F-Stop** button (`cameralab.reset_fstop`) that snaps it back to 2.8.
* **Reset DOF** — `cameralab.reset_dof` — fully restores DOF defaults and clears the focus object.
* **DOF Presets** — `cameralab.apply_dof_preset` with property `preset`. Available presets:
  * **Cinema Shallow** — F/2.0, 6 blades.
  * **Portrait Soft** — F/2.8, 6 blades.
  * **Standard** — F/5.6, 6 blades.
  * **Landscape** — F/11, 6 blades.
  * **Macro Extreme** — F/1.4, 8 blades.

### Aperture shape

A second toggle — **Show Aperture Shape** — exposes blades, rotation, and
ratio for each camera. Stored on the scene property
`cameralab_show_aperture_shape`.

### Camera names in viewport

The **Show Camera Names** toggle (`cameralab_show_camera_names` on the scene)
makes every camera display its name next to its origin in the viewport.

## Quick Actions — alignment

The **Quick Actions** sub-panel groups the alignment helpers.

* **Hero Shot** — `cameralab.hero_shot` — frames the selected object cinematically (corner-of-thirds composition).
* **From Current View** — `cameralab.from_current_view` — re-aligns the active camera to the current viewport view (without creating a new camera).
* **Frame Selected** — `cameralab.frame_selected` — fits the selected object inside the active camera's frustum.
* **Vertigo Align** — `cameralab.rectangle_align` (modal) — drag a rectangle on screen and the camera repositions to produce that vertigo / dolly-zoom effect.
* **Align At Target** — `cameralab.align_at_target` (modal) — interactively place the camera at a specified distance from a target.
* **Refine Position** — `cameralab.refine_current_position` (modal) — fine-tune the active camera's pose with on-screen sliders.

The **Align to Cursor** toggle decides whether alignment operators use the
3D cursor as anchor.

> **Note**: alignment modals support Blender's "Adjust Last Operation" (F6)
> redo panel when fired from the sidebar. When fired from the LABmenu pie
> the redo panel is not available — this is a Blender limitation that
> affects every custom modal pie menu.

## Import / Export

* **Export Camera** — `cameralab.export_camera` — writes the active camera's data (position, rotation, lens, DOF, resolution) to a JSON file.
* **Import Camera** — `cameralab.import_camera` — reads a JSON file and creates a new camera from it.

The exported JSON is human-readable and can be transferred between scenes
or even between Blender versions.

## Operator reference (alphabetical)

Every CameraLAB operator and its `bl_idname`.

| `bl_idname`                                  | Label                              |
|----------------------------------------------|------------------------------------|
| `cameralab.align_at_target`                  | Align At Target                    |
| `cameralab.apply_dof_preset`                 | Apply DOF Preset                   |
| `cameralab.camera_search`                    | Camera Search                      |
| `cameralab.cleanup_all_cameras`              | Cleanup All Cameras                |
| `cameralab.collection_switcher`              | Collection Switcher                |
| `cameralab.create_camera_from_viewport`      | Create Camera from Viewport        |
| `cameralab.cycle_camera` / `cameralab.cycle_cameras` | Cycle Cameras              |
| `cameralab.delete_single_camera`             | Delete Camera                      |
| `cameralab.export_camera`                    | Export Camera                      |
| `cameralab.export_single_camera`             | Export Single Camera               |
| `cameralab.fly_navigation`                   | Fly Navigation                     |
| `cameralab.focus_distance_eyedropper`        | Pick Focus Distance                |
| `cameralab.focus_object_eyedropper`          | Pick Focus Object                  |
| `cameralab.frame_selected`                   | Frame Selected                     |
| `cameralab.from_current_view`                | From Current View                  |
| `cameralab.hero_shot`                        | Hero Shot                          |
| `cameralab.import_camera`                    | Import Camera                      |
| `cameralab.move_camera_to_collection`        | Move Camera to Collection          |
| `cameralab.quick_camera_view`                | Quick Camera View                  |
| `cameralab.rectangle_align`                  | Vertigo Align                      |
| `cameralab.refine_current_position`          | Refine Position                    |
| `cameralab.rename_camera`                    | Rename Camera                      |
| `cameralab.reset_dof`                        | Reset DOF                          |
| `cameralab.reset_focal_length`               | Reset Focal Length                 |
| `cameralab.reset_fstop`                      | Reset F-Stop                       |
| `cameralab.select_all_cameras`               | Select All Cameras                 |
| `cameralab.set_active_camera`                | Set Active Camera                  |
| `cameralab.set_active_from_selected`         | Set Active From Selected           |
| `cameralab.set_resolution_preset_extended`   | Set Resolution Preset (Extended)   |
| `cameralab.set_resolution_preset_main`       | Set Resolution Preset (Main)       |
| `cameralab.set_selected_as_camera`           | Set Selected as Camera             |
| `cameralab.store_all_resolutions`            | Store All Resolutions              |
| `cameralab.store_current_resolution`         | Store Current Resolution           |
| `cameralab.toggle_active_camera_view`        | Toggle Active Camera View          |
| `cameralab.toggle_camera_check`              | Toggle Camera Checkbox             |
| `cameralab.toggle_camera_dropdown`           | Toggle Camera Dropdown             |
| `cameralab.toggle_camera_lock`               | Toggle Camera Lock                 |
| `cameralab.toggle_camera_visibility`         | Toggle Camera Visibility           |
| `cameralab.toggle_dof`                       | Toggle DOF                         |
| `cameralab.toggle_more_presets`              | Toggle More Presets                |
| `cameralab.update_scene_resolution`          | Update Scene Resolution            |
| `cameralab.walk_navigation`                  | Walk Navigation                    |

## Stored properties

CameraLAB stores per-camera state on `Object.lab_cameralab` (a typed
`PropertyGroup`):

| Property              | Type    | Meaning                                              |
|-----------------------|---------|------------------------------------------------------|
| `res_x`, `res_y`      | int     | Remembered resolution for this camera                |
| `preset`              | string  | Preset label (e.g. `"DCI_4K"`)                       |
| `created_frame`       | int     | Scene frame when the camera was created              |
| `creation_type`       | string  | How it was created (`auto_detected`, etc.)           |
| `duplicated_from`     | string  | Source camera if duplicated                          |
| `duplicate_frame`     | int     | Frame when duplication happened                      |
| `checked`             | bool    | List checkbox state                                  |

CameraLAB also stores scene-level UI state on `Scene.lab_cameralab`:

| Property              | Type    | Meaning                                              |
|-----------------------|---------|------------------------------------------------------|
| `show_cameras`        | bool    | Camera list expanded                                 |
| `show_more_presets`   | bool    | Extended preset row expanded                         |

These properties survive save/reload and are migrated automatically when
LABsystem is updated.
