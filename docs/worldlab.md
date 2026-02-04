# WorldLAB

Per-camera HDRI and world shader assignment system with automatic synchronization.

---

## Overview

WorldLAB allows each camera to have its own dedicated HDRI/world shader with custom strength and rotation settings. When you switch cameras, the world automatically updates in the viewport and during rendering.

**Key Features:**
- Assign different HDRIs to different cameras
- Per-camera Strength control (0-10)
- Per-camera Rotation control (0-360°)
- Automatic sync when changing cameras
- HDRI import directly in the addon
- Real-time viewport updates

---

## Camera World Assignment

Manage which world/HDRI is assigned to each camera.

### Enable WorldLAB for Camera

Toggle WorldLAB on/off for the active camera.

**When enabled:**
- Camera uses its assigned world shader
- Auto-sync activates when switching cameras
- Strength and rotation settings apply

**When disabled:**
- Camera uses the scene's default world
- No automatic world switching

---

## World List

Shows all available world shaders in your blend file.

### Expand/Collapse List
Click to show or hide the world list.

### World Items

Each world in the list displays:

- **World Name** - Click to assign to active camera
- **Checkbox** - Shows if this world is assigned to current camera
- **Active Indicator** - Shows which world is currently active in scene

### World Management Operators

- **Create New World** - Creates a basic world shader setup
- **Rename World** - Change world shader name
- **Duplicate World** - Copy an existing world with all settings
- **Delete World** - Remove world from blend file
- **Set Active World** - Make this the scene's active world

---

## Per-Camera Controls

These settings are unique to each camera when WorldLAB is enabled.

### Strength Control

**Range:** 0.0 to 10.0

Controls the intensity of the Background shader in the world.

**Common values:**
- 0.5-1.0 - Subtle ambient lighting
- 1.0-2.0 - Standard HDRI lighting
- 2.0-5.0 - Strong environmental light
- 5.0-10.0 - Very bright/overexposed look

**How it works:**
- Adjusts the "Strength" input of the Background node
- Changes apply in real-time in viewport
- Each camera remembers its own strength value

### Rotation Control

**Range:** 0° to 360°

Rotates the HDRI around the Z-axis.

**How it works:**
- Creates/uses a Mapping node in the world shader
- Connects to the Environment Texture's Vector input
- Rotates the texture coordinates
- Each camera remembers its own rotation value

**Workflow:**
1. Assign HDRI to camera
2. Adjust rotation to position sun/highlights
3. Fine-tune with precise degree values
4. Each camera can have different rotation

---

## Camera List

Shows all cameras in the scene with their WorldLAB status.

### Expand/Collapse
Click to show or hide the camera list.

### Camera Items

Each camera displays:

- **Camera Name** - Identifies the camera
- **WorldLAB Status** - Shows if WorldLAB is enabled (✓) or disabled (✗)
- **Assigned World** - Shows which world is assigned (if any)

### Per-Camera World Assignment

Click the camera name to:
- View its WorldLAB settings
- Assign/change its world
- Adjust its strength and rotation

---

## HDRI Import

Import HDRI images directly into your world shaders.

### Import HDRI Button

**File formats supported:**
- .hdr
- .exr
- .jpg/.jpeg
- .png

**What happens:**
1. Click "Import HDRI"
2. Select HDRI file from disk
3. WorldLAB creates a new world shader
4. Sets up proper node connections:
   - Texture Coordinate (Generated output)
   - Mapping node (for rotation)
   - Environment Texture (your HDRI)
   - Background shader
   - World Output
5. Names the world after the HDRI filename
6. Automatically assigns to active camera (if WorldLAB enabled)

**Node setup created:**
```
[Texture Coord] → [Mapping] → [Environment Texture] → [Background] → [World Output]
                      ↓               ↑
                  Rotation        Your HDRI
                                     ↓
                                 Strength
```

---

## Export World

Save world shader configurations to share between projects.

### Export World

Exports the selected world shader data including:
- Node setup
- HDRI filepath (if using Environment Texture)
- Background color/strength
- All node connections

**How to use:**
1. Select the world you want to export
2. Click "Export World"
3. Choose save location
4. File saved with .world extension

**Note:** The HDRI image file itself is not embedded; only the filepath is saved. Make sure to keep your HDRI files accessible.

---

## Workflows

### Workflow 1: Architectural Visualization with Day/Night

**Setup:**
1. Create two cameras: "Exterior_Day" and "Exterior_Night"
2. Import two HDRIs: day.hdr and night.hdr
3. Assign day.hdr to Exterior_Day camera
4. Assign night.hdr to Exterior_Night camera
5. Adjust strength: Day = 1.5, Night = 0.8
6. Adjust rotation to position sun correctly for each

**Result:**
- Switch to Exterior_Day → Day HDRI loads automatically
- Switch to Exterior_Night → Night HDRI loads automatically
- Each camera maintains its lighting settings

### Workflow 2: Product Photography with Different Moods

**Setup:**
1. Create three cameras: "Studio", "Outdoor", "Dramatic"
2. Import three HDRIs:
   - studio_neutral.hdr → Studio camera
   - outdoor_park.hdr → Outdoor camera
   - dramatic_sunset.hdr → Dramatic camera
3. Set strength: Studio = 2.0, Outdoor = 1.0, Dramatic = 3.0
4. Rotate each HDRI to best lighting angle

**Result:**
- Instant preview switching between different lighting scenarios
- Each camera shows the product in different environment
- No manual HDRI swapping needed

