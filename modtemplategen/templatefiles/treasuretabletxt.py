def template():
    return """
new treasuretable "TUT_Chest_Potions"
CanMerge 1
new subtable "1,1"
object category "I_<Name_From_RootTemplate>",1,0,0,0,0,0,0,0
"""
