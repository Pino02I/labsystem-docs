# Installation

LABsystem v1.0.0 is distributed as a Blender 4.2+ extension package
(`LABsystem 1.0.0.zip`). Installation takes about 30 seconds.

## Requirements

| Requirement       | Version                                           |
|-------------------|---------------------------------------------------|
| Blender           | 4.2.0 or newer                                    |
| Operating system  | Windows / macOS / Linux (any platform Blender supports) |
| Python            | Bundled with Blender — no separate install needed |
| Disk space        | Approximately 1 MB                                |
| Permissions       | None at runtime (no network, no filesystem access outside what Blender already requires) |

LABsystem uses only standard Blender Python APIs. No external dependencies
are downloaded or installed.

## Install via the Extensions panel (recommended)

1. Download `LABsystem 1.0.0.zip` from your purchase or distribution channel.
2. Open Blender 4.2+.
3. Go to **Edit → Preferences → Get Extensions** (or **Add-ons** in older 4.x builds).
4. Click the small **▾** dropdown in the top-right corner of the panel and choose **Install from Disk…**.
5. Navigate to `LABsystem 1.0.0.zip` and click **Install from Disk**.
6. Blender installs the extension and enables it automatically.

You should see a console line like:

```
LABsystem v1.0.0 registered (X/Y classes)
```

(The exact numbers depend on which modules are enabled — by default all five are.)

## Install via the legacy Add-ons panel

If your Blender 4.2 build still uses the legacy add-ons workflow:

1. Open **Edit → Preferences → Add-ons**.
2. Click **Install…** in the top-right.
3. Select `LABsystem 1.0.0.zip` and click **Install Add-on**.
4. In the add-on list, search for `LABsystem` and tick the checkbox to enable it.

## Verify installation

1. Open the 3D Viewport.
2. Press `N` to open the Sidebar.
3. Look for a tab labelled **LABsystem** along the right edge of the viewport.
4. Click it. You should see the **LABsystem v1.0.0** info panel at the top, then panels for CameraLAB, LightLAB, RenderLAB, FrameLAB, WorldLAB, and Hotkeys.

If the **LABsystem** tab is missing, see {doc}`troubleshooting`.

You can also test the universal entry points:

* Press `F1` — the **LABwindow** popup should appear.
* Press `Ctrl+Alt+Shift+Numpad 0` — the **LABmenu** radial pie should appear.

## Updating to a new version

LABsystem follows standard Blender extension update behaviour:

1. Open **Edit → Preferences → Get Extensions**.
2. Find LABsystem in the installed list.
3. Click **Update** if a newer version is available, or remove and re-install with the new ZIP.

User-stored data (per-camera resolution memory, per-camera light/object/world
assignments, hotkey customisations) is stored on the scene and on Blender
preferences — it survives addon updates.

## Uninstalling

1. Open **Edit → Preferences → Get Extensions** (or **Add-ons**).
2. Find LABsystem in the installed list.
3. Click **Remove** (or **Uninstall**).
4. Restart Blender.

After removal, scene-level LABsystem properties remain in your `.blend` files
but are simply ignored by Blender — they take negligible space and don't
affect anything.

## Disabling individual modules

You don't need to uninstall LABsystem to disable a module — open
**Edit → Preferences → Add-ons → LABsystem** and untick the checkboxes for
modules you don't want. The corresponding sidebar panels and hotkeys
disappear immediately. See {doc}`preferences` for details.

## Where things live on disk

LABsystem installs as a Blender extension under your Blender user folder:

* **Windows**: `%APPDATA%\Blender Foundation\Blender\4.x\extensions\…\labsystem\`
* **macOS**: `~/Library/Application Support/Blender/4.x/extensions/…/labsystem/`
* **Linux**: `~/.config/blender/4.x/extensions/…/labsystem/`

You normally don't need to touch these files — Blender manages them.

## Next steps

You're installed. Head to the {doc}`quick-start` to render your first
multi-camera shot in five minutes.