### Workflow 3: Character in Multiple Environments

**Setup:**
1. Create cameras for different scenes
2. Assign appropriate HDRI to each:
   - Interior scenes → Indoor HDRIs
   - Exterior scenes → Outdoor HDRIs
   - Night scenes → Night sky HDRIs
3. Adjust strength/rotation per scene requirements

**Result:**
- Character automatically appears in correct environment per camera
- Lighting matches the intended scene
- Easy to compare different environments

---

## Auto-Sync Behavior

WorldLAB automatically syncs the world when you change cameras.

### Viewport Sync

**When it happens:**
- Any time you change the active camera in the scene
- Switching camera in viewport
- Setting a different camera as scene camera

**What it does:**
1. Detects camera change
2. Checks if new camera has WorldLAB enabled
3. If yes, loads that camera's assigned world
4. Applies that camera's strength setting
5. Applies that camera's rotation setting
6. Updates viewport in real-time

### Render Sync

**When it happens:**
- Just before render starts (render_pre handler)

**What it does:**
1. Checks the scene camera being rendered
2. If camera has WorldLAB enabled
3. Applies that camera's world settings
4. Render proceeds with correct HDRI/world

**Result:**
Rendered images automatically use the correct world for each camera, even in batch rendering with FrameLAB.

---

## World Shader Node Setup

WorldLAB works with standard Blender world shaders.

### Compatible Node Setups

**Basic (created by WorldLAB):**
```
[Background] → [World Output]
```

**With HDRI (created by Import HDRI):**
```
[Texture Coord] → [Mapping] → [Environment Texture] → [Background] → [World Output]
```

**Custom setups:**
WorldLAB can work with custom world shader setups. It will:
- Look for Background node to adjust Strength
- Look for Environment Texture to add rotation control
- Create Mapping node if rotation is needed

### What WorldLAB Modifies

**Strength control:**
- Finds the Background node
- Adjusts its Strength input value
- Per-camera value applied

**Rotation control:**
- Finds or creates Texture Coordinate node
- Finds or creates Mapping node
- Connects: TexCoord (Generated) → Mapping → Env Texture
- Adjusts Mapping node's Rotation Z value
- Per-camera rotation applied

---

## Tips & Best Practices

**Organization:**
- Name your worlds descriptively (e.g., "Day_HDRI", "Night_HDRI")
- Name cameras to match their assigned worlds (e.g., "Cam_Day", "Cam_Night")
- Keep similar HDRIs grouped in your file structure

**Performance:**
- Use lower resolution HDRIs for viewport preview
- Switch to high-res HDRIs for final renders
- Rotation is real-time, strength is instant

**Workflow efficiency:**
- Set up all camera-world assignments early
- Test with viewport rendering (RenderLAB)
- Batch render all cameras with FrameLAB

**Strength values guide:**
- Interior shots: 0.5-1.5
- Exterior daylight: 1.0-2.0
- Studio lighting: 1.5-3.0
- Dramatic/sunset: 2.0-5.0
- Overexposed look: 5.0-10.0

**Rotation workflow:**
- Import HDRI first
- Assign to camera
- Rotate viewport to desired angle
- Adjust world rotation to match sun position
- Fine-tune with numeric input for precision

---

## Troubleshooting

### World doesn't change when switching cameras

**Check:**
1. Is WorldLAB enabled for that camera?
2. Is a world assigned to the camera?
3. Does the assigned world still exist in the file?

**Solution:**
- Enable WorldLAB toggle for camera
- Assign a world from the world list
- If world was deleted, assign a different one

### Rotation doesn't work

**Check:**
1. Is there an Environment Texture node in the world?
2. Is the world using nodes?

**Solution:**
- WorldLAB needs an Environment Texture to rotate
- Import an HDRI using WorldLAB's Import HDRI button
- Or manually add an Environment Texture node

### Strength changes don't show

**Check:**
1. Is there a Background node in the world shader?
2. Is the world using nodes?

**Solution:**
- Enable "Use Nodes" in world shader
- Add a Background node if missing
- Connect Background to World Output

### HDRI looks wrong after import

**Check:**
- File path is correct
- HDRI file format is supported (.hdr, .exr, .jpg, .png)

**Solution:**
- Re-import HDRI
- Check if file exists at the imported path
- Try a different HDRI file

### Viewport doesn't update in real-time

**Possible causes:**
- Very large HDRI file (slow to load)
- Complex world shader setup
- Viewport shading not set to rendered

**Solutions:**
- Use smaller resolution HDRI for viewport
- Simplify world shader nodes
- Switch viewport shading to "Rendered" mode

---

## Quick Reference

**Basic setup:**
1. Enable WorldLAB for camera
2. Assign world from list (or import HDRI)
3. Adjust strength and rotation
4. Switch cameras to test auto-sync

**Import HDRI workflow:**
1. Click "Import HDRI"
2. Select .hdr or .exr file
3. World created and assigned automatically
4. Adjust strength/rotation as needed

**Multi-camera setup:**
1. Create all cameras
2. Enable WorldLAB for each
3. Assign different worlds to each
4. Customize strength/rotation per camera
5. Switch cameras → worlds update automatically

**Batch rendering:**
1. Set up camera-world assignments
2. Use FrameLAB to render all cameras
3. Each render uses its camera's world settings

**Export/share:**
- Export world: Share world setup between projects
- Export camera: Camera includes WorldLAB assignment data
