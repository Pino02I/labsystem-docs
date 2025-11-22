# RenderLAB

Smart rendering with automatic settings backup and viewport-based rendering.

## RenderLAB Info

Shows current render statistics.

**Information displayed:**
- Backup status (when active)
- Object count (visible vs hidden)
- Breakdown by object type:
  - Mesh, Curve, Surface, Metaball
  - Text, Point Cloud, Volume
  - Grease Pencil, Lights

---

## Render Viewport

Renders only objects visible in your viewport.

### Frame
Renders a single frame of viewport-visible objects.

**What it does:**
1. Checks viewport visibility
2. Hides everything else temporarily
3. Renders the frame
4. Restores original visibility

### Animation
Renders full animation of viewport-visible objects.

**Same as Frame but for entire frame range**

---

## Render Selection

Renders only selected objects.

### Frame
Renders a single frame with selected objects only.

**Info shown:** Number of selected objects

### Animation
Renders animation with selected objects only.

### Lights Toggle
Enable/disable lights in selection render.

**Two states:**
- Lights Enabled - All lights render
- Lights Disabled - Lights excluded

**Button:** Click to toggle between states

---

## Viewport Visibility

Batch visibility controls for selected objects.

### Show Selected Objects
Makes all selected objects visible in viewport.

### Hide Selected Objects
Hides all selected objects in viewport.

### Isolate Selected
Hides everything except selected objects.

**Use this for:** Focus on specific objects

### Show All Objects
Makes all objects visible in viewport.

---

## Render Settings

Standard render operations with backup protection.

### Render Image
Standard Blender render (F12) with automatic backup.

**Safety:** Settings backed up before render

### Render Animation
Renders full frame range with automatic backup.

**Safety:** Settings restore even if cancelled (Esc)

---

## Settings Management

Save and load complete render configurations.

### Save Render Settings
Exports all render settings to a JSON file.

**What gets saved:**
- Resolution (X, Y, percentage)
- Output format and path
- Sampling settings
- Performance options
- Film and color settings
- All render properties

**Steps:**
1. Configure render settings
2. Click "Save Render Settings"
3. Choose location and filename
4. Done

### Load Render Settings
Imports previously saved settings.

**Steps:**
1. Click "Load Render Settings"
2. Select file
3. Settings apply instantly

---

## Auto-Restore System

Automatic backup and restoration of render settings.

### Restore Settings
Manually restores the last backup.

**When to use:**
- After canceling a render
- If settings seem wrong
- As a safety check

**Safe to use multiple times**

---

## Quick Reference

**Viewport Render workflow:**
1. Hide objects you don't want
2. Click "Render Viewport - Frame"
3. Fast preview render
4. Original visibility restored

**Selection Render workflow:**
1. Select objects to render
2. Toggle lights if needed
3. Click "Render Selection - Frame"
4. Only selected objects render

**Quality progression:**
- Save "Draft" settings (low res, fast)
- Save "Preview" settings (medium quality)
- Save "Final" settings (high quality)
- Load appropriate preset when rendering

**Common configurations to save:**

**Draft:**
- Resolution: 960×540
- Samples: 32
- Purpose: Quick tests

**Preview:**
- Resolution: 1920×1080
- Samples: 128
- Purpose: Client reviews

**Final:**
- Resolution: 3840×2160
- Samples: 512+
- Purpose: Final delivery

**Pro tip:** The auto-restore system means you can experiment safely - settings always restore automatically
