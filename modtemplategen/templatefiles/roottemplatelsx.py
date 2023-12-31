def template():
    return """<?xml version="1.0" encoding="utf-8"?>
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
</save>"""