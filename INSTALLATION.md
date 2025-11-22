# LABsystem Installation Guide

This guide will walk you through the installation process for LABsystem addon for Blender.



## Prerequisites

Before installing LABsystem, ensure you have:

- **Blender 3.0.0 or newer** installed on your system
- Basic familiarity with Blender's interface
- Administrator/user permissions to install addons



## Download

1. Download the latest version of LABsystem:
   - `LABsystem_v1_0_0.zip`

2. **Important**: Do NOT unzip the file. Blender requires the addon to be installed as a ZIP file.



## Installation Methods

### Method 1: Install via Preferences (Recommended)

This is the standard and most reliable method for installing Blender addons.

#### Step-by-Step Instructions:

1. **Open Blender**
   - Launch Blender 3.0 or newer

2. **Access Preferences**
   - Go to `Edit > Preferences` (or `Blender > Preferences` on macOS)
   - Alternatively, press `F4` and search for "Preferences"

3. **Navigate to Add-ons Section**
   - Click on the `Add-ons` tab in the left sidebar
   - You'll see a list of installed addons

4. **Install the Addon**
   - Click the `Install...` button at the top-right of the window
   - A file browser will open
   - Navigate to where you saved `LABsystem_v1_0_0.zip`
   - Select the ZIP file
   - Click `Install Add-on`

5. **Enable the Addon**
   - After installation, you'll automatically be brought to the addons list
   - The search will be filtered to show "LABsystem"
   - If not visible, type "LABsystem" in the search box at the top-right
   - Check the checkbox next to "Camera: LABsystem" to enable it

6. **Verify Installation**
   - You should see console output confirming successful registration
   - Check the 3D View sidebar (press `N`) for the LABsystem tab



### Method 2: Manual Installation (Advanced Users)

For users who prefer manual file management or need to install to a custom location.

#### Step-by-Step Instructions:

1. **Locate Blender's Addons Directory**

   The default paths are:

   - **Windows**: 
     ```
     C:\Users\[YourUsername]\AppData\Roaming\Blender Foundation\Blender\[Version]\scripts\addons\
     ```

   - **macOS**: 
     ```
     /Users/[YourUsername]/Library/Application Support/Blender/[Version]/scripts/addons/
     ```

   - **Linux**: 
     ```
     ~/.config/blender/[Version]/scripts/addons/
     ```

   Replace `[Version]` with your Blender version (e.g., `4.2`, `3.6`, etc.)

2. **Extract the Addon**
   - Unzip `LABsystem_v1_0_0.zip`
   - You should see a folder named `LABsystem`
   - This folder should contain `__init__.py` and various subfolders

3. **Copy to Addons Directory**
   - Copy the entire `LABsystem` folder into the addons directory
   - The final path should look like: `.../addons/LABsystem/__init__.py`

4. **Enable in Blender**
   - Open or restart Blender
   - Go to `Edit > Preferences > Add-ons`
   - Search for "LABsystem"
   - Enable the addon by checking the checkbox



## Post-Installation Configuration

After installing LABsystem, you can configure its modules and settings.

### 1. Access Addon Preferences

1. Go to `Edit > Preferences > Add-ons`
2. Search for "LABsystem"
3. Click the arrow to expand the addon preferences

### 2. Enable/Disable Modules

LABsystem uses a modular architecture. You can enable or disable individual modules:

- **📷 CameraLAB**: Camera management and resolution memory
- **🎬 RenderLAB**: Render automation and settings management
- **💡 LightLAB**: Lighting control and batch operations
- **🎯 FrameLAB**: Frame range and timeline management

**To toggle modules:**
- Simply check or uncheck the module checkbox
- Changes take effect immediately (no restart required)
- Disabled modules won't appear in the UI or use resources

### 3. Customize Keyboard Shortcuts

LABsystem provides two default shortcuts:

- **LABwindow**: `F1` (popup window with quick access)
- **LABmenu**: `Ctrl+Alt+Shift+Numpad 0` (marking menu)

**To customize:**
1. Expand addon preferences
2. Find the keyboard shortcuts section
3. Click on the shortcut field
4. Press your desired key combination
5. Click outside to confirm

### 4. Configure Auto-Save/Restore

RenderLAB includes auto-save and auto-restore features:

1. In addon preferences, locate the RenderLAB section
2. Enable/disable auto-save for render settings
3. Configure auto-restore behavior
4. Set default paths if needed



## Verify Installation

To confirm LABsystem is installed correctly:

### Visual Verification:

1. **Check Sidebar**
   - Open the 3D View
   - Press `N` to open the sidebar
   - Look for a "LABsystem" tab
   - You should see panels for enabled modules

