# CameraLAB

Professional camera management with resolution presets.

## Camera Creation

### New from View
Creates a camera matching your current viewport position.

**How to use:**
1. Position viewport where you want
2. Click "New from View"
3. Camera created and set as active

**Info displayed:**
- View: Camera name (if in camera view)
- Perspective View / Orthographic View

---

## Camera Navigation

### Previous / Next Camera
Cycles through all cameras in sequence.

**Two buttons:**
- ◀ Previous - Go to previous camera
- Next ▶ - Go to next camera

**When visible:** Only when you have 2 or more cameras

---

## Collection Cameras

List and manage all cameras in your scene.

### Show List / Hide List
Toggles visibility of the camera list.

### Select All
Selects all cameras in the scene.

### Cleanup
Removes any invalid camera references.

### Show Camera Names in Viewport
Toggle to display camera names directly in the 3D viewport.

### Search Cameras
Search and filter cameras by name.

### Camera List - Per Camera Icons

Each camera in the list has these controls:

**☐ Checkbox**
- Check/uncheck for multi-selection

**Camera Name**
- Click to set as active camera
- ⚫ Radio button shows if active

**👁 View**
- Quick view through this camera

**Eye Icon**
- Show/hide camera in viewport

**Lock Icon**
- Lock/unlock camera position

**Rename**
- Change camera name

**Collection**
- Move camera to different collection

**Export**
- Export single camera data

**✖ Delete**
- Remove this camera

---

## Resolution / Camera

Manages resolution settings for the active camera.

### Width / Height
Set render resolution directly.

### Quick Resolution Presets

**Main buttons (always visible):**
- **DCI** - DCI 4K (4096×2160)
- **4K** - 4K UHD (3840×2160)
- **9:16** - Vertical format (1080×1920)
- **1:1** - Square format (1080×1080)

### More Presets
Click to expand additional resolution presets.

**Standard:**
- HD - Full HD (1920×1080)
- QHD - Quad HD (2560×1440)
- 768p - HD (1366×768)

**Cinema:**
- Scope - DCI Scope (2048×858)
- Flat - DCI Flat (1998×1080)
- 2K - DCI 2K (2048×1080)

**Social:**
- IG - Instagram 4:5 (1080×1350)
- 720p - Social HD (1280×720)

**Gaming:**
- UW - Ultrawide QHD (3440×1440)
- SUW - Super Ultrawide (3840×1080)
- UW FHD - Ultrawide FHD (2560×1080)
- Premium UW - (5120×1440)

**Pro:**
- ARRI - ARRI 4.6K (4608×3164)
- RED 8K - RED 8K (8192×4320)
- 2.4:1 - Widescreen 2.4:1
- Presentation - (1920×1200)

### Add Keyframe / Keyframe
Adds keyframe for resolution animation.

**Info button:** Shows keyframe information (when keyframes exist)

---

## Viewport & Depth of Field

Camera viewport and DOF controls.

### Viewport Lock
Lock camera to view (camera follows viewport).

### Depth of Field Toggle
Enable/disable depth of field for active camera.

**DOF Controls (when enabled):**
- Focus distance
- F-Stop
- Aperture settings

---

## Camera Properties

Quick access to camera settings.

### Focal Length
Lens focal length in mm.

### Sensor Size
Camera sensor dimensions.

### Clip Start / End
Near and far clipping distances.

### Camera Type
- Perspective
- Orthographic
- Panoramic

---

## Advanced Operations

### Align Camera to Object
Points camera at selected object.

**Steps:**
1. Select object
2. Select camera
3. Click "Align to Object"

### Camera from Cursor
Moves camera to 3D cursor position.

### Copy Camera Settings
Copies settings from one camera to another.

**Steps:**
1. Select source camera
2. Select target camera
3. Click "Copy Settings"

---

## Quick Reference

**Typical workflow:**
1. Create camera with "New from View"
2. Use quick presets for common resolutions
3. Navigate with Previous/Next buttons
4. Use camera list for precise selection

**Multi-camera workflow:**
1. Create all needed cameras
2. Use collections to organize
3. Use checkboxes for batch operations
4. Lock cameras when positioned

**Pro tips:**
- Use "Show Camera Names in Viewport" when working with many cameras
- Lock cameras to prevent accidental movement
- Use resolution presets for consistent output
- Organize cameras in collections by purpose
