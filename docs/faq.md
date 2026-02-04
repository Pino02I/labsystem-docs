# FAQ - Frequently Asked Questions

Common questions about LABsystem and how to use it effectively.

---

## General Questions

### What is LABsystem?
LABsystem is a professional camera and rendering ecosystem for Blender. It provides four modules (CameraLAB, RenderLAB, LightLAB, FrameLAB) that work together to streamline your workflow.

### Do I need to enable all modules?
No. Enable only the modules you need. Go to Edit > Preferences > Add-ons > LABsystem to enable/disable individual modules.

### Where do I find LABsystem in Blender?
Press **N** in the 3D View to open the sidebar. Click the **LABsystem** tab. You can also use LABwindow (F1) or LABmenu (Ctrl+Alt+Shift+Numpad 0).

### Does LABsystem work with Blender 3.x and 4.x?
Yes. LABsystem requires Blender 3.0 or newer and works with all current versions.

### Can I use LABsystem in production?
Absolutely. LABsystem is designed for professional production workflows with automatic backup systems and safe operation modes.

---

## CameraLAB Questions

### How do I create a camera quickly?
Position your viewport where you want, then click **"New from View"** in CameraLAB. The camera is created instantly at that exact position.

### Can I save different resolutions for each camera?
Yes! Each camera can have its own resolution presets. However, note that CameraLAB currently applies resolution to the scene render settings, not per-camera storage. Use the quick presets (DCI, 4K, 9:16, 1:1) for fast switching.

### What's the difference between Lock Camera to View and regular camera movement?
**Lock Camera to View** makes the camera follow your viewport navigation. When enabled, moving the viewport moves the camera. Use Walk or Fly navigation modes for smooth movement.

### How do I align a camera to an object?
1. Select the object you want to frame
2. In Quick Actions, click **"Frame Selected"**
3. The camera frames your object automatically

### What does Passepartout Alpha do?
It darkens the area outside the camera view in the viewport. Higher values = darker. This helps you focus on what will actually render.

### Can I convert a camera between Perspective and Orthographic?
Yes. In the Viewport & Lens section, click **Perspective** or **Orthographic** button to convert the camera type instantly.

---

## RenderLAB Questions

### What's the difference between Render Viewport and Render Selection?
- **Render Viewport**: Renders only objects visible in viewport (uses Eye icon visibility)
- **Render Selection**: Renders only objects you have selected in the 3D view

### Why use Viewport Render instead of hiding objects manually?
Viewport Render automatically hides objects, renders, then restores everything. You don't need to manually unhide objects afterward - RenderLAB handles it automatically.

### What does "Lights Enabled" do in Render Selection?
It controls whether lights are included when rendering selection:
- **Enabled (blue)**: Lights render with selected objects
- **Disabled (gray)**: Only selected objects render, no lights

### How do I isolate objects for rendering?
Use **"Hide Unselected"** in Viewport Visibility:
1. Select objects you want to keep
2. Click "Hide Unselected"
3. Everything else is hidden
4. Click "Toggle All Viewport" to restore

### Does RenderLAB back up my settings automatically?
Yes. Every render operation automatically creates a backup. If you cancel (Esc) or something goes wrong, settings restore automatically. You can also use **"Restore Settings"** manually.

### Can I save render presets for different quality levels?
Yes, though this feature is in the settings management. You can configure render settings and save them, then load them later. Create presets for Draft, Preview, and Final renders.

---

## LightLAB Questions

### How do I quickly adjust all lights together?
1. Click **"Select All"** in Light Management
2. Use **Quick Multiply** buttons (×2, ×5, ×10, etc.)
3. All light intensities multiply proportionally

### What's the difference between Point, Sun, Spot, and Area lights?
- **Point**: Omnidirectional, like a light bulb
- **Sun**: Directional parallel rays, like sunlight
- **Spot**: Focused cone of light, like a flashlight
- **Area**: Rectangular light source, creates soft shadows

### Can I convert a light from Point to Spot?
Yes. In **Convert & Edit Type**, click the light type you want. The light converts instantly while keeping its position and settings.

### What does "Real-Time" mean in POINT Settings?
Settings update immediately in the viewport as you adjust them. You see changes instantly without waiting.

### How do I set color temperature instead of RGB?
Use the **Color Temperature** section with the Kelvin slider:
- 2700K = Warm (candlelight)
- 4500K = Neutral (daylight)
- 6500K = Cool (overcast)

### Can I assign specific lights to specific cameras?
Yes! Use **Camera-Light Management**:
1. Expand the camera list
2. Expand a camera
3. Check the lights you want for that camera
4. Each camera can have different light assignments

### What's the fastest way to assign selected lights to a camera?
Use the **"Toggle Selected"** button:
1. Select lights in the 3D view
2. Expand the camera in Camera-Light Management
3. Click "Toggle Selected"
4. All selected lights assign/unassign instantly

---

## FrameLAB Questions

### What does FrameLAB actually do?
FrameLAB is a **multi-camera batch rendering system**. It renders multiple cameras in sequence, creating separate output files for each camera.

### How do I render multiple cameras at once?
1. Enable cameras using checkboxes (or click "All")
2. Select output format (PNG, JPEG, etc.)
3. Click **"Frame - All (1)"** for single frame
4. Or **"Animation - All (1)"** for full animation
5. Each camera renders to a separate file

