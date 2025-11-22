# FrameLAB

Multi-camera rendering system with camera management.

## FrameLAB Info

Shows rendering status and camera information.

**Information displayed:**
- Total cameras in scene
- Active camera name
- Rendering progress (when active)

**STOP button:** Appears when rendering sequence is active

---

## Camera Management

Manage which cameras are enabled for batch rendering.

### Show Cameras / Hide Cameras
Toggles the camera list visibility.

### All / None
Enables or disables all cameras for rendering.

### Show / Hide
Shows or hides all cameras in viewport.

### Camera List

Each camera shows:

**☐ Checkbox**
- Enable/disable for rendering
- Only checked cameras render in batch

**Camera Name**
- Click to set as active camera
- Active camera highlighted

---

## Render Sequence

Batch render multiple cameras.

### Format
Select output file format (PNG, JPEG, etc.)

### Viewport Render Mode
Toggle to use viewport visibility filtering.

**When enabled:**
- Objects: Uses viewport visibility filter
- Lights: Managed by LightLAB

### Frame Rendering

**All (X)**
- Renders all enabled cameras (X = number enabled)
- Single frame per camera

**Selected**
- Renders only selected cameras
- Single frame per camera

### Animation Rendering

**All (X)**
- Renders animation for all enabled cameras
- Full frame range per camera

**Selected**
- Renders animation for selected cameras
- Full frame range per camera

---

## Output

Manage render output location.

### Current Output Info
Shows:
- Output filename pattern
- File format

### Open Browser
Opens file browser to output folder.

---

## Quick Reference

**Multi-camera render workflow:**
1. Enable cameras you want (checkboxes)
2. Select file format
3. Click "All" to render enabled cameras
4. Each camera renders to separate file

**Viewport mode workflow:**
1. Enable "Viewport Render Mode"
2. Hide objects you don't want
3. LightLAB manages lights per camera
4. Render sequence

**Selective rendering:**
1. Check specific cameras only
2. Click "Selected" to render only those
3. Faster than rendering all

**Animation sequence:**
1. Enable cameras
2. Set frame range
3. Click "Animation - All"
4. Full animation renders for each camera

**Pro tips:**
- Use checkboxes to enable only needed cameras
- Viewport mode speeds up test renders
- Output names include camera names automatically
- STOP button cancels sequence anytime
