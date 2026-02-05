# LABsystem – Professional Camera, Lighting & Render Ecosystem for Blender

**The complete and modular solution to achieve cinematic images quickly and professionally.**

---

## 🎥 What is LABsystem?

LABsystem is a modular ecosystem for Blender that combines advanced tools for **Camera, Lighting, World/HDRI, Framing, and Rendering**, designed to speed up your workflow.

**Optimized workflow**: switch between cameras while maintaining all settings, each camera has its own lights and dedicated HDRI, render all cameras automatically while you continue working, and render only what you see in the viewport.

From composition to final shot, LABsystem gives you **complete control over visual language** with an intuitive interface accessible from the Sidebar.

---

## 🔥 Why is LABsystem different from other add-ons?

✔ **Modular** → use only the modules you need (CameraLAB, LightLAB, WorldLAB, FrameLAB, RenderLAB).  
✔ **Optimized workflow** → simplifies camera, lighting, HDRI, and rendering management.  
✔ **Intuitive** → clean and immediate interface accessible from the Sidebar, with LABwindow (F1) and LABmenu (marking menu).  
✔ **Plug & Play** → no complex configuration: install, activate, and you're ready to go.  
✔ **Non-destructive** → automatic memory of settings, everything always stays in place.  
✔ **Perfect for** 3D artists, designers, animators, archviz, automotive, and VFX.

---

## 📦 What's included in LABsystem?

### 🎥 CAMERALAB – Advanced camera management

**The problem**: switching between cameras means manually reconfiguring resolutions and settings every time.

**The solution**:

- **Resolution Memory System** → each camera automatically remembers its personal resolution
- **Multi-Camera Workflows** → manage unlimited cameras without ever losing a configuration
- **Innovative Align System** (experimental) → align cameras to targets with advanced real-time controls
  - Align at Target with interactive X/Y offsets
  - Rectangle Align for precise framing
  - Hero Shot for dynamic compositions
- **Import/Export Cameras** → save and share complete camera setups between projects
- **Camera Operators** → frame selected, from current view, walk/fly navigation
- **View Tools** → lock/unlock camera to view, set active from selected, DOF controls, sensors, focal length, lens shift

> **Note**: the align system will be further enhanced in upcoming updates with even more advanced features.

### 💡 LIGHTLAB – Lighting per camera

**The problem**: changing cameras means manually managing which lights are active.

**The solution**:

- **Camera-Light Assignment System** → each camera can have its own personal set of lights
- **Auto-Sync Lights** → when you change cameras, lights activate/deactivate automatically
- **Unified Light Management** → control all scene lights from a single interface
- **Light Collections** → organize lights into groups
- **Quick Controls** → visibility, intensity, color temperature
- **Batch Operations** → assign all selected lights to a camera with one click
- **Professional Workflow** → simulate real multi-camera setups with dedicated lighting

> **Coming soon**: professional lighting presets (3-point light, softbox, rimlight) and more

### 🌍 WORLDLAB – HDRI and World per camera

**The problem**: you want to use different HDRIs for each camera, but manually changing world shaders, strength, and rotation is slow and repetitive.

**The solution**:

- **Camera-World Assignment System** → each camera can have its own dedicated HDRI/World
- **Auto-Sync World** → when you change cameras, the world updates automatically in the viewport
- **Per-Camera Controls** → each camera has its own custom controls:
  - **Strength** (0-10) → HDRI intensity
  - **Rotation** (0-360°) → environment rotation
- **Import HDRI** → import HDRI files (.hdr, .exr, .jpg, .png) directly into the addon
- **Import/Export World (JSON)** → import and export complete world shader setups with all nodes
- **World Management** → create, duplicate, rename, delete world shaders
- **Real-time Viewport Update** → see changes immediately in the viewport

**Perfect use cases**:
- Archviz: day HDRI for exteriors, night HDRI for interiors
- Product: neutral studio HDRI, outdoor HDRI, dramatic HDRI
- Character: different environments for different angles

### 🖼️ FRAMELAB – Automatic multi-camera rendering

**The problem**: rendering multiple cameras means doing it manually one by one, impossible to continue working in the meantime.

**The solution**:

- **Batch Multi-Camera Rendering** → render one, several, or all cameras in automatic sequence
- **Automatic File Naming** → each render is automatically saved with the camera name
- **Background Rendering** → continue working while FrameLAB renders in the background
- **Output Path Management** → intelligent management of save paths
- **Animation Support** → render animations from multiple cameras
- **Camera Selection** → choose exactly which cameras to render
- **Non-blocking Operations** → modal system that doesn't block Blender
- **CameraLAB Integration** → complete synchronization with the camera management system

