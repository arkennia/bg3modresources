def template():
    return """<?xml version="1.0" encoding="utf-8"?>
<save>
    <version major="4" minor="0" revision="4" build="602" />
    <region id="MaterialBank">
        <node id="MaterialBank">
            <children>
            <node id="Resource">
                    <attribute id="DiffusionProfileUUID" type="FixedString" value="" />
                    <attribute id="ID" type="FixedString" value="" />
                    <attribute id="Localized" type="bool" value="False" />
                    <attribute id="MaterialType" type="uint8" value="4" />
                    <attribute id="Name" type="LSString" value="" />
                    <attribute id="SourceFile" type="LSString" value="Public/Shared/Assets/Materials/Base/Base.lsf" />
                    <attribute id="_OriginalFileVersion_" type="int64" value="144115196665790673" />
                    <children>
                        <node id="ScalarParameters">
                            <attribute id="Enabled" type="bool" value="False" />
                            <attribute id="ExportAsPreset" type="bool" value="False" />
                            <attribute id="GroupName" type="FixedString" value="" />
                            <attribute id="ParameterName" type="FixedString" value="SeeThroughEnabled" />
                            <attribute id="SkinnedDepth" type="uint32" value="0" />
                            <attribute id="SkinnedForward" type="uint32" value="0" />
                            <attribute id="SkinnedVelocity" type="uint32" value="0" />
                            <attribute id="StaticBake" type="uint32" value="0" />
                            <attribute id="StaticDepth" type="uint32" value="0" />
                            <attribute id="StaticForward" type="uint32" value="0" />
                            <attribute id="StaticInstancedDepth" type="uint32" value="0" />
                            <attribute id="StaticInstancedForward" type="uint32" value="0" />
                            <attribute id="StaticInstancedVelocity" type="uint32" value="0" />
                            <attribute id="StaticVelocity" type="uint32" value="0" />
                            <attribute id="UniformName" type="FixedString" value="FloatParameter_SeeThroughEnabled" />
                            <attribute id="Value" type="float" value="0" />
                        </node>
                        <node id="ScalarParameters">
                            <attribute id="Enabled" type="bool" value="False" />
                            <attribute id="ExportAsPreset" type="bool" value="False" />
                            <attribute id="GroupName" type="FixedString" value="" />
                            <attribute id="ParameterName" type="FixedString" value="_OpacityFade" />
                            <attribute id="SkinnedForward" type="uint32" value="4" />
                            <attribute id="StaticForward" type="uint32" value="4" />
                            <attribute id="StaticInstancedForward" type="uint32" value="4" />
                            <attribute id="UniformName" type="FixedString" value="_OpacityFade" />
                            <attribute id="Value" type="float" value="1" />
                        </node>
                        <node id="ScalarParameters">
                            <attribute id="Enabled" type="bool" value="False" />
                            <attribute id="ExportAsPreset" type="bool" value="True" />
                            <attribute id="GroupName" type="FixedString" value="" />
                            <attribute id="ParameterName" type="FixedString" value="Reflectance" />
                            <attribute id="SkinnedDeferred" type="uint32" value="0" />
                            <attribute id="SkinnedForward" type="uint32" value="8" />
                            <attribute id="StaticBake" type="uint32" value="4" />
                            <attribute id="StaticDeferred" type="uint32" value="0" />
                            <attribute id="StaticForward" type="uint32" value="8" />
                            <attribute id="StaticInstancedDeferred" type="uint32" value="0" />
                            <attribute id="StaticInstancedForward" type="uint32" value="8" />
                            <attribute id="UniformName" type="FixedString" value="FloatParameter_Reflectance" />
                            <attribute id="Value" type="float" value="0.5" />
                        </node>
                        <node id="Texture2DParameters"> <!-- DO NOT REMOVE THIS. I don't know why its here, but it doenst work without it. -->
                            <attribute id="Enabled" type="bool" value="False" />
                            <attribute id="ExportAsPreset" type="bool" value="True" />
                            <attribute id="GroupName" type="FixedString" value="" />
                            <attribute id="ID" type="FixedString" value="9dc5807b-3697-4b8f-ab0f-b9c5c1bd7010" />
                            <attribute id="IgnoreTexelDensity" type="bool" value="True" />
                            <attribute id="ParameterName" type="FixedString" value="" />
                            <children>
                                <node id="SkinnedDepth">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="SkinnedForward">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="SkinnedVelocity">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticBake">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticDepth">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticForward">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedDepth">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="1" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedForward">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="1" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedVelocity">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="1" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticVelocity">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                            </children>
                        </node>
                        <node id="Texture2DParameters">
                            <attribute id="Enabled" type="bool" value="True" />
                            <attribute id="ExportAsPreset" type="bool" value="True" />
                            <attribute id="GroupName" type="FixedString" value="Texture Map" />
                            <attribute id="ID" type="FixedString" value="" />
                            <attribute id="ParameterName" type="FixedString" value="normalmap" />
                            <attribute id="UniformName" type="FixedString" value="Texture2DParameter_normalmap_DefaultWrapSampler" />
                            <children>
                                <node id="SkinnedDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="SkinnedForward">
                                    <attribute id="DxPsIndex" type="int8" value="1" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="3" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticBake">
                                    <attribute id="DxPsIndex" type="int8" value="1" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="3" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticForward">
                                    <attribute id="DxPsIndex" type="int8" value="1" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="3" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="0" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedForward">
                                    <attribute id="DxPsIndex" type="int8" value="1" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="2" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                            </children>
                        </node>
                        <node id="Texture2DParameters">
                            <attribute id="Enabled" type="bool" value="True" />
                            <attribute id="ExportAsPreset" type="bool" value="True" />
                            <attribute id="GroupName" type="FixedString" value="Texture Map" />
                            <attribute id="ID" type="FixedString" value="" />
                            <attribute id="ParameterName" type="FixedString" value="basecolor" />
                            <attribute id="UniformName" type="FixedString" value="Texture2DParameter_basecolor_DefaultWrapSampler" />
                            <children>
                                <node id="SkinnedDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="1" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="3" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="SkinnedForward">
                                    <attribute id="DxPsIndex" type="int8" value="2" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="4" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticBake">
                                    <attribute id="DxPsIndex" type="int8" value="2" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="4" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="1" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="3" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticForward">
                                    <attribute id="DxPsIndex" type="int8" value="2" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="4" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="1" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="3" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedForward">
                                    <attribute id="DxPsIndex" type="int8" value="2" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="3" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                            </children>
                        </node>
                        <node id="Texture2DParameters">
                            <attribute id="Enabled" type="bool" value="True" />
                            <attribute id="ExportAsPreset" type="bool" value="True" />
                            <attribute id="GroupName" type="FixedString" value="Texture Map" />
                            <attribute id="ID" type="FixedString" value="" />
                            <attribute id="ParameterName" type="FixedString" value="physicalmap" />
                            <attribute id="UniformName" type="FixedString" value="Texture2DParameter_physicalmap_DefaultWrapSampler" />
                            <children>
                                <node id="SkinnedDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="2" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="4" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="SkinnedForward">
                                    <attribute id="DxPsIndex" type="int8" value="3" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="5" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticBake">
                                    <attribute id="DxPsIndex" type="int8" value="3" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="5" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="2" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="4" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticForward">
                                    <attribute id="DxPsIndex" type="int8" value="3" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="5" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedDeferred">
                                    <attribute id="DxPsIndex" type="int8" value="2" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="4" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                                <node id="StaticInstancedForward">
                                    <attribute id="DxPsIndex" type="int8" value="3" />
                                    <attribute id="DxVsIndex" type="int8" value="-1" />
                                    <attribute id="VkBindingIndex" type="int8" value="4" />
                                    <attribute id="VkDescriptorSet" type="int8" value="1" />
                                </node>
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
    <region id="TextureBank">
        <node id="TextureBank">
            <children>
                <node id="Resource">
                        <attribute id="Depth" type="int32" value="0" />
                        <attribute id="Height" type="int32" value="2048" />
                        <attribute id="ID" type="FixedString" value="88994c75-5afc-48d3-8155-b1ae226e2a9a" />
                        <attribute id="Localized" type="bool" value="False" />
                        <attribute id="Name" type="LSString" value="" />
                        <attribute id="SRGB" type="bool" value="False" />
                        <attribute id="SourceFile" type="LSString" value="Generated/Public/Shared/Assets/..." />
                        <attribute id="Streaming" type="bool" value="True" />
                        <attribute id="Template" type="FixedString" value="" />
                        <attribute id="Type" type="int32" value="1" />
                        <attribute id="Width" type="int32" value="2048" />
                        <attribute id="_OriginalFileVersion_" type="int64" value="144115188075855885" />
                </node>
                <node id="Resource">
                        <attribute id="Depth" type="int32" value="0" />
                        <attribute id="Height" type="int32" value="2048" />
                        <attribute id="ID" type="FixedString" value="25cc3f45-318f-4a82-85c2-c283dff25305" />
                        <attribute id="Localized" type="bool" value="False" />
                        <attribute id="Name" type="LSString" value="" />
                        <attribute id="SRGB" type="bool" value="False" />
                        <attribute id="SourceFile" type="LSString" value="Generated/Public/Shared/Assets/Weapons/..." />
                        <attribute id="Streaming" type="bool" value="True" />
                        <attribute id="Template" type="FixedString" value="" />
                        <attribute id="Type" type="int32" value="1" />
                        <attribute id="Width" type="int32" value="2048" />
                        <attribute id="_OriginalFileVersion_" type="int64" value="144115188075855885" />
                </node>
                <node id="Resource">
                        <attribute id="Depth" type="int32" value="0" />
                        <attribute id="Height" type="int32" value="2048" />
                        <attribute id="ID" type="FixedString" value="211e65ee-c285-4df6-a47d-c1d02b31f228" />
                        <attribute id="Localized" type="bool" value="False" />
                        <attribute id="Name" type="LSString" value="" />
                        <attribute id="SRGB" type="bool" value="False" />
                        <attribute id="SourceFile" type="LSString" value="Generated/Public/Shared/Assets/Weapons/..." />
                        <attribute id="Streaming" type="bool" value="True" />
                        <attribute id="Template" type="FixedString" value="" />
                        <attribute id="Type" type="int32" value="1" />
                        <attribute id="Width" type="int32" value="2048" />
                        <attribute id="_OriginalFileVersion_" type="int64" value="144115188075855885" />
                </node>
            </children>
        </node>
    </region>
    <region id="VisualBank">
        <node id="VisualBank">
            <children>
                <node id="Resource">
                    <attribute id="AttachBone" type="FixedString" value="" />
                    <attribute id="AttachmentSkeletonResource" type="FixedString" value="" />
                    <attribute id="BlueprintInstanceResourceID" type="FixedString" value="" />
                    <attribute id="BoundsMax" type="fvec3" value="0.1193077 0.08212577 0.36261" />
                    <attribute id="BoundsMin" type="fvec3" value="-0.1193077 -0.06461757 -1.156051" />
                    <attribute id="Center" type="fvec3" value="-0.005393635 -0.001314297 -0.331817" />
                    <attribute id="ClothColliderResourceID" type="FixedString" value="" />
                    <attribute id="HairPresetResourceId" type="FixedString" value="" />
                    <attribute id="HairType" type="uint8" value="0" />
                    <attribute id="ID" type="FixedString" value="" />
                    <attribute id="Initialized" type="bool" value="True" />
                    <attribute id="Localized" type="bool" value="False" />
                    <attribute id="MaterialType" type="uint8" value="4" />
                    <attribute id="Name" type="LSString" value="" />
                    <attribute id="NeedsSkeletonRemap" type="bool" value="False" />
                    <attribute id="Radius" type="float" value="1.287762" />
                    <attribute id="ScalpMaterialId" type="FixedString" value="" />
                    <attribute id="SkeletonResource" type="FixedString" value="" />
                    <attribute id="SkeletonSlot" type="FixedString" value="" />
                    <attribute id="Slot" type="FixedString" value="Unassigned" />
                    <attribute id="SoftbodyResourceID" type="FixedString" value="" />
                    <attribute id="SourceFile" type="LSString" value="Generated/Public/Shared/Assets/.../.GR2" />
                    <attribute id="SupportsVertexColorMask" type="bool" value="False" />
                    <attribute id="Template" type="FixedString" value="Generated/Public/Shared/Assets/.../Dummy.0" />
                    <attribute id="_OriginalFileVersion_" type="int64" value="144115203108241409" />
                    <children>
                        <node id="AnimationWaterfall">
                            <attribute id="Object" type="FixedString" value="" />
                        </node>
                        <node id="Base" />
                        <node id="Objects">
                            <attribute id="LOD" type="uint8" value="0" />
                            <attribute id="MaterialID" type="FixedString" value="" />
                            <attribute id="ObjectID" type="FixedString" value=".0" />
                            <attribute id="Physics" type="FixedString" value="" />
                            <attribute id="Slot" type="FixedString" value="" />
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
"""
