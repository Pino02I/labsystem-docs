# LABsystem User Guide

Complete guide to using LABsystem for Blender.

## Table of Contents

1. [Getting Started](#getting-started)
2. [CameraLAB](#cameralab)
3. [RenderLAB](#renderlab)
4. [LightLAB](#lightlab)
5. [FrameLAB](#framelab)
6. [LABwindow & LABmenu](#labwindow--labmenu)
7. [Workflows & Tips](#workflows--tips)

## Getting Started

### First Time Setup

After installing LABsystem, follow these steps:

1. Open Blender and press `N` in the 3D View to open the sidebar
2. Look for the "LABsystem" tab
3. Go to `Edit > Preferences > Add-ons > LABsystem` to configure modules
4. Enable the modules you need (all enabled by default)
5. Customize keyboard shortcuts if desired

### Interface Access

LABsystem can be accessed in three ways:

**Sidebar Panel**
- Press `N` in 3D View
- Click on "LABsystem" tab
- All enabled modules appear as separate panels

**LABwindow (Quick Access)**
- Press `F1` (default shortcut)
- Floating window with all tools
- Convenient for quick operations

**LABmenu (Marking Menu)**
- Press `Ctrl+Alt+Shift+Numpad 0` (default)
- Radial menu for rapid access
- Ideal for production workflows

## CameraLAB

Professional camera management system.

### Creating Cameras

**Create Camera from View**
1. Position your 3D viewport to desired angle
2. Click "Create Camera from View" or use LABwindow
3. Camera is created matching your exact viewport position
4. Camera automatically becomes active scene camera

**Quick Camera Creation**
- Use the quick create buttons in CameraLAB panel
- Standard camera types available
- Cameras created at world origin

### Managing Cameras

**Switch Between Cameras**
- Click camera name in the camera list
- Use "Next Camera" / "Previous Camera" buttons
- Keyboard shortcuts (if configured)

**Cycle Cameras**
- Navigate through all scene cameras sequentially
- Forward or backward direction
- Shows camera position (e.g., 3/5)

**Set Active Camera**
1. Select a camera object in the outliner
2. Click "Set Selected as Camera"
3. That camera becomes the scene camera

### Resolution Memory System

Save and recall different resolution settings per camera.

**Saving Resolution Presets**
1. Select a camera
2. Set desired resolution in render properties
3. Click "Save Current Resolution"
4. Enter preset name (e.g., "4K", "Web", "Preview")
5. Resolution is now saved for this camera

**Loading Presets**
1. Select a camera with saved presets
2. Click on preset name in the list
3. Resolution instantly changes to saved values
4. Works independently per camera

**Managing Presets**
- Rename: Click preset, modify name, save again
- Delete: Select preset, click delete button
- Each camera has its own preset library

**Common Preset Examples**
- "4K Final": 3840×2160
- "HD Preview": 1920×1080
- "Web Small": 1280×720
- "Instagram": 1080×1080
- "Print High": 4000×3000

### Camera to View

Align viewport to match camera position or vice versa.

**Viewport to Camera**
- Moves viewport to show camera's view
- Helpful for understanding camera composition

**Camera to Viewport**
- Moves camera to match current viewport
- Great for adjusting camera position visually

### Advanced Operations

**Duplicate Camera**
- Creates exact copy of selected camera
- Includes all camera settings
- Does NOT copy resolution presets (intentional)

**Delete Camera**
- Safe camera deletion
- Prevents deleting last camera
- Confirmation for active cameras

**Camera Properties Quick Access**
- Focal length adjustment
- Depth of field settings
- Sensor size modifications
- All accessible from sidebar

## RenderLAB

Intelligent rendering system with auto-restore capabilities.

### Viewport Rendering

**Render Visible Only**
1. Set up your viewport (hide objects you don't want)
2. Click "Render Viewport"
3. Only viewport-visible objects will render
4. Settings automatically restore after render

**How It Works**
- Creates automatic backup of render visibility
- Sets `hide_render` based on viewport visibility
- Renders the image
- Restores original settings when done

**Best Practices**
- Use collections to organize objects
- Hide complex objects during preview renders
- Great for iterative workflows

### Animation Rendering

**Viewport Animation**
- Same as viewport render but for animations
- Processes entire frame range
- Auto-restore after completion

**Standard Animation**
- Normal animation render with auto-backup
- Safety net for long renders
- Original settings preserved

### Auto-Restore System

**What Gets Backed Up**
- Object render visibility (`hide_render`)
- Camera settings
- Scene properties
- Render settings

**When Restore Happens**
- After successful render completion
- When render is cancelled
- On error/crash (when possible)
- Manual restore available

**Manual Restore**
- Click "Restore Settings" button
- Use if auto-restore didn't trigger
- Safe to use multiple times

### Render Settings Management

**Save Render Settings**
1. Configure render settings as desired
2. Click "Save Render Settings"
3. Name your configuration
4. Settings saved to file

**Load Render Settings**
1. Click "Load Render Settings"
2. Select configuration file
3. Settings instantly applied

**Use Cases**
- Different quality levels (preview/final)
- Client-specific settings
- Platform-specific exports (web/print/video)

### Hotkey System

Customize keyboard shortcuts for common render operations.

**Available Shortcuts**
- Quick render
- Viewport render
- Animation render
- Settings save/load

**Setup**
1. Open addon preferences
2. Find RenderLAB section
3. Assign keys to operations
4. Test in 3D View

## LightLAB

Centralized lighting control and management.

### Light Manager

**Overview Panel**
- Shows all lights in scene
- Quick enable/disable toggles
- Energy adjustments
- Color modifications

**Light Selection**
- Click light name to select in scene
- Multi-select available (Shift+Click)
- Jump to light in viewport

### Batch Operations

**Adjust Multiple Lights**
1. Select lights in Light Manager
2. Use batch controls
3. Energy multiplier (e.g., 0.5 = half intensity)
4. Color temperature adjustments

**Light Groups**
- Organize lights by purpose
- Key lights, fill lights, rim lights
- Enable/disable entire groups

### Quick Setup

**Standard Lighting Presets**
- Three-point lighting
- Product photography setup
- Studio lighting
- Outdoor/HDRI combinations

**Apply Preset**
1. Click preset name
2. Lights automatically created
3. Positioned in standard configuration
4. Adjust to your needs

### Energy Management

**Global Light Control**
- Master intensity slider
- Affects all selected lights proportionally
- Useful for time-of-day adjustments

**Per-Light Control**
- Individual light energy
- Precise value entry
- Real-time viewport preview

## FrameLAB

Timeline and frame range management.

### Frame Range Presets

**Save Frame Range**
1. Set start and end frames
2. Click "Save Frame Range"
3. Name your range (e.g., "Shot_01", "Walk_Cycle")
4. Range saved for quick recall

**Load Frame Range**
1. Click preset name
2. Timeline updates instantly
3. Frame range set to saved values

**Use Cases**
- Different animation shots
- Multiple takes
- Scene breakdowns
- Shot versioning

### Quick Navigation

**Jump to Frame**
- Specific frame number entry
- Jump to start/end shortcuts
- Timeline marker navigation

**Frame Stepping**
- Forward/backward by frames
- Skip to keyframes
- Shot boundary navigation

### Timeline Control

**Playback Options**
- Play/pause shortcuts
- Loop regions
- Speed adjustments
- Range isolation

### Multi-Scene Coordination

**Sync Frame Ranges**
- Copy range from one scene to another
- Maintain consistency across shots
- Useful for camera switching

## LABwindow & LABmenu

### LABwindow (Popup)

**Opening LABwindow**
- Press `F1` (default)
- Or use menu: `Window > LABwindow`

**Features**
- Floating window with all tools
- Stays on top while working
- Quick access to common operations
- Drag to reposition

**Best For**
- Quick operations
- Single-monitor setups
- Focused workflows

### LABmenu (Marking Menu)

**Opening LABmenu**
- Press `Ctrl+Alt+Shift+Numpad 0` (default)

**How to Use**
1. Press and hold shortcut
2. Move mouse to desired section
3. Click or release to activate
4. Works like a pie menu

**Sections**
- Camera operations
- Render controls
- Light adjustments
- Frame navigation

**Best For**
- Production environments
- Speed-critical workflows
- Minimal UI distraction

## Workflows & Tips

### Architectural Visualization

**Multi-Camera Setup**
1. Create cameras for each room/view
2. Save resolution presets per camera:
   - "Client Preview": 1920×1080
   - "Final Print": 4000×3000
   - "Web Gallery": 2560×1440
3. Use viewport render for quick previews
4. Cycle through cameras during client review

**Lighting Workflow**
1. Start with LightLAB preset
2. Adjust energy with batch operations
3. Fine-tune individual lights
4. Save lighting state per camera view

### Animation Production

**Shot Management**
1. Create one camera per shot
2. Save frame ranges for each shot:
   - "Shot_01_Intro": 1-48
   - "Shot_02_Action": 49-120
   - "Shot_03_Close": 121-180
3. Quick switch between shots
4. Render animation per shot with viewport settings

**Iterative Rendering**
1. Hide complex objects during tests
2. Use viewport render for speed
3. Load "Preview" render settings
4. Switch to "Final" settings for delivery

### Product Visualization

**Turntable Setup**
1. Create camera with rotation constraint
2. Save multiple resolution presets:
   - "Web 360": 800×800
   - "Print High": 3000×3000
   - "Video HD": 1920×1080
3. Set up lighting preset
4. Use frame ranges for rotation angles

**Material Variations**
1. Save render settings per material version
2. Use same camera setup
3. Quick load/render workflow
4. Consistent output quality

### VFX and Compositing

**Pass Management**
1. Save render settings per pass type
2. Use viewport render for mask passes
3. Frame range presets for shot segments
4. Auto-restore prevents setting loss

**Multi-Scene Rendering**
1. Sync frame ranges across scenes
2. Coordinate camera positions
3. Batch render multiple setups
4. Settings preserved per scene

### Best Practices

**Camera Organization**
- Name cameras descriptively: "CAM_Room_Wide", "CAM_Product_Close"
- Use collections to group related cameras
- Delete unused cameras to avoid clutter

**Resolution Strategy**
- Create presets before starting project
- Use consistent naming across projects
- Set up client-specific presets early

**Render Settings**
- Save baseline settings immediately
- Create quality tiers (Draft/Preview/Final)
- Document custom settings in file names

**Lighting Management**
- Group lights by purpose
- Use descriptive names
- Save important configurations

### Keyboard Shortcut Tips

**Recommended Customizations**
- Camera cycling: Number pad keys
- Render operations: F-keys
- Frame navigation: Arrow keys
- Keep shortcuts consistent across projects

**Conflict Avoidance**
- Check existing Blender shortcuts
- Avoid system-level shortcuts
- Test in clean scene first

### Performance Tips

**Speed Up Workflow**
- Disable unused modules
- Use viewport render for iterations
- Create resolution presets for speed tiers
- Close LABwindow when not needed

**Large Scenes**
- Use collections for camera organization
- Batch operations instead of individual
- Save render settings to disk, not scene

### Troubleshooting

**Camera Issues**
- If camera won't switch: Check if camera exists in scene
- Resolution not changing: Verify preset is saved correctly
- Camera disappears: Check outliner, may be hidden

**Render Issues**
- Auto-restore not working: Check console for errors
- Settings not loading: Verify file path and permissions
- Viewport render slow: Reduce visible complexity

**Module Issues**
- Panel not showing: Check if module is enabled in preferences
- Operations greyed out: Verify correct context (camera selected, etc.)
- Shortcuts not working: Check for conflicts in keymap editor

### Quick Reference

**Common Operations**

| Task | Method |
|------|--------|
| Create camera from view | LABwindow > Create Camera from View |
| Switch cameras | Click camera name in list |
| Save resolution | Select camera > Save Current Resolution |
| Render visible only | RenderLAB > Render Viewport |
| Adjust multiple lights | LightLAB > Select lights > Batch controls |
| Save frame range | FrameLAB > Save Frame Range |

**Default Shortcuts**

| Action | Shortcut |
|--------|----------|
| Open LABwindow | F1 |
| Open LABmenu | Ctrl+Alt+Shift+Numpad 0 |

**Module Toggle**

All modules can be enabled/disabled in:
`Edit > Preferences > Add-ons > LABsystem`

Changes take effect immediately without restart.

## Getting Help

**Console Output**
- Open system console for detailed messages
- Error messages include troubleshooting hints
- Success confirmations show operation details

**Documentation**
- README.md: Feature overview
- INSTALLATION.md: Setup instructions
- This guide: Detailed usage

**Feedback**
- Use thumbs down in addon preferences
- Report issues with console output
- Suggest features through feedback system

LABsystem is designed to adapt to your workflow. Experiment with different combinations of modules and features to find what works best for your projects.