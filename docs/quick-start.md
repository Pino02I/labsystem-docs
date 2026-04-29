# Quick Start

This page walks you through five short tasks that exercise every module of
LABsystem. Total time: about ten minutes.

## 1. Open the LABsystem sidebar

In the 3D viewport, press `N` and click the **LABsystem** tab. You'll see
panels for each module stacked vertically, ready to use.

You can also press `F1` at any time to open the floating **LABwindow** popup
— it has the same controls reorganised into compact tabs.

## 2. Create your first camera

In the **CameraLAB** panel, click **Create Camera from Viewport** (the camera
icon button at the top).

* The current viewport view becomes a new camera.
* The new camera is set as the active scene camera automatically.
* CameraLAB stores the current scene resolution on this camera as its
  default — it now "remembers" what resolution it was created at.

You can also press the keyboard shortcut `Shift+Numpad 0` to do the same
thing without clicking.

## 3. Try resolution memory

With the new camera active:

1. Open the **Resolution / Camera** panel.
2. Click **DCI 4K**. The scene resolution becomes 4096 × 2160.
3. Click **Store Current Resolution** if it isn't auto-stored. CameraLAB
   saves 4096 × 2160 on this specific camera.

Now create a second camera (`Shift+Numpad 0` or the **Create Camera** button)
and set its resolution to **9:16** (1080 × 1920).

Switch between the two cameras — for example with **Previous Camera** /
**Next Camera** in the CameraLAB panel, or with `Alt+Numpad 0` /
`Alt+Shift+Numpad 0`. Each camera applies its own stored resolution
automatically.

## 4. Per-camera lights with LightLAB

Add a few lights to your scene (e.g. **Add → Light → Area** a few times).

In the **LightLAB** panel:

1. With your first camera active, click **Enable LightLAB** (if not already
   on for this camera). The camera now has a light-assignment list.
2. Select the lights you want this camera to use.
3. Click **Toggle Selected to Active Camera** (or **Assign All Lights**).
   Those lights are now associated with this camera.
4. Switch to the second camera. Notice that none of the lights are assigned
   to it yet — its scene only "sees" the lights you assign through LightLAB.
5. Select a different subset of lights and assign them to camera 2.

Now switch between cameras. The lighting setup follows automatically.

The same pattern can be done quickly from **LABmenu** (default
`Ctrl+Alt+Shift+Numpad 0` → **W** for LightLAB → **Assign All Lights** /
**Hide Selected**).

## 5. Per-camera HDRI with WorldLAB

In the **WorldLAB** panel:

1. Click **Import HDRI** and choose any `.hdr` or `.exr` file. WorldLAB
   creates a new World containing the HDRI.
2. With camera 1 active, click **Toggle Camera WorldLAB** (the world toggle
   icon next to camera 1) so WorldLAB manages the world for this camera.
3. Click the assignment toggle next to your imported HDRI to bind it to
   camera 1.
4. Repeat for camera 2 with a different HDRI.

Switch between cameras — the world environment swaps automatically.

## 6. Render multiple cameras with FrameLAB

In the **FrameLAB** panel:

1. Set an **Output Folder** if you want renders to go somewhere specific.
2. All scene cameras appear in the **Camera Management** list. Toggle the
   ones you want to render — by default all are enabled.
3. Click **Render All Cameras** (image button). FrameLAB renders one image
   per enabled camera, applying each camera's stored resolution and its
   per-camera LightLAB / RenderLAB / WorldLAB setup.
4. Or click **Render Animation All Cameras** to render the full timeline
   for every camera in sequence.

Need to stop mid-sequence? Click **Stop Sequence** in FrameLAB.

## 7. Render only what's selected with RenderLAB

In the **RenderLAB** panel:

1. Select two or three objects in the viewport.
2. Click **Render Selected (Image)**.
3. RenderLAB hides everything else from render automatically, fires a
   render, then restores visibility.

Hotkey: `Alt+Shift+F12` for selection image, `Alt+Ctrl+Shift+F12` for
selection animation.

## 8. Try the LABmenu

Press `Ctrl+Alt+Shift+Numpad 0`. A radial pie appears at the cursor.

* Move up (**N**) → CameraLAB sub-pie.
* Move right (**E**) → RenderLAB sub-pie.
* Move down (**S**) → FrameLAB sub-pie.
* Move left (**W**) → LightLAB sub-pie.

Inside each sub-pie, a second flick of the mouse fires the action. Click
the centre to go back to the main pie. Click outside the pie to cancel.

## You're set

Every other panel and operator is documented in the module pages:
{doc}`cameralab`, {doc}`lightlab`, {doc}`renderlab`, {doc}`framelab`,
{doc}`worldlab`. The {doc}`labwindow` and {doc}`labmenu` pages are reference
listings of every action available in those two surfaces.
