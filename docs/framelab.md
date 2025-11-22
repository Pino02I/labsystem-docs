# FrameLAB

Multi-camera rendering system with batch operations.

---

## FrameLAB Info

Shows camera status and rendering information.

**Information displayed:**
- Cameras: 1
- Active: Camera (name of active camera)

---

## Camera Management

Manage cameras for batch rendering.

**Shows:** Camera Management... 1/1

### All
Enables all cameras for rendering.

### None
Disables all cameras from rendering.

### Show
Shows all cameras in viewport.

### Hide
Hides all cameras in viewport.

### Show Cameras
Expands camera list.

**Camera List (when expanded):**
- ☐ Checkbox - Enable/disable for rendering
- Camera name - Click to set active
- Active camera highlighted

---

## Render Sequence

Batch render multiple cameras.

**Header:** Render Sequence

### Format
Select output file format.

**Dropdown shows:** 🖼 PNG

**Available formats:**
- PNG
- JPEG
- OpenEXR
- TIFF
- etc.

### Viewport Render Mode
☐ Checkbox to enable viewport visibility filtering.

**When enabled:**
- Uses viewport visibility for rendering
- Objects hidden in viewport won't render

### Frame

**Two buttons:**
- **All (1)** - Renders all enabled cameras (1 frame each)
- **Selected** - Renders selected cameras only (1 frame each)

Number in parentheses shows enabled camera count.

### Animation

**Two buttons:**
- **All (1)** - Renders animation for all enabled cameras
- **Selected** - Renders animation for selected cameras only

Each camera renders full frame range.

---

## Output

Shows output settings and file browser access.

**Header:** Output

**Display:** PNG (current format)

### Open Browser
Opens file browser to output folder.

**Use this to:** Navigate to rendered files

---

## Quick Reference

**Basic multi-camera render:**
1. Enable cameras (checkboxes or "All" button)
2. Select format (PNG, JPEG, etc.)
3. Click "Frame - All (1)"
4. Each camera renders to separate file

**Selective rendering:**
1. Enable only cameras you need
2. Number updates (e.g., "All (3)")
3. Click "All" to render enabled cameras
4. Or select specific cameras and click "Selected"

**Animation sequence:**
1. Set frame range
2. Enable cameras
3. Click "Animation - All (1)"
4. Full animation renders for each camera

**Viewport mode workflow:**
1. Hide objects you don't want
2. Enable "Viewport Render Mode"
3. Render sequence
4. Only visible objects render

**Output management:**
1. Check current format (shows in Output section)
2. Click "Open Browser" to see files
3. Each camera file named automatically

**Pro tips:**
- Use "All/None" for quick enable/disable
- Number in parentheses shows enabled count
- Selected button only renders checked cameras
- Viewport mode speeds up test renders
- Each camera gets separate output file
- Format applies to all cameras in sequence
