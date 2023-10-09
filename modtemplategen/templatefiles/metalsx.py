def template(modname: str, folder: str = None):
    if folder is None:
        folder = modname.replace(" ", "_")
    return f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
    <save>
    <version major=\"4\" minor=\"0\" revision=\"9\" build=\"331\"/>
    <region id=\"Config\">
        <node id=\"root\">
            <children>
                <node id=\"Dependencies\"/>
                    <node id=\"ModuleInfo\">
                        <attribute id=\"Author\" type=\"LSWString\" value=\"\"/>  CHANGE THIS
                        <attribute id=\"CharacterCreationLevelName\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"Description\" type=\"LSWString\" value=\"\"/> CHANGE THIS
                        <attribute id=\"Folder\" type=\"LSWString\" value=\"{folder}\"/>  CHANGE THIS
                        <attribute id=\"GMTemplate\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"LobbyLevelName\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"MD5\" type=\"LSString\" value=\"\"/>
                        <attribute id=\"MainMenuBackgroundVideo\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"MenuLevelName\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"Name\" type=\"FixedString\" value=\"{modname}\"/>  CHANGE THIS
                        <attribute id=\"NumPlayers\" type=\"uint8\" value=\"4\"/>
                        <attribute id=\"PhotoBooth\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"StartupLevelName\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"Tags\" type=\"LSWString\" value=\"\"/>
                        <attribute id=\"Type\" type=\"FixedString\" value=\"Add-on\"/>
                        <attribute id=\"UUID\" type=\"FixedString\" value=\"\"/>
                        <attribute id=\"Version64\" type=\"int64\" value=\"36028797018963968\"/>
                        <children>
                            <node id=\"PublishVersion\">
                                <attribute id=\"Version64\" type=\"int64\" value=\"36028797018963968\"/>
                            </node>
                            <node id=\"Scripts\"/>
                            <node id=\"TargetModes\">
                                <children>
                                    <node id=\"Target\">
                                        <attribute id=\"Object\" type=\"FixedString\" value=\"Story\"/>
                                    </node>
                                </children>
                            </node>
                        </children>
                    </node>
                </children>
            </node>
        </region>
    </save>"""
