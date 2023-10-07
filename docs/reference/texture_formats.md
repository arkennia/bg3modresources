From [BG3 Wiki](https://bg3.wiki/wiki/Guide:Texture_Formatting)

Normal Map Channels:

    Red - Nothing
    Green - Green
    Blue - Blue
    Alpha - Red

Physical Map Channels:

    Red - Metalness
    Green - Roughness
    Blue - AO
    Alpha - Nothing

Basecolor Map Channels:

    Red - Red
    Green - Green
    Blue - Blue
    Alpha - Nothing

Mask Map Channels:  
Check vanilla textures for whatever you're masking.  
These usually don't need an Alpha channel.

DDS Export Settings:

    Normal Map:
    BC3 DTX5

    Physical Map:
    BC1 DTX1

    Basecolor Map:
    BC1 DTX1


Mask Map:  
These again depend on the type of mask you're creating. I'll be collecting as much info for different mask maps here as I find.
BC5 Unsigned (Paint.NET) / BC5 ATI2 (GIMP) for Horn masks
BC7 RGBA 8bpp | Explicit alpha (Photoshop) / BC7 sRGB or BC7 Linear (Paint.NET) for Shared Scars MSK (thanks to aurebuen for the info)