### 🚀 RENDERLAB – Fast viewport rendering

**The problem**: you want to render only what you see in the viewport without manually hiding hundreds of objects.

**The solution**:

- **Viewport Render** → render ONLY objects visible in the current viewport
- **Selected Objects Render** → render only selected objects
- **Auto-Restore System** → render visibility settings are automatically saved and restored
- **Animation Support** → render viewport or selected-only animations
- **Smart Visibility Management** → intelligent hide_render management for viewport and selections
- **No Manual Work** → no manual scene preparation, everything is automatic
- **Custom Hotkeys** → configurable shortcuts for blazing-fast workflows
- **Include/Exclude Lights** → optional control to include or exclude lights from rendering

**Perfect use cases**:
- Quick test render on a portion of the scene
- Lighting preview on specific objects
- Single asset rendering without manual preparation

---

## ⚡ Fast and powerful interface

### LABwindow (F1 - configurable)
**Professional floating window** that puts every tool at your fingertips:
- Zero menu diving – everything is visible and organized in tabs
- Panels for each module (CameraLAB, LightLAB, WorldLAB, FrameLAB, RenderLAB)
- Compact design that doesn't clutter the viewport
- Instant access with a single hotkey

### LABmenu (Ctrl+Alt+Shift+Numpad0 - configurable)
**Marking menu** pie-menu style for instant access:
- Most-used commands at your fingertips
- Perfect for fast workflows
- Ideal for tablet users
- Fully customizable

### Sidebar Integration
All panels are also accessible from the **Sidebar (N) → LABsystem** for native integration with Blender.

---

## 🧰 Key features (quick summary)

- **Modular ecosystem** Camera + Light + World/HDRI + Multi-Render + Viewport Render
- **Resolution Memory** – each camera remembers its settings
- **Camera-Light Assignment** – each camera has its personal lights
- **Camera-World Assignment** – each camera has its own HDRI with custom strength and rotation
- **Batch Multi-Camera Rendering** – render all cameras automatically
- **Viewport Rendering** – render only what you see
- **Import/Export Cameras** – share setups between projects
- **Auto-Restore System** – automatic configuration saving
- **LABwindow + LABmenu** – instant access with hotkeys
- **Sidebar Integration** – native panels in Blender's Sidebar
- **20,000+ lines of code** tested and production-ready
- **Experimental Align System** – continuously evolving

---

## 🎯 Perfect for

✅ **Architectural Visualization** – manage multiple angles, day/night HDRIs, automatic batch rendering  
✅ **Product Photography** – fast test renders with different HDRIs, automated final batch  
✅ **Animation Studios** – coordinate multi-camera setups with dedicated lighting and environments  
✅ **Freelance Artists** – maximize productivity on every project  
✅ **VFX Artists** – precise control and non-destructive workflow  
✅ **Motion Graphics** – fast viewport test renders and final batch  

---

## 🧑‍💻 Compatibility

- **Blender**: 3.0+
- **Operating System**: Windows, macOS, Linux
- **Dependencies**: no external libraries required
- **Render Engines**: Cycles, Eevee, Workbench

---

## 📥 Installation

1. Go to **Edit → Preferences → Add-ons**.
2. Click **Install…**.
3. Select `LABsystem_v1.0.0.zip`.
4. Activate **LABsystem** from the list.
5. Find it in the **Sidebar (N) → LABsystem**.
6. Press **F1** to open LABwindow.

**Optional configuration:**
- Go to **Preferences → Add-ons → LABsystem**
- Enable/disable the modules you prefer
- Customize hotkeys for LABwindow and LABmenu

---

## ❓ FAQ

**👉 Is it suitable for beginners?**  
Yes. The interface is simple and guided. Beginners will appreciate the logical organization, while professionals will leverage advanced features and automated workflows.

**👉 Can I use only some modules?**  
Absolutely. LABsystem is completely modular. You can enable/disable each individual module from preferences.

**👉 Is it useful for automotive, archviz, and character art?**  
Absolutely yes. Any pipeline using multiple cameras benefits enormously from LABsystem: architecture, product, characters, automotive, VFX, motion graphics.

**👉 Can I continue working while it renders?**  
Yes with FrameLAB! The batch rendering system is non-blocking, you can continue modeling while cameras are being rendered in the background.

