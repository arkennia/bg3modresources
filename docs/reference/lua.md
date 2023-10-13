---
layout: default
title: Scripting
---

[Osiris Lua Docs](/bg3modresources/reference/luadocs/)  
Reference for the Osiris calls in Script Extender.

- [Aliases](#aliases)
  - [Equipment Slots](#equipment-slots)
  - [Type Aliases](#type-aliases)
  - [Enums](#enums)
    - [Deathtype](#deathtype)
    - [Tag Category](#tag-category)
    - [Armour Set](#armour-set)
    - [Crowd Behavior](#crowd-behavior)
    - [Splatter Type](#splatter-type)
    - [Quantity](#quantity)
    - [Tradable Type](#tradable-type)
    - [Equipment Slot](#equipment-slot)
    - [Unsheathed State](#unsheathed-state)
    - [Criticality Type](#criticality-type)
    - [Trade Mode](#trade-mode)


# Aliases

## Equipment Slots

```lua
EQUIPMENTSLOTNAME

"Amulet"|
"Boots"|
"Breast"|
"Cloak"|
"Gloves"|
"Helmet"|
"Melee Main Weapon"|
"Melee Offhand Weapon"|
"Ranged Main Weapon"|
"Ranged Offhand Weapon"|
"Ring"|
"Ring2"|
"Underwear"|
"VanityBody"|
"VanityBoots"
```

## Type Aliases

```lua
---@alias CHARACTER GUIDSTRING
---@alias ITEM GUIDSTRING
---@alias TRIGGER GUIDSTRING
---@alias SPLINE GUIDSTRING
---@alias LEVELTEMPLATE GUIDSTRING
---@alias DIALOGRESOURCE GUIDSTRING
---@alias EFFECTRESOURCE GUIDSTRING
---@alias VOICEBARKRESOURCE GUIDSTRING
---@alias ANIMATION GUIDSTRING
---@alias TAG GUIDSTRING
---@alias FLAG GUIDSTRING
---@alias FACTION GUIDSTRING
---@alias TIMELINERESOURCE GUIDSTRING
---@alias ROOT GUIDSTRING
---@alias CHARACTERROOT ROOT
---@alias ITEMROOT ROOT
---@alias PLATFORM GUIDSTRING
---@alias DISTURBANCEPROPERTY GUIDSTRING
---@alias SHAPESHIFTRULE GUIDSTRING
---@alias DIFFICULTYCLASS GUIDSTRING
---@alias GOLDREWARD GUIDSTRING
---@alias TUTORIALEVENT GUIDSTRING
---@alias DLC GUIDSTRING
---@alias RULESETMODIFIER GUIDSTRING
---@alias UNIFIEDTUTORIAL GUIDSTRING
```

## Enums

### Deathtype

```lua
---@alias DEATHTYPE
---| `0` # None
---| `1` # Acid
---| `2` # Chasm
---| `3` # DoT
---| `4` # Electrocution
---| `5` # Explode
---| `6` # Falling
---| `7` # Incinerate
---| `8` # KnockedDown
---| `9` # Lifetime
---| `10` # Necrotic
---| `11` # Physical
---| `12` # Psychic
---| `13` # Radiant
---| `14` # CinematicDeath
---| `15` # Cold
---| `16` # Disintegrate
```

### Tag Category

```lua
---@alias TAGCATEGORY
---| `0` # Undefined
---| `1` # Code
---| `2` # Dialog
---| `3` # Origin
---| `4` # Identity
---| `5` # Profession
---| `6` # Race
---| `7` # Race_Meta
---| `8` # Story
---| `9` # Voice
---| `10` # Background
---| `11` # Class
---| `12` # DialogHidden
---| `13` # Deity
---| `14` # Class_Deity
---| `15` # PlayerRace
---| `16` # CharacterSheet
---| `17` # SpellCondition
```

### Armour Set

```lua
---@alias ARMOURSET
---| `0` # Normal
---| `1` # Vanity
```

### Crowd Behavior

```lua
---@alias CROWDBEHAVIOUR
---| `0` # Cower
---| `1` # Disperse
---| `2` # Flee
```

### Splatter Type

```lua
---@alias SPLATTERTYPE
---| `1` # Blood
---| `2` # Bruise
---| `4` # Dirt
---| `8` # Sweat
```

### Quantity

```lua
---@alias QUANTITY
---| `0` # NONE
---| `1` # BARELY
---| `2` # SOME
---| `3` # HALF
---| `4` # LOTS
---| `5` # MOST
---| `6` # ALL
```

### Tradable Type

```lua
---@alias TRADABLETYPE
---| `0` # Default
---| `1` # Tradable
---| `2` # NonTradable
```

### Equipment Slot

```lua
---@alias EQUIPMENTSLOT
---| `0` # Helmet
---| `1` # Breast
---| `2` # Cloak
---| `3` # MeleeMainHand
---| `4` # MeleeOffHand
---| `5` # RangedMainHand
---| `6` # RangedOffHand
---| `7` # Ring
---| `8` # Underwear
---| `9` # Boots
---| `10` # Gloves
---| `11` # Amulet
---| `12` # Ring2
---| `13` # Wings
---| `14` # Horns
---| `15` # Overhead
---| `16` # MusicalInstrument
---| `17` # VanityBody
---| `18` # VanityBoots
```

### Unsheathed State

```lua
---@alias UNSHEATHSTATE
---| `0` # Instrument
---| `1` # Melee
---| `2` # Ranged
---| `3` # Sheathed
```

### Criticality Type

```lua
---@alias CRITICALITYTYPE
---| `0` # None
---| `1` # Success
---| `2` # Fail
```

### Trade Mode
```lua
---@alias TRADEMODE
---| `0` # Barter
---| `3` # Trade
---| `2` # Donate
---| `1` # Default
```