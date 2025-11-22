# LightLAB

Centralized lighting control with batch operations and camera-light management.

## LightLAB Info

Shows lighting statistics.

**Information displayed:**
- Total lights in scene
- Number of selected lights

---

## Light Management

Manage all lights in your scene.

### Show List / Hide List
Toggles light list visibility.

### Select All
Selects all lights in the scene.

### Cleanup
Removes invalid light references.

### Search Lights
Filter lights by name.

### Light List - Per Light Icons

Each light in the list shows:

**☐ Checkbox**
- Check/uncheck for multi-selection

**Light Name (with type icon)**
- Point, Sun, Spot, or Area icon
- Light name displayed

**Selectable Icon**
- Toggle if light can be selected in viewport

**👁 Eye Icon (hide_get)**
- Temporary hide/show in viewport
- Like Outliner eye icon

**Monitor Icon (hide_viewport)**
- Disable/enable in viewport permanently

**Render Icon (hide_render)**
- Enable/disable in renders

**Rename**
- Change light name

**Collection**
- Move light to different collection

**✖ Delete**
- Remove this light

---

## Quick Controls

### Enable/Disable Selected Lights

**Show Selected**
- Makes selected lights visible

**Hide Selected**
- Hides selected lights

**Isolate Selected**
- Hides all except selected

**Show All**
- Makes all lights visible

---

## Camera-Light Management

Assign specific lights to specific cameras.

### Show List / Hide List
Toggles camera list visibility.

### Camera List

For each camera:

**Camera icon**
- 📷 Active camera indicator
- 🎥 Inactive camera icon

**Camera Name**
- Displayed

**Light Icon**
- 💡 LightLAB enabled
- 🔆 LightLAB disabled

**Triangle**
- ▼ Expanded - shows light list
- ▶ Collapsed - hides light list

### Per-Camera Light Assignment

When expanded, each camera shows:

**LightLAB Status**
- If disabled: "LightLAB disabled - using all lights"
- If enabled: Light assignment controls

**Toggle Selected Button**
- Assigns/unassigns all currently selected lights
- Quick bulk assignment

**Clear All**
- Removes all light assignments
- Camera uses all lights

**Assign All**
- Assigns all scene lights to this camera

**Search Lights**
- Filter lights by name

**Light List (per camera):**
- ☐ Checkbox for each light
- Check = assigned to camera
- Uncheck = not assigned

---

## Batch Energy Control

Adjust multiple lights at once.

### Energy Multiplier
Set multiplier value (0.1 to 10.0)

**Examples:**
- 0.5 = Half brightness
- 1.0 = No change
- 2.0 = Double brightness

### Apply to Selected
Applies multiplier to all checked lights.

**Maintains proportions:** If one light is brighter, it stays proportionally brighter

### Apply to All
Applies multiplier to all lights in scene.

---

## Light Presets

Save and load complete lighting setups.

### Save Light Setup
Exports all light properties to file.

**What gets saved:**
- All light positions
- Energy values
- Colors and temperatures
- Enable/disable states
- All properties

**Steps:**
1. Set up lights
2. Click "Save Light Setup"
3. Choose filename
4. Done

### Load Light Setup
Imports saved lighting configuration.

**Steps:**
1. Click "Load Light Setup"
2. Select preset file
3. Lights update instantly

---

## Quick Reference

**Per-camera lighting workflow:**
1. Expand camera in Camera-Light Management
2. Enable LightLAB for that camera
3. Check lights you want for this camera
4. Repeat for other cameras
5. Each camera renders with its assigned lights

**Global lighting adjustment:**
1. Check all lights (or use Select All)
2. Set energy multiplier (e.g., 1.5)
3. Click "Apply to Selected"
4. All lights brighten proportionally

**Lighting presets workflow:**
1. Set up day lighting
2. Save as "Day_Lighting"
3. Set up night lighting
4. Save as "Night_Lighting"
5. Load presets as needed

**Quick light filtering:**
1. Use search to find specific lights
2. Check lights you want to adjust
3. Use batch controls
4. Fast targeted adjustments

**Toggle Selected feature:**
1. Select lights in 3D view
2. Expand camera
3. Click "Toggle Selected"
4. Selected lights assigned/unassigned instantly

**Pro tips:**
- Use Camera-Light Management for different lighting per camera
- Toggle Selected is fastest for bulk assignment
- Energy multipliers maintain relative brightness
- Save presets for common lighting scenarios (day, night, studio)
- Use search when working with many lights