**👉 What happens to my settings when I change cameras?**  
With CameraLAB each camera remembers its resolution. With LightLAB each camera automatically activates/deactivates its lights. With WorldLAB each camera applies its HDRI with custom strength and rotation. Everything is non-destructive.

**👉 Will there be updates?**  
Yes. LABsystem is in active development. The camera align system will be enhanced, professional lighting presets will be added, and much more. All future updates are **included for free**.

**👉 Does it work with Cycles and Eevee?**  
Yes, LABsystem works perfectly with both render engines (and Workbench too).

**👉 Can I customize the hotkeys?**  
Certainly. LABwindow and LABmenu have fully customizable hotkeys in the addon preferences.

**👉 Does it slow down Blender?**  
No. LABsystem is highly optimized. Operators are fast and efficient, designed for professional use.

**👉 Can I use it in commercial projects?**  
Yes. LABsystem is licensed for both personal and commercial use, with no restrictions.

---

## 💬 Support

Have questions or special needs? I respond within **24-48 hours** via **Superhive Inbox**.

---

## 🆕 Changelog

### v1.0.0 – Initial release

**CameraLAB:**
- ✅ Complete camera management system with automatic resolution memory
- ✅ Complete camera import/export
- ✅ Innovative align system (Align at Target, Rectangle Align, Hero Shot)
- ✅ Camera operators (frame selected, from view, walk/fly navigation)
- ✅ Complete view tools with DOF, sensors, focal length, lens shift

**LightLAB:**
- ✅ Camera-Light assignment system – each camera has its lights
- ✅ Auto-sync of lights when changing cameras
- ✅ Unified control of all scene lights
- ✅ Light collections and batch operations
- ✅ Quick controls for visibility and intensity

**WorldLAB:**
- ✅ Camera-World assignment system – each camera has its HDRI/World
- ✅ Auto-sync of world when changing cameras
- ✅ Per-camera Strength control (0-10)
- ✅ Per-camera Rotation control (0-360°)
- ✅ Direct HDRI import (.hdr, .exr, .jpg, .png)
- ✅ Complete Import/Export World (JSON) with all nodes
- ✅ Complete world management (create, duplicate, rename, delete)
- ✅ Real-time viewport update

**FrameLAB:**
- ✅ Automatic batch multi-camera rendering
- ✅ Render selected cameras or render all cameras
- ✅ Automatic file naming with camera name
- ✅ Animation support for multi-camera rendering
- ✅ Non-blocking system to continue working
- ✅ Intelligent output path management

**RenderLAB:**
- ✅ Viewport rendering – render only what you see
- ✅ Selected objects rendering
- ✅ Auto-restore system for visibility settings
- ✅ Animation support for viewport and selected
- ✅ Smart visibility management
- ✅ Configurable custom hotkeys

**Core System:**
- ✅ LABwindow (F1) – popup window for quick access
- ✅ LABmenu (marking menu) – instant command access
- ✅ Sidebar Integration – native panels in Sidebar (N)
- ✅ Complete modular system – enable/disable modules individually
- ✅ Professional and organized UI
- ✅ 20,000+ lines of production-tested code

---

## 🛒 Ready to optimize your workflow?

**Download LABsystem and take your workflow to the next level.**

With LABsystem you get:
- ✅ Each camera remembers everything automatically
- ✅ Lights sync with cameras
- ✅ HDRIs apply automatically per camera
- ✅ Automated multiple rendering in the background
- ✅ Instant viewport tests without preparation

**Buy now and receive:**
- ✅ All 5 LAB modules
- ✅ LABwindow + LABmenu + Sidebar Integration
- ✅ Complete documentation
- ✅ Free future updates
- ✅ Direct developer support
- ✅ Commercial license included

---

## 📊 Technical specifications

- **Name**: LABsystem v1.0.0
- **Author**: Giuseppe Iuliano
- **Category**: Camera / Rendering / Workflow / Productivity
- **Size**: <5MB
- **Format**: standard Blender .zip addon
- **Language**: Python (20,000+ lines)
- **License**: Personal and commercial use
- **Modules**: 5 (all independent and can be disabled)

---

## 🏷️ Tags

camera, render, lighting, world, hdri, workflow, productivity, professional, studio, multi-camera, batch-render, viewport-render, archviz, automotive, VFX, animation, pipeline, tools, management, non-destructive, automation, cinematography, environment

---

*LABsystem – The complete and modular solution for cinematic images.*
