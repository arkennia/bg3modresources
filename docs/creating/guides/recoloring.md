---
layout: default
title: Recoloring Vanilla Weapons Tutorial
---

# Recoloring Vanilla Weapons
Below is a guide for changing the textures of vanilla weapons. I'll do my best to include as much information as possible, but if you get stuck, head on over to #bg3-mods-general in the Larian Studios Discord server. Even if I'm not around, they should be able to answer any questions.

## Setting Up Your Workspace
For the tutorial you will need at a minimum:  
* A text editor
* Photo editing tools(I will be using GIMP)
* The modders' multitool
* Converter App  
  
Links to the tools can be found on [here](/bg3modresources/creating/#tools)

Also you will need to create a specific folder structure. I have released a python script that can generate a basic structure, but I will also write it out here.

```
<ModName>                                                                                               ├───Generated                                                                                                           │   └───Public                                                                                                          │       └───Shared                                                                                                      │           └───Assets                                                                                                  │               └───Weapons                                                                                             │                                                                                       ├───Localization
│   └───English
├───Mods
│   └───<ModName>                                                                                             
└───Public
    └───<ModName>
        ├───Content
        │   └───Assets
        │       └───Weapons
        │           └───[PAK]_Weapons
        ├───RootTemplates
        └───Stats
            └───Generated
                └───Data
```
You don't need to create all of these now, but keep this in mind when following this guide. For now, create the Localization folder tree, the Mods/Modname folders, and Public/RootTemplates folders.

## Meta.lsx File

