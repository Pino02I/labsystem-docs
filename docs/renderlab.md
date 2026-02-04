# RenderLAB

Smart rendering with automatic settings backup and viewport-based rendering.

---

## RenderLAB Info

Shows current scene statistics.

**Information displayed:**
- Objects: X visible / X hidden
- Mesh: X visible / X hidden
- Lights: X visible / X hidden

---

## Render Viewport

Renders only viewport-visible objects.

### Viewport Render
Button to access viewport render mode.

### Frame
Renders single frame of viewport-visible objects.

**⚙ Settings icon:** Quick settings access

### Animation
Renders animation of viewport-visible objects.

**What happens:**
1. Checks viewport visibility
2. Hides non-visible objects temporarily
3. Renders
4. Restores original visibility

---

## Render Selection

Renders only selected objects.

### Selection Render
Shows selection status.

**Status:** "1 objects selected" (updates dynamically)

### Frame
Renders single frame with selected objects only.

**⚙ Settings icon:** Quick settings access

### Animation
Renders animation with selected objects only.

### Lights Enabled
Toggle button to include/exclude lights in selection render.

**When enabled (blue):**
- Button shows "Lights Enabled"
- Status: "Lights enabled" with light icon

**When disabled:**
- Button not highlighted
- Lights excluded from selection render

---

## Viewport Visibility

Batch visibility controls.

### Viewport Visibility (Eye Icon)
Shows number of selected objects.

**Display:** "Selected: 1"

### Toggle All Viewport
Shows/hides all objects in viewport.

### Toggle Selected (1)
Shows/hides selected objects.
- Number in parentheses shows selected count

### Hide Unselected
Hides all objects except selected ones.

**Use this for:** Isolating specific objects

---

## Quick Reference

**Viewport render workflow:**
1. Hide objects you don't want
2. Click "Render Viewport - Frame"
3. Fast preview render
4. Visibility restored automatically

**Selection render workflow:**
1. Select objects to render
2. Toggle "Lights Enabled" if needed
3. Click "Frame" under Selection Render
4. Only selected objects render

**Isolation workflow:**
1. Select objects you want
2. Click "Hide Unselected"
3. Work on isolated objects
4. Click "Toggle All Viewport" to restore

**Lights control:**
- Lights Enabled (blue) = Lights render with selection
- Lights disabled (gray) = Only selected objects, no lights

**Pro tips:**
- RenderLAB Info updates in real-time
- Viewport Visibility is fastest for isolating objects
- Selection Render respects light toggle
- Use Hide Unselected for focus work
- All render operations have automatic backup protection
