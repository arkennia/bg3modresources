---
layout: default
title: Recoloring Vanilla Weapons Tutorial
---

# Recoloring Vanilla Weapons
Below is a guide for changing the textures of vanilla weapons. I'll do my best to include as much information as possible, but if you get stuck, head on over to #bg3-mods-general in the Larian Studios Discord server. Even if I'm not around, they should be able to answer any questions.  
  
__I will be using the model of the Glaive +2 item as the basis of this tutorial, however the process will be almost the same for whichever weapon you choose. The name of my mod will be Glaive Revamped, but of course substitute that for the name of your mod.__

## Setting Up Your Workspace
For the tutorial you will need at a minimum:  
* A text editor
* Photo editing tools(I will be using GIMP)
* The modders' multitool
* Converter App  
  
Links to the tools can be found on [here](/bg3modresources/creating/#tools)

Also you will need to create a specific folder structure. I have released a python script that can generate a basic structure, but I will also write it out here.

```
<ModName>  
├───Generated
│   └───Public  
│       └───Shared  
│           └───Assets  
│               └───Weapons   
│  
├───Localization
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

## How to Generate new UUIDs and Handles

Before we really get into the creation of the mod, the first thing that you should know how to do is creating new UUIDs and handles.

1. Open up the Modders Multitool, and you should see a box that looks likes this:  
   ![uuids](../../images/recoloring/uuids.png)
2. To generate a new UUID, simply click the Generate button, and then click inside the box. It will copy the UUID to the ckeyboard. To generate handles, simply check the Handle box and repeat the same process as with UUIDs.  
    *Note: Make sure to only have the Handle box checked when generating handles for Localization.*

## Meta.Lsx

The very first file to edit will me the `meta.lsx` file inside of the folder `Glaive_Revamped\Mods\Glaive_Revamped\meta.lsx`. This is where the general information about your mod is stored. Here are the contents of the file:  
```xml
<?xml version="1.0" encoding="UTF-8"?>
    <save>
    <version major="4" minor="0" revision="9" build="331"/>
    <region id="Config">
        <node id="root">
            <children>
                <node id="Dependencies"/>
                    <node id="ModuleInfo">
                        <attribute id="Author" type="LSWString" value=""/>  CHANGE THIS
                        <attribute id="CharacterCreationLevelName" type="FixedString" value=""/>
                        <attribute id="Description" type="LSWString" value=""/> CHANGE THIS
                        <attribute id="Folder" type="LSWString" value=""/>  CHANGE THIS
                        <attribute id="GMTemplate" type="FixedString" value=""/>
                        <attribute id="LobbyLevelName" type="FixedString" value=""/>
                        <attribute id="MD5" type="LSString" value=""/>
                        <attribute id="MainMenuBackgroundVideo" type="FixedString" value=""/>
                        <attribute id="MenuLevelName" type="FixedString" value=""/>
                        <attribute id="Name" type="FixedString" value=""/>  CHANGE THIS
                        <attribute id="NumPlayers" type="uint8" value="4"/>
                        <attribute id="PhotoBooth" type="FixedString" value=""/>
                        <attribute id="StartupLevelName" type="FixedString" value=""/>
                        <attribute id="Tags" type="LSWString" value=""/>
                        <attribute id="Type" type="FixedString" value="Add-on"/>
                        <attribute id="UUID" type="FixedString" value=""/>
                        <attribute id="Version64" type="int64" value="36028797018963968"/>
                        <children>
                            <node id="PublishVersion">
                                <attribute id="Version64" type="int64" value="36028797018963968"/>
                            </node>
                            <node id="Scripts"/>
                            <node id="TargetModes">
                                <children>
                                    <node id="Target">
                                        <attribute id="Object" type="FixedString" value="Story"/>
                                    </node>
                                </children>
                            </node>
                        </children>
                    </node>
                </children>
            </node>
        </region>
    </save>
```

We will make the follow changes to this:
1. Change the value of the Author attribute to your name, in my case I'll set it to Faane.
2. Change the value of Description to whatever you want to description to be.
3. Make sure the folder is set to the name of your folder. Here it will be `Glaive_Revamped`. 
   - Make sure there are no spaces/special characters apart from _.
4. Set the name to the name of your mod, so `Glaive Revamped.`
5. Create a UUID using the multitool and paste it into the value field for UUID.
6. The only other field you might change in this file is Version64, which changes the version of the mod. There is a utility in the multitool for figuring out the number to put here, but know for now that it is set to `1.0.0.0`.  
  
You should now have a `meta.lsx` file that has contents similiar to this:  
```xml
<attribute id="Author" type="LSWString" value="Faane"/>
<attribute id="CharacterCreationLevelName" type="FixedString" value=""/>
<attribute id="Description" type="LSWString" value="A recolored version of Glaive +2"/>
<attribute id="Folder" type="LSWString" value="Glaive_Revamped"/>
<attribute id="GMTemplate" type="FixedString" value=""/>
<attribute id="LobbyLevelName" type="FixedString" value=""/>
<attribute id="MD5" type="LSString" value=""/>
<attribute id="MainMenuBackgroundVideo" type="FixedString" value=""/>
<attribute id="MenuLevelName" type="FixedString" value=""/>
<attribute id="Name" type="FixedString" value="Glaive Revamped"/>
<attribute id="NumPlayers" type="uint8" value="4"/>
<attribute id="PhotoBooth" type="FixedString" value=""/>
<attribute id="StartupLevelName" type="FixedString" value=""/>
<attribute id="Tags" type="LSWString" value=""/>
<attribute id="Type" type="FixedString" value="Add-on"/>
<attribute id="UUID" type="FixedString" value="873d534e-8168-459a-b140-8e448d356bf1"/>
<attribute id="Version64" type="int64" value="36028797018963968"/>
```

This file is done, and you can more or less forget about it for the duration of this tutorial.

## Localization File

Next step is to set up your localization file. This is located at: `Glaive_Revamped\Localization\English\Glaive_Revamped.loca.xml`.

The layout of this file is as follows:

```xml
<?xml version="1.0" encoding="utf-8"?>
<contentList>
	<content contentuid="" version="1"></content>
	<content contentuid="" version="1"></content>
</contentList>
```

Each line in this file will be some sort of text used in your mod. In your case, the first line will be the name of the item, and the second will be the description that shows in the tooltip.

1. Generate a handle for each `contentuid` field.
2. Place the text for the name and description between the opening and closing content tags.
  
Your file should look something like this:
```xml
<?xml version="1.0" encoding="utf-8"?>
<contentList>
	<content contentuid="hfc497768g1352g4f5agacbegdd8fcf52e613" version="1">My New Glaive</content>
	<content contentuid="hdd52a424gaeeag4cedg8f43gba7eed9a8e13" version="1">A recolored Glaive.</content>
</contentList>
```
  
Save the file, but keep it open, as we will need the handles we generated in the next step.

## RootTemplate Creation

The RootTemplate is file that ties all of your mod together. If your mod isn't working, 75% of the time it is an issue with the RootTemplate. 

The file will start out looking something like this:  
```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
    <version major="4" minor="0" revision="9" build="328" lslib_meta="v1,bswap_guids" />
    <region id="Templates">
        <node id="Templates">
            <children>
                <node id="GameObjects">
                    <attribute id="CanShootThrough" type="bool" value="True" />
                    <attribute id="Description" type="TranslatedString" handle="" version="1" /> Handle from localization file.
                    <attribute id="DisplayName" type="TranslatedString" handle="" version="1" /> Handle from localization file.
                    <attribute id="EquipmentTypeID" type="guid" value="" />
                    <attribute id="Flag" type="int64" value="0" />
                    <attribute id="Icon" type="FixedString" value="<Icon_Name>" />
                    <attribute id="IsInspector" type="bool" value="True" />
                    <attribute id="LevelName" type="FixedString" value="" />
                    <attribute id="LevelOverride" type="int64" value="-1" />
                    <attribute id="MapKey" type="FixedString" value="" /> Generate new UUID.
                    <attribute id="Name" type="LSString" value="" />
                    <attribute id="ParentTemplateId" type="FixedString" value="" />
                    <attribute id="PhysicsTemplate" type="FixedString" value="" />
                    <attribute id="Race" type="int8" value="0" />
                    <attribute id="ReadinessFlags" type="uint32" value="144" />
                    <attribute id="Stats" type="FixedString" value="" />
                    <attribute id="Tooltip" type="uint8" value="2" />
                    <attribute id="Type" type="FixedString" value="item" />
                    <attribute id="VisualTemplate" type="FixedString" value="" />
                    <attribute id="WalkThrough" type="bool" value="True" />
                    <attribute id="_OriginalFileVersion_" type="int64" value="144115188075855912" />
                    <children>
                        <node id="GameMaster" />
                        <node id="OnDestroyActions">
                            <children>
                                <node id="Action">
                                    <attribute id="ActionType" type="int64" value="26" />
                                    <children>
                                        <node id="Attributes">
                                            <attribute id="ActivateSoundEvent" type="FixedString" value="3ea82655-5140-4287-9ab8-794559f182d3" />
                                            <attribute id="Animation" type="FixedString" value="" />
                                            <attribute id="PlayOnHUD" type="bool" value="False" />
                                        </node>
                                    </children>
                                </node>
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
```

We can fill out some of the basic information here, and generate our UUID, but a lot of the information here will actually come from the game files. It is located at `Glaive_Revamped\Public\Glaive_Revamped\RootTemplates\merged.lsf.lsx`. The name and extension is important here, so make sure your's looks the same.
### Basic Information
1. Copy and paste the handles into the approriate areas of the template for DisplayName and Description.
2. Go to the multitool, and making sure the Handle box is *unchecked* generate a new UUID and paste it into the value for `MapKey`. This is the UUID you will use if you want to spawn the weapon into the game using the console.
3. Put a name for the item into the value for Name. This needs to have no spaces and consist of only letters. It is best to pick something to prefix it with to help make sure it is unique. I personally prefix all of mine with `FAA` but you can choose what works for you. I will be naming my item `FAA_Glaive_Revamped`.
4. Paste the value you used for name into the value for Stats.
   
Now my file will have these changes:  
```xml
<attribute id="CanShootThrough" type="bool" value="True" />
<attribute id="Description" type="TranslatedString" handle="hdd52a424gaeeag4cedg8f43gba7eed9a8e13" version="1" /> 
<attribute id="DisplayName" type="TranslatedString" handle="hfc497768g1352g4f5agacbegdd8fcf52e613" version="1" /> 
<attribute id="EquipmentTypeID" type="guid" value="" />
<attribute id="Flag" type="int64" value="0" />
<attribute id="Icon" type="FixedString" value="" />
<attribute id="IsInspector" type="bool" value="True" />
<attribute id="LevelName" type="FixedString" value="" />
<attribute id="LevelOverride" type="int64" value="-1" />
<attribute id="MapKey" type="FixedString" value="a619eb76-475b-4f36-a4ef-542d931f05ec" />
<attribute id="Name" type="LSString" value="FAA_Glaive_Revamped" />
<attribute id="ParentTemplateId" type="FixedString" value="" />
<attribute id="PhysicsTemplate" type="FixedString" value="" />
<attribute id="Race" type="int8" value="0" />
<attribute id="ReadinessFlags" type="uint32" value="144" />
<attribute id="Stats" type="FixedString" value="FAA_Glaive_Revamped" />
<attribute id="Tooltip" type="uint8" value="2" />
<attribute id="Type" type="FixedString" value="item" />
<attribute id="VisualTemplate" type="FixedString" value="" />
<attribute id="WalkThrough" type="bool" value="True" />
<attribute id="_OriginalFileVersion_" type="int64" value="144115188075855912" />
```
### ParentTemplateID, PhysicsTemplate, EquipmentTypeID and Icon

The next step of the process are locating some key pieces of information:
* ParentTemplateID
* PhysicsTEmplate
* EquipmentTypeID
* Icon  
*We will be using a vanilla icon here, which won't reflect our changes. Creating a new icon is beyond the scope of this tutorial, but there is a guide linked on this website if you wish to do that.*  

To find these pieces of information, open up the Multitool. Click the "Search Index" button and let it do its thing. It may take some time, so this is a good time to get up and stretch your legs. When it finishes it will open up a window, but close that as we will be using another function at this point.

1. With your Multitool open, go to `Utlities -> Game Object Explorer -> Open`. It will take a few moments to load everything here, so be patient.
2. Once it finishes, you should have a window that looks like this:
![explorer](../../images/recoloring/explorer.png)
3. In the drop down, select `item` as the game object type. In the search field, put in the item you're looking for. In my case it will be "Glaive". click through the menu's until you find the item you're looking for. I want the Glaive +2, so I selected `WPN_HUM_Glaive_A_2`. You should get something like this:
![glaive](../../images/recoloring/glaive.png)
4. Click the "Attributes" tab on the right, see more information regarding the weapon. We can find the following pieces: 
    * ParentTemplateID: `bc1c2a84-27f5-46e4-b4b4-0f5ca534469c`  
    * PhysicsTemplate: `5a6acc22-4359-0d52-0a08-a6ad2fb16f21`
    * EquipmentTypeID: `5e004b79-461d-4617-bb0f-eef0e0ae1232`
    * Icon: `Item_WPN_HUM_Glaive_A_2`
*Note: This is the `MapKey` for the Glaive here, because we want to make something based on this item, so we will inherit from it by setting it as our ParentTemplateID.*

With these pieces of information, go back to the Roottemplate(merged.lsf.lsx) and edit the apporiate fields:
```xml
...
<attribute id="EquipmentTypeID" type="guid" value="5e004b79-461d-4617-bb0f-eef0e0ae1232" />
...
<attribute id="Icon" type="FixedString" value="Item_WPN_HUM_Glaive_A_2" />
...
<attribute id="ParentTemplateId" type="FixedString" value="bc1c2a84-27f5-46e4-b4b4-0f5ca534469c" />
<attribute id="PhysicsTemplate" type="FixedString" value="5a6acc22-4359-0d52-0a08-a6ad2fb16f21" />
```

### Notes on VisualTemplate
Now we have all the pieces in our RootTemplate set except for `VisualTemplate`. This defines the model and textures that will be used by the weapon, which is what we will have to create for our edits. The VisualTemplate id for the glaive is `4c829229-bff7-4d31-4d35-f07d54deb9b0`. Note this down, but don't insert it into your RootTemplate.  
*Note: If for your particular weapon certain fields are missing, go up the tree in the Object explorer until you find the values you need. A lot of times, they are inherited from the ParentTemplate, so you need to go find that to get the information you need*

We will come back around to the VisualTemplate in a later section, next we will create the stats for the weapon.

## Stats

Next we will create the stats for the new weapon. This is a will go into `Weapon.txt` which will be placed at: `Glaive_Revamped\Public\Glaive_Revamped\Stats\Generated\Data\Weapon.txt`.

This is the entry for the Glaive at its most basic:
```
new entry "FAA_Glaive_Revamped"
type "Weapon"
using "WPN_Glaive_2"
data "RootTemplate" ""
```

The first line is for the name of the item, which must match the name in your RootTemplate.  
for data "RootTemplate" this is where you need to go back into your RootTemplate and copy the `MapKey`.  
The using "WPN_Glaive_2" means that I want to use the values present inside that entry in the game files.  
*Note: Finding these can be somewhat tricky. You can use the Index Search and look for the MapKey of the item or unpack the game files. There's plenty of guides online about this, as well as the discord to ask if you need help.*  

The completed entry will look like this:

```
new entry "FAA_Glaive_Revamped"
type "Weapon"
using "WPN_Glaive_2"
data "RootTemplate" "a619eb76-475b-4f36-a4ef-542d931f05ec"
```

However I want to add some magic damage and a Weapon Enchantment to my weapon, and I want to define the properties(such as Heavy, Magic, Reach etc). So I will edit the entry to:
```
new entry "FAA_Glaive_Revamped"
type "Weapon"
using "WPN_Glaive_2"
data "RootTemplate" "a619eb76-475b-4f36-a4ef-542d931f05ec"
data "DefaultBoosts" "WeaponEnchantment(2);WeaponProperty(Magical);WeaponDamage(1d4, Thunder)"
data "Weapon Properties" "Heavy;Reach;Twohanded;Melee;Dippable;Magical"
```

More information about possible entries for this as well as how to add things like abilities and passives is beyond the scope of this guide. Just note that this is where you would do such things.

