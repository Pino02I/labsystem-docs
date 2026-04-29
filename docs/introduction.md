# Introduction

## What LABsystem is

LABsystem is a Blender 4.2+ addon that consolidates camera, lighting, render,
and environment workflows into one consistent interface. Instead of jumping
between scattered Blender panels for every operation — switching cameras,
setting resolution, isolating lights for a specific shot, rendering only
selected objects, sequencing multiple cameras, swapping HDRI environments —
LABsystem brings every control into a unified system organised around the
**camera** as the unit of work.

The addon is built around a simple idea: a camera is rarely just a viewpoint.
A camera is a *shot* — and a shot has its own resolution, its own lighting,
its own subject objects, its own world environment, its own depth-of-field.
LABsystem makes those associations explicit and one-click toggleable.

## Modular architecture

LABsystem is divided into five sub-modules that can be enabled or disabled
independently from the addon preferences. Each module is self-contained and
focused on one workflow domain:

**CameraLAB** handles everything about cameras themselves — creation,
navigation, resolution memory (each camera remembers its own width/height
preset), depth-of-field, focal length, alignment helpers, and import/export
of camera settings to JSON.

**LightLAB** introduces per-camera light assignment. You assign a set of lights
to each camera, and when that camera becomes active, only those lights stay
enabled. This makes lighting setups for multi-shot scenes trivially
manageable — no more manually toggling light visibility before every render.

**RenderLAB** gives you four render variants (viewport image, viewport
animation, selection image, selection animation) plus per-camera object
assignment. Just like LightLAB does for lights, RenderLAB lets you say
*"camera A renders these objects, camera B renders those"* without ever
touching the standard hide-render eye icons by hand.

**FrameLAB** turns the camera collection into a render queue. With one click
you can render an image (or animation) from every camera in the scene, or
only the selected ones, with a unified output folder structure. Cameras can
be enabled or disabled per-render without affecting their underlying state.

**WorldLAB** does the same per-camera trick for HDRI / world environments:
each camera can have its own world override, swapped automatically when the
camera becomes active.

## Two universal entry points

On top of the five modules sit two surfaces designed to keep you in flow:

**LABwindow** is a tabbed popup that opens with `F1` (configurable). It packs
the most-used controls of every module into a single 440-pixel-wide window
that you can summon from anywhere in the 3D viewport. Tabs at the top let
you switch between CameraLAB, RenderLAB, LightLAB, FrameLAB, and WorldLAB
in-place, without losing your place in the scene.

**LABmenu** is a radial pie menu that opens with `Ctrl+Alt+Shift+Numpad 0`
(also configurable). The center of the pie has four directional sub-pies
(CameraLAB, RenderLAB, LightLAB, FrameLAB), each containing 6–8 directional
operators for the most frequent actions. With muscle memory you can fire
common operations as gestures without ever looking at the screen.

Every control is also available in the 3D Viewport Sidebar — press `N`,
choose the **LABsystem** tab, and every panel sits there persistently.

## Who LABsystem is for

LABsystem targets Blender artists who routinely work with **multiple
cameras** in the same scene — product visualisation, architectural
visualisation, animation pre-production, motion design, photogrammetry
review, multi-angle reference renders, and similar workflows where the
"shot" is the natural unit of organisation.

If you've ever caught yourself naming objects `LIGHT_for_camera_2_only`
or building duplicate scenes just to swap an HDRI, LABsystem is built for you.

## What's next

* {doc}`installation` — install the addon and verify it loaded.
* {doc}`quick-start` — your first camera, your first per-camera light setup, your first multi-camera render.
* {doc}`interface` — a tour of where everything lives.
