from argparse import ArgumentParser, ArgumentError
from templatefiles import metalsx, icon_itemslsx, icontexturebanklsx, visuallsx, roottemplatelsx
import os


def createFile(path: str, contents=None):
    open(path, "w+").close()


def createTemplate(path, text):
    with open(path, "w+") as file:
        file.writelines(text)


parser = ArgumentParser(
    "Template Generator",
    description="Generate a template for creating a mod in Baldur's Gate 3.",
)

parser.add_argument("name", help="the name of your mod.")

parser.add_argument("dest", default=".", help="the target destination.")

parser.add_argument(
    "-i", help="use this option if you will be adding icons.", action='store_true'
)

parser.add_argument(
    "-t", help="use this option if you will be adding textures.", action='store_true'
)

parser.add_argument(
    "-s", help="use this if you will be using script extender.", action='store_true'
)

args = parser.parse_args()

modname: str = args.name
folder = modname.replace(" ", "_")
dest: str = args.dest

if not os.path.isdir(args.dest):
    raise ArgumentError("dest", "Invalid destination.")

try:
    os.mkdir(os.path.join(dest, folder))
except FileExistsError:
    print(f"Folder already exists with name: {folder}.")
    exit()
except FileNotFoundError:
    print(f"Could not find destination directory: {dest}")
    exit()

os.chdir(os.path.join(dest, folder))

print(os.getcwd())

os.makedirs("./Localization/English")

os.makedirs(f"./Mods/{folder}")
createTemplate(f"./Mods/{folder}/meta.lsx", metalsx.template(modname, folder))

os.makedirs(f"./Public/{folder}")

if args.i is True:
    os.makedirs("./Public/Game/GUI/Assets/Tooltips/ItemIcons")
    os.makedirs(f"./Public/{folder}/Assets/Textures/Icons")
    os.makedirs(f"./Public/{folder}/Content/UI/[PAK]_UI")
    os.makedirs(f"./Public/{folder}/GUI/")
    createTemplate(f"./Public/{folder}/GUI/Icons_Items.lsx", icon_itemslsx.template())
    createTemplate(f"./Public/{folder}/Content/UI/[PAK]_UI/merged.lsf.lsx", icontexturebanklsx.template())

if args.t is True:
    os.makedirs(os.path.join(os.getcwd(), "Generated/Public/Shared/Assets"))
    os.makedirs(f"./Public/{folder}/Content/Assets/")
    createTemplate(f"./Public/{folder}/Content/Assets/templatevisuals.lsx", visuallsx.template())

if args.s is True:
    os.makedirs(f"./Mods/{folder}/ScriptExtender/Lua")
    createFile(f"./Mods/{folder}/ScriptExtender/Config.json")
    createFile(f"./Mods/{folder}/ScriptExtender/Lua/BootstrapServer.lua")
    createFile(f"./Mods/{folder}/ScriptExtender/Lua/BootstrapClient.lua")

os.mkdir(f"./Public/{folder}/RootTemplates")
os.makedirs(f"./Public/{folder}/Stats/Generated/Data")
createTemplate(f"./Public/{folder}/RootTemplates/merged.lsf.lsx", roottemplatelsx.template())
