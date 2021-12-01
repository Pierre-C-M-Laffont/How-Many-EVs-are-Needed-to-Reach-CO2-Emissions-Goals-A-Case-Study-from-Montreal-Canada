<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" simplifyLocal="1" simplifyAlgorithm="0" simplifyMaxScale="1" maxScale="0" simplifyDrawingHints="1" labelsEnabled="0" version="3.10.4-A Coruña" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" minScale="1e+08" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="RuleRenderer" symbollevels="0" enableorderby="0" forceraster="0">
    <rules key="{c011e98f-5d43-4b52-9712-6e87fde44d7e}">
      <rule label="&lt; 1/2x l'objectif par personne" key="{e6aa2dce-ce8c-40e3-a972-858b3eab0ae4}" symbol="0" filter="&quot;tCO2/an/pe&quot; &lt; 0.2679"/>
      <rule label="&lt; l'objectif par personne" key="{ba2aa8cf-8a11-4555-9f26-c8529bfcd3de}" symbol="1" filter=" &quot;tCO2/an/pe&quot; > 0.2679 and  &quot;tCO2/an/pe&quot; &lt; 0.5358"/>
      <rule label="> l'objectif par personne" key="{4fa899ea-5947-4545-8090-6effb555c7bd}" symbol="2" filter=" &quot;tCO2/an/pe&quot; > 0.5358 and  &quot;tCO2/an/pe&quot; &lt; 1.0716"/>
      <rule label="> 2x l'objectif par personne" key="{1086f937-b17e-4958-bd78-ece75035f3f0}" symbol="3" filter=" &quot;tCO2/an/pe&quot; > 1.0716 and  &quot;tCO2/an/pe&quot; &lt; 2.1432"/>
      <rule label="> 4x l'objectif par personne" key="{4488500e-5f94-4112-b5ad-acd935ab21d3}" symbol="4" filter=" &quot;tCO2/an/pe&quot; > 2.1432 and  &quot;tCO2/an/pe&quot; &lt; 4.2864"/>
      <rule label="> 8x l'objectif par personne" key="{511ce14c-c249-4e10-9b81-95aa8fa80c56}" symbol="5" filter=" &quot;tCO2/an/pe&quot; > 4.2864"/>
    </rules>
    <symbols>
      <symbol type="fill" clip_to_extent="1" force_rhr="0" name="0" alpha="1">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="fill" clip_to_extent="1" force_rhr="0" name="1" alpha="1">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="fill" clip_to_extent="1" force_rhr="0" name="2" alpha="1">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="fill" clip_to_extent="1" force_rhr="0" name="3" alpha="1">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="fill" clip_to_extent="1" force_rhr="0" name="4" alpha="1">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="fill" clip_to_extent="1" force_rhr="0" name="5" alpha="1">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions" value="&quot;ADIDU&quot;"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory diagramOrientation="Up" enabled="0" maxScaleDenominator="1e+08" scaleDependency="Area" penWidth="0" lineSizeType="MM" opacity="1" sizeType="MM" labelPlacementMethod="XHeight" penAlpha="255" width="15" penColor="#000000" minScaleDenominator="0" backgroundAlpha="255" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0" lineSizeScale="3x:0,0,0,0,0,0" barWidth="5" minimumSize="0" height="15" scaleBasedVisibility="0" backgroundColor="#ffffff">
      <fontProperties style="" description="Ubuntu,11,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" label="" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" placement="1" priority="0" linePlacementFlags="18" obstacle="0" showAll="1" zIndex="0">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option type="double" value="0" name="allowedGapsBuffer"/>
        <Option type="bool" value="false" name="allowedGapsEnabled"/>
        <Option type="QString" value="" name="allowedGapsLayer"/>
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
    <field name="km/jr/ve">
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
    <alias index="0" name="" field="ADIDU"/>
    <alias index="1" name="" field="aires"/>
    <alias index="2" name="" field="nb_pers"/>
    <alias index="3" name="" field="nb_veh"/>
    <alias index="4" name="" field="veh/pers"/>
    <alias index="5" name="" field="gCO2/km"/>
    <alias index="6" name="" field="km_totaux"/>
    <alias index="7" name="" field="km/hab"/>
    <alias index="8" name="" field="tCO2/AD"/>
    <alias index="9" name="" field="kgCO2/pers"/>
    <alias index="10" name="" field="km/jr/ve"/>
    <alias index="11" name="" field="gCO2/m2"/>
    <alias index="12" name="" field="tCO2/an/AD"/>
    <alias index="13" name="" field="tCO2/an/pe"/>
    <alias index="14" name="" field="tCO2/an/ve"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="ADIDU" applyOnUpdate="0" expression=""/>
    <default field="aires" applyOnUpdate="0" expression=""/>
    <default field="nb_pers" applyOnUpdate="0" expression=""/>
    <default field="nb_veh" applyOnUpdate="0" expression=""/>
    <default field="veh/pers" applyOnUpdate="0" expression=""/>
    <default field="gCO2/km" applyOnUpdate="0" expression=""/>
    <default field="km_totaux" applyOnUpdate="0" expression=""/>
    <default field="km/hab" applyOnUpdate="0" expression=""/>
    <default field="tCO2/AD" applyOnUpdate="0" expression=""/>
    <default field="kgCO2/pers" applyOnUpdate="0" expression=""/>
    <default field="km/jr/ve" applyOnUpdate="0" expression=""/>
    <default field="gCO2/m2" applyOnUpdate="0" expression=""/>
    <default field="tCO2/an/AD" applyOnUpdate="0" expression=""/>
    <default field="tCO2/an/pe" applyOnUpdate="0" expression=""/>
    <default field="tCO2/an/ve" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" constraints="0" field="ADIDU" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="aires" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="nb_pers" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="nb_veh" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="veh/pers" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="gCO2/km" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="km_totaux" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="km/hab" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="tCO2/AD" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="kgCO2/pers" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="km/jr/ve" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="gCO2/m2" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="tCO2/an/AD" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="tCO2/an/pe" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="tCO2/an/ve" unique_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ADIDU" desc="" exp=""/>
    <constraint field="aires" desc="" exp=""/>
    <constraint field="nb_pers" desc="" exp=""/>
    <constraint field="nb_veh" desc="" exp=""/>
    <constraint field="veh/pers" desc="" exp=""/>
    <constraint field="gCO2/km" desc="" exp=""/>
    <constraint field="km_totaux" desc="" exp=""/>
    <constraint field="km/hab" desc="" exp=""/>
    <constraint field="tCO2/AD" desc="" exp=""/>
    <constraint field="kgCO2/pers" desc="" exp=""/>
    <constraint field="km/jr/ve" desc="" exp=""/>
    <constraint field="gCO2/m2" desc="" exp=""/>
    <constraint field="tCO2/an/AD" desc="" exp=""/>
    <constraint field="tCO2/an/pe" desc="" exp=""/>
    <constraint field="tCO2/an/ve" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column hidden="0" type="field" name="ADIDU" width="-1"/>
      <column hidden="0" type="field" name="gCO2/km" width="-1"/>
      <column hidden="0" type="field" name="km_totaux" width="-1"/>
      <column hidden="0" type="field" name="nb_pers" width="-1"/>
      <column hidden="0" type="field" name="aires" width="-1"/>
      <column hidden="0" type="field" name="tCO2/AD" width="-1"/>
      <column hidden="0" type="field" name="km/hab" width="-1"/>
      <column hidden="0" type="field" name="gCO2/m2" width="-1"/>
      <column hidden="0" type="field" name="kgCO2/pers" width="-1"/>
      <column hidden="0" type="field" name="tCO2/an/AD" width="-1"/>
      <column hidden="0" type="field" name="tCO2/an/pe" width="-1"/>
      <column hidden="0" type="field" name="nb_veh" width="-1"/>
      <column hidden="0" type="field" name="tCO2/an/ve" width="-1"/>
      <column hidden="0" type="field" name="km/jr/ve" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
      <column hidden="0" type="field" name="veh/pers" width="-1"/>
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
    <field editable="1" name="gCO2/km"/>
    <field editable="1" name="gCO2/m2"/>
    <field editable="1" name="kgCO2/pers"/>
    <field editable="1" name="km/hab"/>
    <field editable="1" name="km/jr/ve"/>
    <field editable="1" name="km_totaux"/>
    <field editable="1" name="nb_pers"/>
    <field editable="1" name="nb_veh"/>
    <field editable="1" name="tCO2/AD"/>
    <field editable="1" name="tCO2/an/AD"/>
    <field editable="1" name="tCO2/an/pe"/>
    <field editable="1" name="tCO2/an/ve"/>
    <field editable="1" name="veh/pers"/>
  </editable>
  <labelOnTop>
    <field name="ADIDU" labelOnTop="0"/>
    <field name="aires" labelOnTop="0"/>
    <field name="gCO2/km" labelOnTop="0"/>
    <field name="gCO2/m2" labelOnTop="0"/>
    <field name="kgCO2/pers" labelOnTop="0"/>
    <field name="km/hab" labelOnTop="0"/>
    <field name="km/jr/ve" labelOnTop="0"/>
    <field name="km_totaux" labelOnTop="0"/>
    <field name="nb_pers" labelOnTop="0"/>
    <field name="nb_veh" labelOnTop="0"/>
    <field name="tCO2/AD" labelOnTop="0"/>
    <field name="tCO2/an/AD" labelOnTop="0"/>
    <field name="tCO2/an/pe" labelOnTop="0"/>
    <field name="tCO2/an/ve" labelOnTop="0"/>
    <field name="veh/pers" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>ADIDU</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
