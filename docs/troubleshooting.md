# Troubleshooting

Solutions to common issues.

## Installation Issues

**Addon doesn't appear after installation**
1. Make sure you installed the correct zip file
2. Check the addon is enabled (Edit > Preferences > Add-ons)
3. Search for "LABsystem" in addon list
4. Restart Blender

**Can't find LABsystem tab**
- Press N in 3D View to open sidebar
- Scroll down to find LABsystem tab
- Check modules are enabled in preferences

**Modules not showing**
- Go to Edit > Preferences > Add-ons > LABsystem
- Verify modules are enabled
- Click checkbox to enable
- Restart Blender if needed

---

## CameraLAB Issues

**Camera won't switch**
- Verify camera exists in scene (check Outliner)
- Make sure camera isn't hidden
- Try selecting camera manually first

**Resolution not changing**
- Confirm preset is saved
- Check correct camera is selected
- Try saving preset again
- Verify in render settings manually

**Preset not showing**
- Presets are per-camera, not global
- Make sure correct camera is selected
- Try refreshing panel (collapse/expand)

**Camera creation fails**
- Check you're in 3D View
- Verify viewport is in correct context
- Try different creation method

---

## RenderLAB Issues

**Settings not restoring**
- Check console for error messages (Window > Toggle System Console)
- Use "Restore Settings" button manually
- Verify backup was created (console shows confirmation)
- Restart Blender if problem persists

**Viewport render shows wrong objects**
- Verify objects are actually hidden in viewport
- Check collection visibility
- Try toggling viewport visibility
- Console shows what's being rendered

**Can't load settings file**
- Verify file exists and path is correct
- Check file permissions
- Ensure file is valid JSON format
- Try saving new file from working scene

**Nothing renders**
- Verify camera is set and active
- Check some objects are visible
- Look for render layer issues
- Console may show specific errors

---

## LightLAB Issues

**Lights not showing in list**
- Check lights exist in scene
- Verify lights aren't in hidden collections
- Refresh panel (collapse/expand)
- Check scene has lights

**Batch operations not working**
- Verify lights are actually selected
- Check console for error messages
- Try selecting lights manually
- Make sure values are reasonable

**Preset won't load**
- Verify file exists
- Check file permissions
- Ensure JSON format is valid
- Try creating new preset

---

## FrameLAB Issues

**Frame range not updating**
- Verify preset is saved
- Check timeline manually
- Try refreshing panel
- Console shows confirmation messages

**Markers not appearing**
- Check timeline is visible
- Verify marker was actually created
- Look in timeline for marker
- Try creating marker manually (M key)

---

## General Troubleshooting

**Check the Console**
LABsystem provides detailed feedback:
- Window > Toggle System Console (Windows)
- Shows confirmations and errors
- Helpful for diagnosing issues

**Module Crashes Blender**
1. Disable the problematic module
2. Edit > Preferences > Add-ons > LABsystem
3. Uncheck module
4. Report issue with details

**Weird Behavior After Update**
- Save your work
- Restart Blender
- Check preferences are correct
- Re-enable modules if needed

**Addon Stops Working**
1. Check Blender version compatibility (3.0+)
2. Verify addon is still enabled
3. Try disabling and re-enabling
4. Reinstall addon if necessary
5. Check console for error messages

---

## Getting Help

**Console Messages**
Always check console first - it provides real-time feedback about what LABsystem is doing.

**Before Reporting Issues**
1. Check this troubleshooting page
2. Verify Blender version (3.0+)
3. Check addon is enabled
4. Look at console messages
5. Try in a fresh scene

**What to Include When Reporting**
- Blender version
- LABsystem version
- Steps to reproduce issue
- Console error messages
- Description of expected vs actual behavior
