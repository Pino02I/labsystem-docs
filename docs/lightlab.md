# LightLAB

Centralized lighting control with batch operations and camera-light management.

---

## LightLAB Info

Shows lighting statistics.

**Information displayed:**
- Total Lights: 1
- Selected: 1

---

## Light Management

Manage all lights in your scene.

### Show List
Expands light list.

### Select All
Selects all lights in scene.

### Cleanup
Removes invalid light references.

### Light List (when expanded)

Each light shows:
- ☐ Checkbox for multi-selection
- Light name with type icon
- Selectable, Eye, Monitor, Render icons
- Rename, Collection, Delete icons

---

## Camera-Light Management

Assign specific lights to cameras.

**Shows:** Cameras (1)

### Show List
Expands camera list for light assignment.

---

## Quick Actions

Fast light operations.

### Light (POINT) 1
Shows active light name and type.

### Convert & Edit Type

**Four light type buttons:**
- **⚪ Point** - Point light
- **☀ Sun** - Sun light
- **🔦 Spot** - Spot light
- **◻ Area** - Area light

**Click to convert light to that type**

### POINT Settings (Real-Time)

Shows current light settings that update in real-time.

**Radius:** 0.1 m (slider)

**Soft Falloff:** (slider control)

---

## Align Light

Position lights precisely.

### Align to 3D Cursor
Moves light to 3D cursor position.

### Align to Target
Points light at target object.

### 1 Point (position only)
Position-only alignment mode.

---

## Light Properties

Direct access to light settings.

**Selected:** 1 lights

### Strength
Light intensity slider.

**Strength (W):** 1000.000 (watts)

### Quick Multiply

Fast intensity adjustments:
- **÷10** - Divide by 10
- **÷5** - Divide by 5
- **÷2** - Divide by 2
- **100W** - Set to 100 watts
- **×2** - Multiply by 2
- **×5** - Multiply by 5
- **×10** - Multiply by 10

### Color

#### RGB Color (Real-Time)
Color picker with real-time preview.

#### Color Temperature

**Kelvin:** 6500K (slider)

Shows temperature value with adjustable slider.

### Quick Presets

**Select Preset:** Dropdown menu

Pre-configured light presets for common scenarios.

---

## Quick Reference

**Change light type:**
1. Select light
2. Click desired type button (Point/Sun/Spot/Area)
3. Light converts instantly

**Adjust intensity quickly:**
1. Select light
2. Use Quick Multiply buttons
3. ×2 doubles brightness, ÷2 halves it

**Color workflow:**
1. Use RGB Color for precise control
2. Or use Color Temperature for realistic lighting
3. Kelvin slider for warm/cool adjustment

**Alignment workflow:**
1. Position 3D cursor where needed
2. Select light
3. Click "Align to 3D Cursor"
4. Light moves to cursor

**Target lighting:**
1. Select target object
2. Select light
3. Click "Align to Target"
4. Light points at target

**Pro tips:**
- Quick Multiply buttons are fastest for iteration
- Use Color Temperature for realistic lighting
- Point lights for local illumination
- Sun lights for outdoor/directional
- Spot lights for focused beams
- Area lights for soft, realistic shadows
- Real-time settings update as you adjust
