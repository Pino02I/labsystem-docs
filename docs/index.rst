LABsystem Documentation
=======================

**LABsystem** is a professional camera and render ecosystem for Blender 4.2+
that turns the 3D viewport into a single cockpit for camera management,
lighting, render visibility, sequence rendering, and HDRI environments.

Five modular sub-systems work together — and any of them can be disabled
independently from the addon preferences:

* **CameraLAB** — camera creation, navigation, resolution memory, depth-of-field, alignment tools.
* **LightLAB** — per-camera light assignment so each shot has its own lighting setup.
* **RenderLAB** — selective render visibility, lights/objects assigned to specific cameras, viewport-render presets.
* **FrameLAB** — multi-camera sequence rendering with one click.
* **WorldLAB** — per-camera HDRI / world environment override.

Two universal entry points sit on top of the modules:

* **LABwindow** (default ``F1``) — a tabbed popup with quick controls for every module.
* **LABmenu** (default ``Ctrl+Alt+Shift+Numpad 0``) — a radial pie menu with gesture-based shortcuts.

Every persistent control is also available in the 3D Viewport Sidebar
(``N`` key → **LABsystem** category).

This site is the reference for **LABsystem v1.0.0**.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   introduction
   installation
   quick-start
   interface

.. toctree::
   :maxdepth: 2
   :caption: Modules

   cameralab
   lightlab
   renderlab
   framelab
   worldlab

.. toctree::
   :maxdepth: 2
   :caption: Universal Tools

   labwindow
   labmenu
   hotkeys
   preferences

.. toctree::
   :maxdepth: 1
   :caption: Support

   faq
   troubleshooting
   changelog

Indices
=======

* :ref:`genindex`
* :ref:`search`
