# LABsystem Documentation

Complete reference guide for LABsystem features and functionality.

## Table of Contents

1. [Introduction](#introduction)
2. [CameraLAB Features](#cameralab-features)
3. [RenderLAB Features](#renderlab-features)
4. [LightLAB Features](#lightlab-features)
5. [FrameLAB Features](#framelab-features)
6. [Interface Reference](#interface-reference)
7. [Workflows](#workflows)

## Introduction

LABsystem is a professional addon for Blender that provides four specialized modules for camera management, rendering automation, lighting control, and frame range management. Each module can be enabled or disabled independently based on your workflow needs.

### System Requirements

- Blender 3.0.0 or newer
- Operating System: Windows, macOS, or Linux
- No external dependencies required

### Module Overview

**CameraLAB** - Camera creation, switching, and resolution management
**RenderLAB** - Intelligent rendering with automatic settings backup
**LightLAB** - Centralized lighting control and batch operations
**FrameLAB** - Frame range presets and timeline management

## CameraLAB Features

### Camera Creation

**Create Camera from View**

Creates a new camera that exactly matches your current viewport position and angle.

Usage:
1. Position your 3D viewport to the desired view
2. Click "Create Camera from View"
3. New camera is created and automatically set as active

The camera inherits:
- Viewport position and rotation
- View angle and focal length
- Becomes the scene's active camera

**Quick Camera Creation**

Create standard cameras at world origin with predefined settings. Useful for starting new setups or creating placeholder cameras.

### Camera Switching

**Camera List**

Displays all cameras in the current scene. Click any camera name to:
- Make it the active scene camera
- Update the viewport to that camera's view
- See camera properties in the sidebar

**Cycle Cameras**

Navigate through all scene cameras in sequence.

- Next Camera: Moves to the next camera in the list
- Previous Camera: Moves to the previous camera
- Shows current position (e.g., "Camera 3 of 5")
- Loops back to start/end when reaching boundaries

**Set Active Camera**

Make any selected camera object the active scene camera. Select a camera in the outliner or 3D view, then use this function to activate it.

### Resolution Memory System

Save and recall different resolution settings for each camera. Each camera maintains its own independent library of resolution presets.

**Saving Presets**

1. Select a camera
2. Set your desired resolution in render settings
3. Click "Save Current Resolution"
4. Enter a name for the preset (e.g., "4K Final", "Web Preview")
5. Preset is saved to that camera

What gets saved:
- Resolution X and Y
- Resolution percentage
- Preset name for reference

**Loading Presets**

1. Select a camera with saved presets
2. Click on the preset name in the list
3. Resolution settings update immediately
4. Scene render settings change to match preset

**Managing Presets**

- View all presets for the selected camera
- Delete unwanted presets
- Rename by saving over existing name
- Each camera has separate preset storage

**Common Use Cases**

Different output formats:
- "4K Final": 3840×2160 for high-quality renders
- "HD Preview": 1920×1080 for quick reviews
- "Web Small": 1280×720 for online delivery
- "Instagram Square": 1080×1080 for social media
- "Print Large": 4000×3000 for physical prints

Multiple clients:
- "Client A Logo": 1920×1920
- "Client B Banner": 2560×1440
- "Client C Video": 1920×1080

Production stages:
- "Draft": 960×540 @ 50%
- "Review": 1920×1080 @ 75%
- "Final": 3840×2160 @ 100%

### Camera to View Operations

**View from Camera**

Aligns the 3D viewport to show exactly what the active camera sees. Useful for:
- Understanding camera composition
- Previewing the render without rendering
- Quick camera view reference

**Camera from View**

Moves the active camera to match your current viewport position. Use this to:
- Adjust camera position visually
- Fine-tune camera angles
- Set cameras by viewport navigation

### Camera Management

**Duplicate Camera**

Creates an exact copy of the selected camera including:
- Position and rotation
- Focal length and sensor settings
- All camera properties
- Note: Resolution presets are NOT copied

**Delete Camera**

Safely removes cameras from the scene with safeguards:
- Prevents deleting the last camera
- Warns before deleting active camera
- Removes from scene completely

## RenderLAB Features

### Viewport Rendering

**Render Visible Only**

Renders only objects that are visible in your viewport, ignoring hidden objects.

How it works:
1. Checks viewport visibility of all objects
2. Temporarily adjusts render visibility to match
3. Performs the render
4. Automatically restores original settings after completion

Benefits:
- Faster preview renders
- Test specific parts of scene
- Iterative workflow optimization
- No manual hide/unhide needed

**Viewport Animation Render**

Same functionality as viewport render but for animations. Renders entire frame range using only viewport-visible objects.

### Standard Rendering

**Enhanced Render Operations**

Standard render and animation operations with automatic backup:
- Creates backup before rendering
- Monitors render completion
- Restores settings automatically
- Handles cancellation gracefully

**Auto-Restore System**

Automatically saves and restores render settings:
- Object visibility states
- Render properties
- Camera settings
- Scene configuration

Triggers restoration on:
- Render completion
- Render cancellation
- Error conditions
- Manual restore command

**Manual Restore**

Force restoration of backed-up settings if automatic restore doesn't trigger. Safe to use multiple times.

### Render Settings Management

**Save Render Settings**

Export current render configuration to a file for reuse.

Saves:
- Resolution settings
- Output format and path
- Sampling and performance settings
- Film and color management
- All render engine settings

Usage:
1. Configure render settings as desired
2. Click "Save Render Settings"
3. Choose file location and name
4. Settings saved as JSON file

**Load Render Settings**

Import previously saved render configurations.

Usage:
1. Click "Load Render Settings"
2. Browse to settings file
3. Select and load
4. Settings applied immediately

**Common Configurations**

Quality tiers:
- "Draft": Low samples, fast render
- "Preview": Medium quality for review
- "Final": Full quality for delivery

Output types:
- "Video HD": 1920×1080, H.264, 30fps
- "Image Sequence": PNG, full quality
- "Web Optimized": Compressed, small file

Client specific:
- "Client A Specs": Custom requirements
- "Platform Standards": Social media specs

## LightLAB Features

### Light Manager

**Scene Light Overview**

Displays all lights in the current scene with controls for:
- Light name and type
- Enable/disable toggle
- Energy (intensity) value
- Color settings
- Quick selection

**Light Selection**

Click light names to:
- Select in 3D view
- Jump to light location
- View properties
- Multi-select with Shift

### Individual Light Control

**Energy Adjustment**

Control light intensity:
- Slider for quick adjustments
- Numeric input for precision
- Real-time viewport preview
- Per-light independent control

**Color Management**

Adjust light color:
- Color picker interface
- Temperature presets
- RGB values
- Real-time updates

**Light Properties**

Quick access to:
- Light type (Point, Sun, Spot, Area)
- Shadow settings
- Falloff and shape
- Special effects

### Batch Operations

**Multiple Light Selection**

Select multiple lights simultaneously:
- Shift+click for multi-select
- Affects all selected lights
- Visual selection indicator

**Batch Energy Control**

Adjust multiple lights at once:
- Multiplier system (0.5 = half intensity, 2.0 = double)
- Proportional adjustment
- Maintains relative intensities
- Affects only selected lights

**Batch Enable/Disable**

Toggle multiple lights:
- Enable all selected
- Disable all selected
- Useful for lighting layers

**Group Operations**

Organize lights by purpose:
- Key lights group
- Fill lights group
- Rim/accent lights group
- Environmental lights group

### Lighting Presets

**Standard Setups**

Pre-configured lighting arrangements:
- Three-point lighting
- Studio setup
- Product photography
- Outdoor simulation

**Apply Presets**

1. Click preset name
2. Lights automatically created
3. Positioned in standard layout
4. Adjust to your scene

**Customize After Application**

Presets are starting points:
- Move lights as needed
- Adjust energies
- Change colors
- Add or remove lights

## FrameLAB Features

### Frame Range Presets

**Save Frame Range**

Store current timeline range with a name.

Usage:
1. Set frame start and end
2. Click "Save Frame Range"
3. Enter name (e.g., "Shot_01", "Walk_Cycle")
4. Range stored for quick recall

What gets saved:
- Start frame number
- End frame number
- Preset name

**Load Frame Range**

Recall saved frame ranges instantly.

Usage:
1. Click preset name in list
2. Timeline updates to saved range
3. Start and end frames set
4. Ready to work on that segment

**Preset Management**

- View all saved presets
- Delete unwanted ranges
- Update by saving with same name
- Organize by shot or sequence

**Common Applications**

Shot breakdown:
- "Shot_01_Intro": 1-48
- "Shot_02_Action": 49-120
- "Shot_03_Closeup": 121-180
- "Shot_04_Outro": 181-240

Animation cycles:
- "Walk_Cycle": 1-24
- "Run_Cycle": 25-40
- "Idle": 1-60

Production phases:
- "Blocking": 1-240
- "Polish_Part1": 1-120
- "Polish_Part2": 121-240

### Quick Navigation

**Jump to Frame**

Move playhead to specific frame:
- Direct frame number input
- Jump to start/end
- Previous/next frame buttons

**Marker Navigation**

Jump between timeline markers:
- Next marker
- Previous marker
- First/last marker

### Timeline Control

**Playback Management**

Control animation playback:
- Play/pause shortcuts
- Loop section
- Speed control
- Scrubbing

**Range Display**

Current frame range information:
- Total frames
- Current position
- Duration in seconds

### Multi-Scene Coordination

**Sync Frame Ranges**

Copy frame range from one scene to another:
- Maintain consistency
- Shot coordination
- Multi-scene projects

## Interface Reference

### Sidebar Panel

Location: 3D View > Sidebar (N key) > LABsystem Tab

Contains:
- All enabled module panels
- Collapsible sections
- Context-sensitive controls
- Always accessible

### LABwindow

Popup window with quick access to all tools.

Open: Press F1 (default, customizable)

Features:
- Floating window
- Stays on top
- Drag to reposition
- Shows all modules
- Quick operations

Best for:
- Rapid access
- Single monitor setups
- Focused workflows
- Minimal UI switching

### LABmenu

Radial marking menu for gesture-based access.

Open: Press Ctrl+Alt+Shift+Numpad 0 (default, customizable)

Usage:
1. Press and hold shortcut
2. Move mouse to section
3. Click or release to activate

Features:
- Radial layout
- Gesture selection
- Context-aware
- Module sections

Best for:
- Production speed
- Muscle memory
- Minimal distraction
- Expert users

### Customization

**Module Toggle**

Enable or disable modules:
1. Edit > Preferences > Add-ons
2. Find LABsystem
3. Expand preferences
4. Check/uncheck modules
5. Changes apply immediately

**Keyboard Shortcuts**

Customize access keys:
1. Open addon preferences
2. Find shortcut settings
3. Click shortcut field
4. Press desired keys
5. Confirm and test

## Workflows

### Architectural Visualization

**Setup**
1. Create cameras for each room/angle
2. Save resolution presets per camera:
   - "Client Preview": 1920×1080
   - "Final Print": 4000×3000
   - "Web Gallery": 2560×1440
3. Configure lighting per space
4. Save render settings per quality tier

**Daily Workflow**
1. Switch between cameras with camera list
2. Load appropriate resolution preset
3. Use viewport render for quick previews
4. Hide unnecessary objects in viewport
5. Render visible only for faster iterations
6. Load "Final" settings for delivery

**Client Review**
1. Cycle through cameras
2. Load "Client Preview" preset
3. Quick renders for presentation
4. Adjust lighting with batch controls
5. Switch to final resolution for approvals

### Animation Production

**Shot Setup**
1. Create one camera per shot
2. Name cameras descriptively (CAM_Shot01_Wide)
3. Save frame ranges:
   - "Shot_01": 1-48
   - "Shot_02": 49-120
   - "Shot_03": 121-180
4. Configure lighting per shot

**Animation Workflow**
1. Load frame range for current shot
2. Switch to shot camera
3. Animate and preview
4. Use viewport render to test visibility
5. Move to next shot, load its range
6. Consistent render settings across shots

**Rendering**
1. Load "Preview" settings for dailies
2. Render animation per shot
3. Auto-restore handles cleanup
4. Load "Final" for delivery
5. Batch render all shots

### Product Visualization

**Camera Setup**
1. Create multiple angle cameras:
   - Hero shot
   - Detail closeups
   - 360 turntable
2. Save resolutions:
   - "Web 360": 800×800
   - "Print Detail": 3000×3000
   - "Video HD": 1920×1080

**Lighting Variations**
1. Apply lighting preset (product photography)
2. Save as base configuration
3. Create variations with batch energy
4. Test with viewport render

**Multiple Products**
1. Save render settings per product
2. Load settings when switching
3. Use same camera setup
4. Consistent output quality

### VFX and Compositing

**Pass Management**
1. Save render settings per pass:
   - Beauty pass
   - Shadow pass
   - Reflection pass
   - Matte pass
2. Quick load between passes
3. Viewport render for masks

**Shot Coordination**
1. Save frame ranges per element
2. Sync ranges across scenes
3. Coordinate camera positions
4. Consistent timing

**Multi-Scene Projects**
1. Save settings per scene type
2. Load configurations as needed
3. Maintain consistency
4. Organized workflows

### Tips for All Workflows

**Organization**
- Name cameras descriptively
- Use consistent resolution preset names
- Save render settings early
- Document special configurations

**Efficiency**
- Use viewport render for iterations
- Batch operations for similar tasks
- Keyboard shortcuts for speed
- Minimize manual adjustments

**Quality Control**
- Preview settings for testing
- Final settings for delivery
- Save configurations before changes
- Use auto-restore as safety net

**Collaboration**
- Share render settings files
- Document preset naming conventions
- Consistent camera naming
- Clear frame range labels

## Getting Support

**Console Messages**

LABsystem provides detailed console output:
- Success confirmations
- Warning messages
- Error information
- Operation status

View console: Window > Toggle System Console (Windows)

**Common Solutions**

Module not appearing:
- Check if enabled in preferences
- Verify Blender version compatibility
- Restart Blender if needed

Settings not saving:
- Ensure write permissions
- Check file paths
- Save Blender preferences

Operations not working:
- Verify correct context (camera selected, etc.)
- Check console for error messages
- Review operation requirements

**Feedback**

Provide feedback through:
- Addon preferences feedback system
- Include console output for issues
- Describe steps to reproduce problems
- Suggest improvements

LABsystem is designed to streamline production workflows while maintaining flexibility for different project types and user preferences.