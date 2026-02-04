# Tips & Workflows

Practical advice for getting the most from LABsystem.

## General Tips

**Start Simple**
- Enable only the modules you need
- Learn one module at a time
- Build complexity gradually

**Use Presets**
- Save common configurations
- Create a personal preset library
- Share presets between projects

**Check the Console**
- LABsystem provides detailed feedback in the console
- Window > Toggle System Console (Windows)
- Useful for troubleshooting

## CameraLAB Workflows

**Multi-Camera Projects**
```
1. Create all cameras first
2. Name them clearly (CAM_Wide, CAM_Close, etc.)
3. Save resolution presets for each
4. Switch and render as needed
```

**Resolution Strategy**
Save these standard presets for each camera:
- "Draft" - Quick testing (540p @ 50%)
- "Preview" - Client review (1080p @ 100%)
- "Final" - Delivery (4K @ 100%)

**Organize Cameras**
- Use collections for camera groups
- Keep similar cameras together
- Delete unused cameras regularly

## RenderLAB Workflows

**Quality Progression**
```
Stage 1: Draft settings + Viewport render = Very fast feedback
Stage 2: Preview settings + Selected objects = Medium quality
Stage 3: Final settings + Full scene = Production quality
```

**Settings Library**
Create and save these configurations:
- Draft (960×540, 32 samples)
- Preview (1920×1080, 128 samples)
- Final (3840×2160, 512 samples)
- Client-specific formats

**Save Before Experiments**
1. Save current settings
2. Try new things
3. Load saved settings if needed
4. Risk-free exploration

## LightLAB Workflows

**Scene Lighting Presets**
Save complete lighting setups:
- Day lighting
- Night lighting
- Overcast
- Studio setup

**Global Adjustments**
```
1. Select All Lights
2. Batch multiply energy
3. Quick scene-wide changes
```

**Organized Naming**
Use prefixes for lights:
- KEY_Light, FILL_Light, RIM_Light
- Easy to select by type
- Clear purpose

## FrameLAB Workflows

**Shot Management**
```
1. Plan shots with markers
2. Save range for each shot
3. Switch instantly between shots
4. Render shots individually
```

**Animation Segments**
Save ranges for:
- Individual shots
- Action sequences
- Test ranges
- Full animation

## Combined Workflows

**Complete Shot Setup**
```
1. [FrameLAB] Load shot frame range
2. [CameraLAB] Switch to shot camera
3. [CameraLAB] Load resolution preset
4. [RenderLAB] Load render settings
5. Render
```

**Quick Preview Workflow**
```
1. [CameraLAB] Position viewport, create camera from view
2. [RenderLAB] Load draft settings
3. [RenderLAB] Render viewport
4. Review and iterate
```

**Consistent Multi-Scene Project**
```
1. Set up first scene completely
2. [RenderLAB] Save render settings
3. [LightLAB] Save light setup
4. Switch to other scenes
5. Load saved presets for consistency
```

## Keyboard Shortcuts

**Essential Shortcuts**
- N - Open/close sidebar
- F1 - LABwindow (default, customizable)
- Ctrl+Alt+Shift+Numpad 0 - LABmenu (default, customizable)

**Customize in Preferences**
Edit > Preferences > Add-ons > LABsystem
- Set your preferred shortcuts
- Module-specific shortcuts available
- Make it match your workflow

## Performance Tips

**Viewport Rendering**
- Hide objects not in frame
- Use simpler materials for tests
- Temporarily disable heavy modifiers

**File Management**
- Keep preset files organized in project folder
- Use descriptive filenames
- Version important presets if needed

**Scene Organization**
- More cameras don't slow Blender down
- Delete unused cameras anyway (cleaner scene)
- Use collections to organize everything
