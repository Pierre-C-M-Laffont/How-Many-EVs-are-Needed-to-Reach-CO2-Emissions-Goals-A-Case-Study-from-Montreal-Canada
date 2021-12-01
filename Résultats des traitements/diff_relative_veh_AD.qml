<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.10.4-A Coruña" simplifyDrawingTol="1" maxScale="0" simplifyMaxScale="1" readOnly="0" hasScaleBasedVisibilityFlag="0" labelsEnabled="0" simplifyDrawingHints="1" simplifyLocal="1" styleCategories="AllStyleCategories" minScale="1e+08" simplifyAlgorithm="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" type="RuleRenderer" symbollevels="0" forceraster="0">
    <rules key="{6ea6390e-3267-4165-87b5-df16b065ff5b}">
      <rule filter=" &quot;frac_veh&quot; &lt;= 0.25" symbol="0" key="{099ac25d-bdd9-430c-9f4e-7a119356cc47}" label="encore moins selon SAAQ"/>
      <rule filter="&quot;frac_veh&quot; > 0.25 AND &quot;frac_veh&quot; &lt;= 0.5" symbol="1" key="{3a62fddf-f2a4-4514-9f99-ab60ba57dfaa}" label="4x moins"/>
      <rule filter="&quot;frac_veh&quot; > 0.5 AND &quot;frac_veh&quot; &lt;= 0.8" symbol="2" key="{9f7913ce-b647-4ff1-8d6c-cc99220a402c}" label="2x moins">
        <rule filter="&quot;frac_veh&quot; > 0.25 AND &quot;frac_veh&quot; &lt;= 0.5" symbol="3" key="{bbd08f64-4bff-4c60-9a4e-8ca31f9d2a92}" label="4x moins"/>
        <rule filter="&quot;frac_veh&quot; > 0.25 AND &quot;frac_veh&quot; &lt;= 0.5" symbol="4" key="{ca787746-1327-4e64-ba26-90bc7489b114}" label="4x moins"/>
        <rule filter="&quot;frac_veh&quot; > 0.25 AND &quot;frac_veh&quot; &lt;= 0.5" symbol="5" key="{97a7691d-97e8-4ede-80fa-1f84c28480de}" label="4x moins"/>
      </rule>
      <rule filter="&quot;frac_veh&quot; > 0.8 AND &quot;frac_veh&quot; &lt;= 1.2" symbol="6" key="{7239d5fe-8b58-43cd-a4ff-a7d2f5c49823}" label="OK"/>
      <rule filter="&quot;frac_veh&quot; > 1.2 AND &quot;frac_veh&quot; &lt;= 2" symbol="7" key="{55da85b7-f68f-4a67-9c1d-22822a4a87fc}" label="2x plus"/>
      <rule filter="&quot;frac_veh&quot; > 2 AND &quot;frac_veh&quot; &lt;= 4" symbol="8" key="{c20c989e-3c52-4ba8-8aea-0156b24fbea8}" label="4x plus"/>
      <rule filter="&quot;frac_veh&quot; > 4 AND &quot;frac_veh&quot; &lt;= 8" symbol="9" key="{3238084b-bb4b-40bf-914d-854a57930ab5}" label="8x plus"/>
      <rule filter="&quot;frac_veh&quot; > 8 " symbol="10" key="{52191b54-e6d6-487d-b487-cbac7537def8}" label="encore plus"/>
    </rules>
    <symbols>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="0">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="50,50,155,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="100,100,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="10">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="2">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="150,150,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="3">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="100,100,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="4">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="100,100,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="5">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="100,100,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="6">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="7">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,150,150,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="8">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,100,100,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" force_rhr="0" clip_to_extent="1" name="9">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,50,50,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property value="ADIDU" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory diagramOrientation="Up" scaleBasedVisibility="0" maxScaleDenominator="1e+08" penAlpha="255" sizeType="MM" penWidth="0" labelPlacementMethod="XHeight" barWidth="5" rotationOffset="270" enabled="0" minimumSize="0" height="15" lineSizeScale="3x:0,0,0,0,0,0" width="15" backgroundColor="#ffffff" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="0" lineSizeType="MM" penColor="#000000" opacity="1" scaleDependency="Area" backgroundAlpha="255">
      <fontProperties style="" description="Ubuntu,11,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" field="" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" zIndex="0" dist="0" priority="0" placement="1" obstacle="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option value="0" type="double" name="allowedGapsBuffer"/>
        <Option value="false" type="bool" name="allowedGapsEnabled"/>
        <Option value="" type="QString" name="allowedGapsLayer"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <fieldConfiguration>
    <field name="ADIDU">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="aires">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nb_pers">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nb_veh">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nb_veh_OD">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="frac_veh">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="veh/pers">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gCO2/km">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="km_totaux">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="km/hab">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="km/jr/ve">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tCO2/AD">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="kgCO2/pers">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gCO2/m2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tCO2/an/AD">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tCO2/an/pe">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tCO2/an/ve">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="ADIDU" name=""/>
    <alias index="1" field="aires" name=""/>
    <alias index="2" field="nb_pers" name=""/>
    <alias index="3" field="nb_veh" name=""/>
    <alias index="4" field="nb_veh_OD" name=""/>
    <alias index="5" field="frac_veh" name=""/>
    <alias index="6" field="veh/pers" name=""/>
    <alias index="7" field="gCO2/km" name=""/>
    <alias index="8" field="km_totaux" name=""/>
    <alias index="9" field="km/hab" name=""/>
    <alias index="10" field="km/jr/ve" name=""/>
    <alias index="11" field="tCO2/AD" name=""/>
    <alias index="12" field="kgCO2/pers" name=""/>
    <alias index="13" field="gCO2/m2" name=""/>
    <alias index="14" field="tCO2/an/AD" name=""/>
    <alias index="15" field="tCO2/an/pe" name=""/>
    <alias index="16" field="tCO2/an/ve" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="ADIDU" expression=""/>
    <default applyOnUpdate="0" field="aires" expression=""/>
    <default applyOnUpdate="0" field="nb_pers" expression=""/>
    <default applyOnUpdate="0" field="nb_veh" expression=""/>
    <default applyOnUpdate="0" field="nb_veh_OD" expression=""/>
    <default applyOnUpdate="0" field="frac_veh" expression=""/>
    <default applyOnUpdate="0" field="veh/pers" expression=""/>
    <default applyOnUpdate="0" field="gCO2/km" expression=""/>
    <default applyOnUpdate="0" field="km_totaux" expression=""/>
    <default applyOnUpdate="0" field="km/hab" expression=""/>
    <default applyOnUpdate="0" field="km/jr/ve" expression=""/>
    <default applyOnUpdate="0" field="tCO2/AD" expression=""/>
    <default applyOnUpdate="0" field="kgCO2/pers" expression=""/>
    <default applyOnUpdate="0" field="gCO2/m2" expression=""/>
    <default applyOnUpdate="0" field="tCO2/an/AD" expression=""/>
    <default applyOnUpdate="0" field="tCO2/an/pe" expression=""/>
    <default applyOnUpdate="0" field="tCO2/an/ve" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="ADIDU"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="aires"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="nb_pers"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="nb_veh"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="nb_veh_OD"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="frac_veh"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="veh/pers"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="gCO2/km"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="km_totaux"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="km/hab"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="km/jr/ve"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="tCO2/AD"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="kgCO2/pers"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="gCO2/m2"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="tCO2/an/AD"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="tCO2/an/pe"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="tCO2/an/ve"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="ADIDU"/>
    <constraint exp="" desc="" field="aires"/>
    <constraint exp="" desc="" field="nb_pers"/>
    <constraint exp="" desc="" field="nb_veh"/>
    <constraint exp="" desc="" field="nb_veh_OD"/>
    <constraint exp="" desc="" field="frac_veh"/>
    <constraint exp="" desc="" field="veh/pers"/>
    <constraint exp="" desc="" field="gCO2/km"/>
    <constraint exp="" desc="" field="km_totaux"/>
    <constraint exp="" desc="" field="km/hab"/>
    <constraint exp="" desc="" field="km/jr/ve"/>
    <constraint exp="" desc="" field="tCO2/AD"/>
    <constraint exp="" desc="" field="kgCO2/pers"/>
    <constraint exp="" desc="" field="gCO2/m2"/>
    <constraint exp="" desc="" field="tCO2/an/AD"/>
    <constraint exp="" desc="" field="tCO2/an/pe"/>
    <constraint exp="" desc="" field="tCO2/an/ve"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="1" sortExpression="&quot;diff_veh&quot;">
    <columns>
      <column width="-1" type="field" hidden="0" name="ADIDU"/>
      <column width="-1" type="field" hidden="0" name="gCO2/km"/>
      <column width="-1" type="field" hidden="0" name="km_totaux"/>
      <column width="-1" type="field" hidden="0" name="nb_pers"/>
      <column width="-1" type="field" hidden="0" name="aires"/>
      <column width="-1" type="field" hidden="0" name="tCO2/AD"/>
      <column width="-1" type="field" hidden="0" name="km/hab"/>
      <column width="-1" type="field" hidden="0" name="gCO2/m2"/>
      <column width="-1" type="field" hidden="0" name="kgCO2/pers"/>
      <column width="-1" type="field" hidden="0" name="tCO2/an/AD"/>
      <column width="-1" type="field" hidden="0" name="tCO2/an/pe"/>
      <column width="-1" type="field" hidden="0" name="nb_veh"/>
      <column width="-1" type="field" hidden="0" name="tCO2/an/ve"/>
      <column width="-1" type="field" hidden="0" name="km/jr/ve"/>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" type="field" hidden="0" name="veh/pers"/>
      <column width="-1" type="field" hidden="0" name="frac_veh"/>
      <column width="-1" type="field" hidden="0" name="nb_veh_OD"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="ADIDU"/>
    <field editable="1" name="aires"/>
    <field editable="1" name="diff_veh"/>
    <field editable="1" name="frac_veh"/>
    <field editable="1" name="gCO2/km"/>
    <field editable="1" name="gCO2/m2"/>
    <field editable="1" name="kgCO2/pers"/>
    <field editable="1" name="km/hab"/>
    <field editable="1" name="km/jr/ve"/>
    <field editable="1" name="km_totaux"/>
    <field editable="1" name="nb_pers"/>
    <field editable="1" name="nb_veh"/>
    <field editable="1" name="nb_veh_AD"/>
    <field editable="1" name="nb_veh_OD"/>
    <field editable="1" name="tCO2/AD"/>
    <field editable="1" name="tCO2/an/AD"/>
    <field editable="1" name="tCO2/an/pe"/>
    <field editable="1" name="tCO2/an/ve"/>
    <field editable="1" name="veh/pers"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="ADIDU"/>
    <field labelOnTop="0" name="aires"/>
    <field labelOnTop="0" name="diff_veh"/>
    <field labelOnTop="0" name="frac_veh"/>
    <field labelOnTop="0" name="gCO2/km"/>
    <field labelOnTop="0" name="gCO2/m2"/>
    <field labelOnTop="0" name="kgCO2/pers"/>
    <field labelOnTop="0" name="km/hab"/>
    <field labelOnTop="0" name="km/jr/ve"/>
    <field labelOnTop="0" name="km_totaux"/>
    <field labelOnTop="0" name="nb_pers"/>
    <field labelOnTop="0" name="nb_veh"/>
    <field labelOnTop="0" name="nb_veh_AD"/>
    <field labelOnTop="0" name="nb_veh_OD"/>
    <field labelOnTop="0" name="tCO2/AD"/>
    <field labelOnTop="0" name="tCO2/an/AD"/>
    <field labelOnTop="0" name="tCO2/an/pe"/>
    <field labelOnTop="0" name="tCO2/an/ve"/>
    <field labelOnTop="0" name="veh/pers"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>ADIDU</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