### What does the number in "All (1)" mean?
It shows how many cameras are enabled for rendering. If you enable 3 cameras, it shows "All (3)".

### What's Viewport Render Mode in FrameLAB?
When enabled, FrameLAB uses viewport visibility filtering. Objects hidden in viewport won't render for any camera. Useful for test renders.

### How are output files named?
Each camera gets a separate file. The filename includes the camera name automatically, so you can identify which camera rendered which file.

### Can I render only specific cameras?
Yes. Either:
1. Enable only those cameras (checkboxes)
2. Use the **"Selected"** button instead of "All"

### What's the difference between Frame and Animation rendering?
- **Frame**: Renders one frame per camera (fast)
- **Animation**: Renders full frame range per camera (slow, production)

---

## Workflow Questions

### What's the best workflow for multiple cameras with different resolutions?
1. Create all cameras with CameraLAB
2. For each camera, select it and use resolution presets
3. Use FrameLAB to batch render all cameras
4. Each renders at the scene resolution (switch presets between renders if needed)

### How do I set up day and night lighting quickly?
1. Set up day lighting
2. Use LightLAB to adjust all lights
3. Save preset (if available)
4. Adjust for night lighting
5. Render or save night preset

### Can I use LABsystem with render farms?
Yes. LABsystem works with standard Blender files. However, camera-light assignments and some settings are stored in the blend file, so make sure to save your file before sending to a render farm.

### What's the fastest way to test render different lighting setups?
1. Hide complex objects (RenderLAB - Viewport Visibility)
2. Use LightLAB Quick Multiply to adjust all lights
3. RenderLAB Viewport Render for fast preview
4. Iterate quickly

### How do I organize a complex multi-camera project?
1. Use CameraLAB collections to group cameras by type/purpose
2. Name cameras clearly (e.g., "Hero_Wide", "Detail_Close")
3. Use FrameLAB to manage which cameras render
4. Use LightLAB Camera-Light Management for per-camera lighting

---

## Technical Questions

### Does LABsystem slow down Blender?
No. LABsystem modules only run when you use them. Having many cameras or lights doesn't impact viewport performance.

### Where are settings stored?
Most settings are stored in your blend file. Some preferences (like keyboard shortcuts) are stored in Blender preferences.

### Can I use LABsystem with other addons?
Yes. LABsystem is designed to work alongside other addons without conflicts.

### What happens if I disable a module?
The module's panel disappears from the sidebar, but your data (cameras, lights) remains intact. Re-enable the module to access features again.

### Does LABsystem work with Cycles and Eevee?
Yes. LABsystem works with all Blender render engines. It manipulates scene settings, not render engine internals.

---

## Troubleshooting Questions

### LABsystem tab doesn't appear in sidebar
1. Press N to open sidebar
2. Check LABsystem is enabled in Edit > Preferences > Add-ons
3. Check at least one module is enabled
4. Restart Blender if needed

### Camera won't switch when I click it
1. Make sure camera exists in scene (check Outliner)
2. Camera might be hidden - check visibility
3. Try selecting in Outliner first

### Render Selection isn't working
1. Make sure objects are actually selected (orange outline)
2. Check object types are renderable (Mesh, Curve, etc.)
3. Look at "X objects selected" - should be > 0

### Lights don't change when I use Quick Multiply
1. Make sure lights are selected (check "Selected: X lights")
2. Verify lights aren't hidden
3. Check console for error messages (Window > Toggle System Console)

### FrameLAB says "No enabled cameras"
1. Check camera checkboxes are enabled
2. Use "All" button to enable all cameras
3. Verify cameras exist in scene

### Viewport Render shows unexpected objects
1. Check Eye icon visibility in Outliner
2. Remember: Viewport Render uses viewport visibility, not render visibility
3. Use "Hide Unselected" to isolate specific objects

---

## Best Practices

### Should I lock cameras after positioning them?
Yes! Use the lock icon in CameraLAB camera list to prevent accidental movement. Essential in production.

### How many cameras is too many?
No technical limit. Projects with 20+ cameras work fine. Organize them in collections and name them clearly.

### Should I use Viewport Render Mode in FrameLAB for final renders?
No. Viewport Render Mode is for testing. For final renders, use standard mode with all objects visible.

### When should I use Lights Enabled vs Disabled in Render Selection?
- **Enabled**: When testing object appearance with lighting
- **Disabled**: When testing object geometry/materials only

### How often should I save presets?
Save lighting and camera setups whenever you achieve a look you want to reuse or might need to restore later.

---

## Tips & Tricks

### Quick camera creation from any view
Press Numpad 0 to enter camera view, adjust framing, then use CameraLAB "New from View" - instant perfect camera!

### Fast lighting iteration
Select All Lights, use Quick Multiply ×2 or ÷2 to quickly test brighter/darker overall lighting.

### Isolate and render
Select hero objects > Hide Unselected > Render Selection > Fast preview of just those objects.

### Multi-camera batch test
Enable all cameras > Viewport Render Mode ON > Frame All > Quick test render from every camera angle.

### Color temperature workflow
Use Kelvin slider instead of RGB picker for realistic lighting - 2700K for warm interiors, 6500K for daylight.

---

Still have questions? Check the troubleshooting page or refer to the module-specific documentation for detailed command explanations.
