# FrameLAB

FrameLAB turns the camera collection into a **render queue**. With a single
click you render an image (or animation) from every camera in the scene,
or only the selected ones, with each camera applying its own remembered
resolution / LightLAB / RenderLAB / WorldLAB setup.

This is the natural pairing for the per-camera systems in CameraLAB,
LightLAB, RenderLAB, and WorldLAB. Configure your shots once, then fire
the whole sequence.

## Sidebar layout

The FrameLAB sidebar group contains:

* **FrameLAB** (header) — quick render and animation buttons.
* **Render Sequence** — sequence-render controls (image / animation, all / selected, stop).
* **Output** — output folder, filename format, auto-enable, use-camera-resolution.
* **Camera Management** — per-camera enable/disable and visibility toggles.

## Render Sequence

The four primary commands:

| Button                          | Operator                                       |
|---------------------------------|------------------------------------------------|
| Render All Cameras (Image)      | `framelab.render_all_cameras`                  |
| Render Selected Cameras (Image) | `framelab.render_selected_cameras`             |
| Render Animation All Cameras    | `framelab.render_animation_all_cameras`        |
| Render Animation Selected Cameras | `framelab.render_animation_selected_cameras` |

When you fire one of these:

1. FrameLAB iterates the relevant cameras in scene order.
2. For each camera it sets the camera as active (so per-camera resolution / lights / objects / world all activate).
3. It writes the output to the configured folder using the configured filename pattern.
4. It moves to the next camera and repeats.

A handler-based system keeps the queue moving between renders, so animation
sequences across multiple cameras render with no manual intervention.

To stop in the middle:

* **Stop Sequence** — `framelab.stop_sequence` — cancels the rest of the queue. The currently-rendering camera finishes its current frame.

To open the output folder once you're done:

* **Open Browser** — `framelab.open_browser` — opens the configured output folder in the system file explorer.

## Output settings

The **Output** sub-panel controls where renders go and how they're named:

* **Output Folder** — base folder for sequence renders. Each camera's output is placed under this folder.
* **Filename Format** — token-based filename (camera name, frame number, scene name, etc.).
* **Auto-Enable New Cameras** — preference (`Auto-Enable New Cameras` in the addon prefs) — newly-added cameras are auto-enabled in the FrameLAB queue.
* **Use Camera Resolution** — preference — when on, FrameLAB uses each camera's stored resolution (CameraLAB resolution memory). When off, it uses the scene resolution.

## Camera Management

The **Camera Management** sub-panel lists every scene camera. Each row
has:

| Button                  | Operator                                  |
|-------------------------|-------------------------------------------|
| Enable / Disable toggle | `framelab.toggle_camera`                  |
| Set Active              | `framelab.set_active_camera`              |
| Visibility (Eye)        | `framelab.toggle_camera_visibility`       |

At the bottom of the list:

* **Enable All Cameras** — `framelab.enable_all_cameras`.
* **Disable All Cameras** — `framelab.disable_all_cameras`.
* **Show All Cameras** — `framelab.show_all_cameras`.
* **Hide All Cameras** — `framelab.hide_all_cameras`.
* **Sync With CameraLAB** — `framelab.sync_with_cameralab` — adopts the *checked* state from CameraLAB's camera list (so cameras you've checked in CameraLAB become enabled here).
* **Toggle Camera Dropdown** — `framelab.toggle_camera_dropdown` — collapses or expands the list.

## Viewport render mode

* **Toggle Viewport Mode** — `framelab.toggle_viewport_mode` — switches between full render and viewport-render mode. In viewport mode, only objects currently visible in the viewport are rendered (similar to RenderLAB's selection render but applied to the entire FrameLAB sequence).

## Operator reference (alphabetical)

| `bl_idname`                                          | Label                              |
|------------------------------------------------------|------------------------------------|
| `framelab.disable_all_cameras`                       | Disable All Cameras                |
| `framelab.enable_all_cameras`                        | Enable All Cameras                 |
| `framelab.hide_all_cameras`                          | Hide All Cameras                   |
| `framelab.open_browser`                              | Open Output Folder                 |
| `framelab.render_all_cameras`                        | Render All Cameras                 |
| `framelab.render_animation_all_cameras`              | Render Animation All Cameras       |
| `framelab.render_animation_selected_cameras`         | Render Animation Selected Cameras  |
| `framelab.render_selected_cameras`                   | Render Selected Cameras            |
| `framelab.set_active_camera`                         | Set Active Camera                  |
| `framelab.show_all_cameras`                          | Show All Cameras                   |
| `framelab.stop_sequence`                             | Stop Sequence                      |
| `framelab.sync_with_cameralab`                       | Sync With CameraLAB                |
| `framelab.toggle_camera`                             | Toggle Camera                      |
| `framelab.toggle_camera_dropdown`                    | Toggle Camera Dropdown             |
| `framelab.toggle_camera_visibility`                  | Toggle Camera Visibility           |
| `framelab.toggle_viewport_mode`                      | Toggle Viewport Mode               |

## Stored properties

`Scene.lab_framelab_ui`:

| Property        | Type | Meaning                              |
|-----------------|------|--------------------------------------|
| `show_cameras`  | bool | Camera list expanded                 |

Per-camera enable / disable state for FrameLAB lives on the camera object
itself via `Object.lab_cameralab.checked` (shared with CameraLAB's
checkbox column — that's what **Sync With CameraLAB** uses).
