---
layout: default
title: Template Generator
---
- [Template Generator](#template-generator)
  - [Getting the Generator](#getting-the-generator)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [Example Usage](#example-usage)


# Template Generator
A very basic mod workspace template generator written in python.

## Getting the Generator
Download or clone this repository  
`git clone git@github.com:arkennia/bg3modresources.git`

## Requirements
- [Python](https://www.python.org/downloads/)

## Usage
```
usage: Template Generator [-h] [-i] [-t] [-s] name dest


  name        the name of your mod.

options:
  -h, --help  show this help message and exit
  -i          use this option if you will be adding icons.
  -t          use this option if you will be adding textures.
  -s          use this if you will be using script extender.
```
  
dest is the folder you want it to create the template in.  
The -i option adds the folder and files needed for dealign with icons.  
The -t option adds *basic* folders/files for textures, obviously your specific use will likely need more folders and files.  
The -s option adds the basic files and folders for a mod that uses the script extender  

### Example Usage

`python templategen.py -its Template .`

Will create the following structure in the current directory.

```
TemplateMod
    ├───Generated
    │   └───Public
    │       └───Shared
    │           └───Assets
    ├───Localization
    │   └───English
    ├───Mods
    │   └───TemplateMod
    │       └───ScriptExtender
    │           └───Lua
    └───Public
        ├───Game
        │   └───GUI
        │       └───Assets
        │           └───Tooltips
        │               ├───Icons
        │               └───ItemIcons
        └───TemplateMod
            ├───Assets
            │   └───Textures
            │       └───Icons
            ├───Content
            │   ├───Assets
            │   └───UI
            │       └───[PAK]_UI
            ├───GUI
            ├───RootTemplates
            └───Stats
                └───Generated
                    └───Data
```