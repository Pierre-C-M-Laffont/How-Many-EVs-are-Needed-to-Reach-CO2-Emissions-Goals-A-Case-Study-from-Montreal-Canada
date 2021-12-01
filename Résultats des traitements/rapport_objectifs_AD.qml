<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" simplifyDrawingHints="1" version="3.10.4-A Coruña" simplifyMaxScale="1" readOnly="0" styleCategories="AllStyleCategories" simplifyLocal="1" minScale="1e+08" labelsEnabled="0" simplifyDrawingTol="1" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" type="RuleRenderer" symbollevels="0" enableorderby="0">
    <rules key="{c011e98f-5d43-4b52-9712-6e87fde44d7e}">
      <rule key="{e6aa2dce-ce8c-40e3-a972-858b3eab0ae4}" filter="&quot;tCO2/an/ve&quot; &lt; 0.44225" label="&lt; 1/2x l'objectif par véhicule" symbol="0"/>
      <rule key="{ba2aa8cf-8a11-4555-9f26-c8529bfcd3de}" filter=" &quot;tCO2/an/ve&quot; > 0.44225 and  &quot;tCO2/an/ve&quot; &lt; 0.8845" label="&lt; l'objectif par véhicule" symbol="1"/>
      <rule key="{4fa899ea-5947-4545-8090-6effb555c7bd}" filter=" &quot;tCO2/an/ve&quot; > 0.8845 and  &quot;tCO2/an/ve&quot; &lt; 1.769" label="> l'objectif par véhicule" symbol="2"/>
      <rule key="{1086f937-b17e-4958-bd78-ece75035f3f0}" filter=" &quot;tCO2/an/ve&quot; > 1.769 and  &quot;tCO2/an/ve&quot; &lt; 3.538" label="> 2x l'objectif par véhicule" symbol="3"/>
      <rule key="{4488500e-5f94-4112-b5ad-acd935ab21d3}" filter=" &quot;tCO2/an/ve&quot; > 3.538 and  &quot;tCO2/an/ve&quot; &lt; 7.076" label="> 4x l'objectif par véhicule" symbol="4"/>
      <rule key="{511ce14c-c249-4e10-9b81-95aa8fa80c56}" filter=" &quot;tCO2/an/ve&quot; > 7.076" label="> 8x l'objectif par véhicule" symbol="5"/>
    </rules>
    <symbols>
      <symbol alpha="1" type="fill" name="0" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="50,50,155,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="150,150,255,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="2" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,150,150,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="3" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,100,100,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="4" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,50,50,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="5" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
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
    <property key="dualview/previewExpressions" value="&quot;ADIDU&quot;"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory width="15" opacity="1" lineSizeType="MM" scaleBasedVisibility="0" scaleDependency="Area" backgroundColor="#ffffff" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" penColor="#000000" barWidth="5" backgroundAlpha="255" rotationOffset="270" enabled="0" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="0" diagramOrientation="Up" maxScaleDenominator="1e+08" penWidth="0" height="15" sizeType="MM" minimumSize="0" penAlpha="255">
      <fontProperties description="Ubuntu,11,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" placement="1" obstacle="0" zIndex="0" priority="0" linePlacementFlags="18" dist="0">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
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
    <default expression="" applyOnUpdate="0" field="ADIDU"/>
    <default expression="" applyOnUpdate="0" field="aires"/>
    <default expression="" applyOnUpdate="0" field="nb_pers"/>
    <default expression="" applyOnUpdate="0" field="nb_veh"/>
    <default expression="" applyOnUpdate="0" field="veh/pers"/>
    <default expression="" applyOnUpdate="0" field="gCO2/km"/>
    <default expression="" applyOnUpdate="0" field="km_totaux"/>
    <default expression="" applyOnUpdate="0" field="km/hab"/>
    <default expression="" applyOnUpdate="0" field="tCO2/AD"/>
    <default expression="" applyOnUpdate="0" field="kgCO2/pers"/>
    <default expression="" applyOnUpdate="0" field="km/jr/ve"/>
    <default expression="" applyOnUpdate="0" field="gCO2/m2"/>
    <default expression="" applyOnUpdate="0" field="tCO2/an/AD"/>
    <default expression="" applyOnUpdate="0" field="tCO2/an/pe"/>
    <default expression="" applyOnUpdate="0" field="tCO2/an/ve"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="ADIDU"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="aires"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="nb_pers"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="nb_veh"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="veh/pers"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="gCO2/km"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="km_totaux"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="km/hab"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="tCO2/AD"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="kgCO2/pers"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="km/jr/ve"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="gCO2/m2"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="tCO2/an/AD"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="tCO2/an/pe"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" notnull_strength="0" field="tCO2/an/ve"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="ADIDU" exp=""/>
    <constraint desc="" field="aires" exp=""/>
    <constraint desc="" field="nb_pers" exp=""/>
    <constraint desc="" field="nb_veh" exp=""/>
    <constraint desc="" field="veh/pers" exp=""/>
    <constraint desc="" field="gCO2/km" exp=""/>
    <constraint desc="" field="km_totaux" exp=""/>
    <constraint desc="" field="km/hab" exp=""/>
    <constraint desc="" field="tCO2/AD" exp=""/>
    <constraint desc="" field="kgCO2/pers" exp=""/>
    <constraint desc="" field="km/jr/ve" exp=""/>
    <constraint desc="" field="gCO2/m2" exp=""/>
    <constraint desc="" field="tCO2/an/AD" exp=""/>
    <constraint desc="" field="tCO2/an/pe" exp=""/>
    <constraint desc="" field="tCO2/an/ve" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column width="-1" type="field" name="ADIDU" hidden="0"/>
      <column width="-1" type="field" name="gCO2/km" hidden="0"/>
      <column width="-1" type="field" name="km_totaux" hidden="0"/>
      <column width="-1" type="field" name="nb_pers" hidden="0"/>
      <column width="-1" type="field" name="aires" hidden="0"/>
      <column width="-1" type="field" name="tCO2/AD" hidden="0"/>
      <column width="-1" type="field" name="km/hab" hidden="0"/>
      <column width="-1" type="field" name="gCO2/m2" hidden="0"/>
      <column width="-1" type="field" name="kgCO2/pers" hidden="0"/>
      <column width="-1" type="field" name="tCO2/an/AD" hidden="0"/>
      <column width="-1" type="field" name="tCO2/an/pe" hidden="0"/>
      <column width="-1" type="field" name="nb_veh" hidden="0"/>
      <column width="-1" type="field" name="tCO2/an/ve" hidden="0"/>
      <column width="-1" type="field" name="km/jr/ve" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" type="field" name="veh/pers" hidden="0"/>
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