2. **Test LABwindow**
   - Press `F1` (or your custom shortcut)
   - A popup window should appear with LABsystem tools

3. **Test LABmenu**
   - Press `Ctrl+Alt+Shift+Numpad 0` (or your custom shortcut)
   - A marking menu should appear

### Console Verification:

1. **Open System Console**
   - Windows: `Window > Toggle System Console`
   - macOS/Linux: Launch Blender from terminal

2. **Look for Success Messages**
   - You should see messages like:
     ```
     ======================================================================
     🚀 LABsystem v1.0 - REGISTRATION COMPLETE
     ======================================================================
     📍 Location: 3D View > Sidebar (N) > LABsystem
     🎯 LABwindow: F1 (configurable)
     🎛️ LABmenu: Ctrl+Alt+Shift+Numpad 0 (configurable)
     ======================================================================
     ```

3. **Check Module Status**
   - Console shows which modules are enabled:
     ```
     📦 Module Status:
        📷 CameraLAB: ✅ Enabled
        🎬 RenderLAB: ✅ Enabled
        💡 LightLAB: ✅ Enabled
        🎯 FrameLAB: ✅ Enabled
     ```



## Updating LABsystem

To update to a newer version:

1. **Remove Old Version** (if using manual installation)
   - Disable the addon in preferences
   - Delete the `LABsystem` folder from the addons directory
   - Restart Blender

2. **Install New Version**
   - Follow the installation steps above with the new ZIP file

3. **Note on Preferences Install**
   - If you installed via Preferences, you can simply install the new version
   - Blender will automatically overwrite the old version
   - Your settings should be preserved



## Uninstallation

To remove LABsystem from Blender:

### Via Preferences (Recommended):

1. Go to `Edit > Preferences > Add-ons`
2. Search for "LABsystem"
3. Click the arrow to expand the addon
4. Click the `Remove` button
5. Confirm the removal
6. Restart Blender (recommended)

### Manual Removal:

1. Disable the addon in preferences
2. Close Blender
3. Navigate to the addons directory (see Method 2 above)
4. Delete the `LABsystem` folder
5. Restart Blender



## Troubleshooting Installation

### "No module named 'LABsystem'" Error

**Cause**: Addon folder is not in the correct location or has incorrect structure.

**Solution**:
- Verify the folder structure: `addons/LABsystem/__init__.py` must exist
- Check that you copied the entire folder, not just its contents
- Ensure folder name is exactly "LABsystem" (case-sensitive on Linux/macOS)

### Addon Not Appearing in List

**Cause**: Installation path is incorrect or Blender cache issues.

**Solution**:
- Try installing via Preferences method instead of manual
- Refresh the addon list (search for it again)
- Restart Blender with `--factory-startup` flag to reset preferences (backup your settings first)

### Keyboard Shortcuts Not Working

**Cause**: Conflict with other addons or system shortcuts.

**Solution**:
- Check for conflicts in `Edit > Preferences > Keymap`
- Customize LABsystem shortcuts in addon preferences
- Ensure 3D View is the active editor when using shortcuts

### Modules Not Enabling

**Cause**: Dependency issues or corrupted installation.

**Solution**:
- Check console for error messages
- Reinstall the addon
- Enable modules one at a time to identify problematic modules
- Ensure Blender version is 3.0 or newer

### Console Errors During Installation

**Cause**: Various potential issues with Python dependencies or file permissions.

**Solution**:
- Copy the full error message from the console
- Check file permissions on the addons directory
- Ensure Blender has write access to user preferences
- Try running Blender as administrator (Windows) or with sudo (Linux) temporarily for installation



## Saving Preferences

After configuring LABsystem:

1. Blender saves addon preferences automatically
2. Your module enable/disable states persist across sessions
3. Keyboard shortcut customizations are saved
4. Per-module settings are preserved

**To ensure settings are saved**:
- Go to `Edit > Preferences`
- Click the hamburger menu (≡) at the bottom-left
- Select `Save Preferences`



## Support

If you encounter issues during installation:

1. **Check Console**: Most errors are reported in the System Console
2. **Verify Requirements**: Ensure Blender version compatibility
3. **Clean Install**: Try removing and reinstalling
4. **Documentation**: Refer to README.md for additional information
5. **Feedback**: Use the addon preferences feedback system



## Next Steps

After successful installation:

1. Read the [README.md](README.md) for feature overview
2. Experiment with each module in a test project
3. Customize keyboard shortcuts to your workflow
4. Configure module settings in addon preferences
5. Check [CHANGELOG.md](CHANGELOG.md) for version information



**Congratulations!** LABsystem is now installed and ready to enhance your Blender workflow.

Happy Blending! 
