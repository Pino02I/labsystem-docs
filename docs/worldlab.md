# WorldLAB

WorldLAB does for **HDRI / world environments** what LightLAB does for
lights: it lets each camera have its own world override. When the camera
becomes active, WorldLAB swaps `Scene.world` to the camera's assigned
world — automatically, with no manual switching.

This is useful whenever a multi-camera scene needs different lighting
moods or different reflection environments per shot.

## How it works

Every Blender world is a normal `bpy.data.worlds[…]` data block. WorldLAB
adds two layers of state on top:

* **Camera enable flag** — on `Object.lab_worldlab` — whether WorldLAB manages this camera.
* **Camera-to-world association** — managed via `worldlab.toggle_world_assignment` and stored as a per-camera property.

When you switch cameras, WorldLAB checks whether the new camera has a
managed world assignment; if so, it activates that world for the scene.

## Sidebar layout

The WorldLAB sidebar group contains:

* **WorldLAB** (header) — module info and enable status.
* **World Management** — every Blender world listed with CRUD actions.
* **Camera World Assignment** — per-camera world assignment list.

## World Management

The **World Management** sub-panel lists every world that exists in the
file. Each row has:

| Button             | Operator                                  |
|--------------------|-------------------------------------------|
| Set Active         | `worldlab.set_active_world`               |
| Duplicate          | `worldlab.duplicate_world`                |
| Rename             | `worldlab.rename_world`                   |
| Delete             | `worldlab.delete_world`                   |

Below the list:

* **Create World** — `worldlab.create_world` — creates a new empty world.
* **Import HDRI** — `worldlab.import_hdri` — opens a file picker for `.hdr` / `.exr` images and creates a new world with that HDRI plugged into the **Background** node.

The list is collapsible via `worldlab.toggle_world_dropdown`.

## Camera World Assignment

The **Camera World Assignment** sub-panel lists every scene camera. Each
camera row has:

* **Toggle Camera WorldLAB** — `worldlab.toggle_camera_worldlab` — turns per-camera world override on or off for this camera.
* **Toggle Camera Dropdown** — `worldlab.toggle_camera_dropdown` — expands the camera row.
* **Toggle Camera Worlds List** — `worldlab.toggle_camera_worlds_list` — shows the world assignment list for this specific camera.

Inside an expanded camera row:

* The list of every world with an assignment toggle (`worldlab.toggle_world_assignment`).
* **Assign All** — `worldlab.assign_all_to_camera`.
* **Clear Camera World** — `worldlab.clear_camera_world`.

To reset a camera's world override entirely:

* **Reset Camera Overrides** — `worldlab.reset_camera_overrides`.

## Import / Export

* **Export World** — `worldlab.export_world` — writes the current world's full node-graph to a JSON file for transfer.
* **Import World From JSON** — `worldlab.import_world_from_json` — reconstructs a world from a previously-exported JSON.

## Operator reference (alphabetical)

| `bl_idname`                                  | Label                              |
|----------------------------------------------|------------------------------------|
| `worldlab.assign_all_to_camera`              | Assign All Worlds To Camera        |
| `worldlab.clear_camera_world`                | Clear Camera World                 |
| `worldlab.create_world`                      | Create World                       |
| `worldlab.delete_world`                      | Delete World                       |
| `worldlab.duplicate_world`                   | Duplicate World                    |
| `worldlab.export_world`                      | Export World                       |
| `worldlab.import_hdri`                       | Import HDRI                        |
| `worldlab.import_world_from_json`            | Import World From JSON             |
| `worldlab.rename_world`                      | Rename World                       |
| `worldlab.reset_camera_overrides`            | Reset Camera Overrides             |
| `worldlab.set_active_world`                  | Set Active World                   |
| `worldlab.toggle_camera_dropdown`            | Toggle Camera Dropdown             |
| `worldlab.toggle_camera_worldlab`            | Toggle Camera WorldLAB             |
| `worldlab.toggle_camera_worlds_list`         | Toggle Camera Worlds List          |
| `worldlab.toggle_world_assignment`           | Toggle World Assignment            |
| `worldlab.toggle_world_dropdown`             | Toggle World Dropdown              |

## Stored properties

`Object.lab_worldlab` (camera objects):

| Property            | Type | Meaning                              |
|---------------------|------|--------------------------------------|
| `worlds_expanded`   | bool | Per-camera world list expanded       |

`Scene.lab_worldlab_ui`:

| Property        | Type | Meaning                              |
|-----------------|------|--------------------------------------|
| `show_worlds`   | bool | World list expanded                  |
| `show_cameras`  | bool | Camera list expanded                 |
