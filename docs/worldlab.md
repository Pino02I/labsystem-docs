# WorldLAB

Per-camera HDRI and world shader assignment with automatic synchronization.

---

## WorldLAB Info

Shows world assignment status.

**Information displayed:**
- Current camera world assignment
- WorldLAB enabled/disabled status

---

## Camera World Assignment

Enable WorldLAB for the active camera.

### Enable WorldLAB
Toggle WorldLAB on/off for current camera.

**When enabled:**
- Camera uses assigned world shader
- Auto-sync when switching cameras
- Strength and rotation settings apply

**When disabled:**
- Camera uses scene default world
- No automatic world switching

---

## World Management

Manage all world shaders in your scene.

### Show List
Expands world list.

### World List (when expanded)

Each world shows:
- World name - Click to assign to camera
- ☐ Checkbox - Shows if assigned to current camera
- Active indicator - Current scene world

### World Operations

**Available actions:**
- **Create** - New world shader
- **Rename** - Change world name
- **Duplicate** - Copy world with settings
- **Delete** - Remove world
- **Set Active** - Make scene active world

---

## Per-Camera Controls

Custom settings for each camera.

**Shows:** Camera - ACTIVE

### Strength

**Range:** 0.0 to 10.0

Controls HDRI/background intensity.

**Slider adjusts:** Background node Strength value

**Common values:**
- 0.5-1.0 - Subtle ambient
- 1.0-2.0 - Standard lighting
- 2.0-5.0 - Strong light
- 5.0-10.0 - Very bright

### Rotation

**Range:** 0° to 360°

Rotates HDRI around Z-axis.

**Slider adjusts:** Mapping node Rotation Z value

**Use for:** Position sun/highlights in HDRI

---

## Camera List

Shows all cameras with WorldLAB status.

**Shows:** Cameras (1)

### Show List
Expands camera list.

**Camera List (when expanded):**
- Camera name
- WorldLAB status (✓ enabled / ✗ disabled)
- Assigned world name (if any)

---

## Import

Import HDRI images or complete world shader setups.

### Import HDRI

Import HDRI image files directly.

**Supported formats:**
- .hdr
- .exr
- .jpg / .jpeg
- .png

**What happens:**
1. Select HDRI file
2. Creates new world shader
3. Sets up node connections (TexCoord → Mapping → Env Texture → Background)
4. Names world after filename
5. Assigns to active camera (if WorldLAB enabled)

### Import World (JSON)

Import complete world shader setup from JSON file.

**File format:** .json

**What's imported:**
- Complete node tree with all nodes
- All node connections
- Node positions and properties
- HDRI filepath (if Environment Texture present)
- Color ramps, node groups, and custom setups

**How to use:**
1. Click "Import JSON"
2. Select .json file (exported from WorldLAB)
3. World created with complete node setup
4. Ready to assign to cameras

---

## Export

Save world shader configuration to share or backup.

### Export World (JSON)

Exports complete world shader data to JSON file.

**What's exported:**
- Full node tree with all nodes
- All node connections and properties
- HDRI filepath
- Node positions (for visual layout)
- Node groups used in the shader

**File format:** .json

**Use for:**
- Share complete world setups between projects
- Backup complex world shader configurations
- Create reusable world shader libraries

**Note:** HDRI image file itself is not embedded; only the filepath is saved. Make sure HDRI files are accessible when importing.

---

## Quick Reference

**Basic setup:**
1. Enable WorldLAB for camera
2. Assign world from list (or import HDRI)
3. Adjust strength and rotation
4. Switch cameras to test

**Import HDRI workflow:**
1. Click "Import HDRI"
2. Select .hdr or .exr file
3. World created and assigned
4. Adjust strength/rotation

**Import World (JSON) workflow:**
1. Click "Import JSON"
2. Select .json file
3. Complete world setup imported with all nodes
4. Ready to assign to cameras

**Export World workflow:**
1. Select world to export
2. Click "Export World"
3. Save as .json file
4. Share between projects or backup

**Multi-camera setup:**
1. Create cameras
2. Enable WorldLAB for each
3. Assign different worlds
4. Customize strength/rotation
5. Switch cameras → auto-sync

**Archviz example:**
- Exterior_Day camera → day.hdr (Strength: 1.5)
- Exterior_Night camera → night.hdr (Strength: 0.8)
- Switch camera → HDRI updates automatically

**Product example:**
- Studio camera → studio.hdr (Strength: 2.0)
- Outdoor camera → park.hdr (Strength: 1.0)
- Dramatic camera → sunset.hdr (Strength: 3.0)

**Pro tips:**
- Name worlds descriptively (Day_HDRI, Night_HDRI)
- Rotation positions sun in HDRI
- Each camera remembers its settings
- Works with FrameLAB batch rendering
- Viewport updates in real-time
- Lower res HDRIs for viewport speed
