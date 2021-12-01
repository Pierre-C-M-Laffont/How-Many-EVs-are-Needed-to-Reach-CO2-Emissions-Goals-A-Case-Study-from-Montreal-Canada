from qgis.core import (
    QgsProject,
    QgsPathResolver,
    QgsVectorLayer
)

from qgis.gui import (
    QgsLayerTreeMapCanvasBridge,
)


#init pour une appli indépendante
# Supply path to qgis install location
QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()





### Doc officielle

project = QgsProject.instance()
project.read('nom_du_projet.qgs')
print(project.fileName())


project.write()
# ... or to a new file
project.write('nom_du_projet.qgs')




#If you are writing a QGIS standalone application, in order to synchronise the loaded project with the canvas you need to instantiate a QgsLayerTreeMapCanvasBridge as in the example below:
bridge = QgsLayerTreeMapCanvasBridge( \
         QgsProject.instance().layerTreeRoot(), canvas)
# Now you can safely load your project and see it in the canvas
project.read('testdata/my_new_qgis_project.qgs')



vl = QgsVectorLayer("Linestring", "temp", "memory")
if not vl.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vl)

# pour l'ajouter à l'instance :
QgsProject.instance().addMapLayer(rlayer)

# QgsProject.instance().removeMapLayer(layer_id)
QgsProject.instance().removeMapLayer(rlayer.id())

#lister
QgsProject.instance().mapLayers()


### Petit site https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis101-creating-editing-a-new-vector-layer/
vl = QgsVectorLayer("Linestring", "temp", "memory")


# ajouter des attributs
from qgis.PyQt.QtCore import QVariant
pr = vl.dataProvider()
pr.addAttributes([QgsField("name", QVariant.String),
                  QgsField("age",  QVariant.Int),
                  QgsField("size", QVariant.Double)])
vl.updateFields()

# ajouter des enregistrements
f = QgsFeature()
f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10,10)))
#gLine = QgsGeometry.fromPolyline([QgsPoint(1, 1), QgsPoint(2, 2)])
f.setAttributes(["Ada L.", 2, 0.3])
pr.addFeature(f)
vl.updateExtents() 
QgsProject.instance().addMapLayer(vl)

# quelques stats :
print("No. fields:", len(pr.fields()))
print("No. features:", pr.featureCount())
e = vl.extent()
print("Extent:", e.xMinimum(), e.yMinimum(), e.xMaximum(), e.yMaximum())
 
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry().asPoint())

# pour ajouter les attributs
help(QgsVectorLayer.addAttribute)

# ce qui donne 
vl.startEditing()
 
my_field_name = 'new field'
vl.addAttribute(QgsField(my_field_name, QVariant.String))
vl.updateFields()
 
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry().asPoint())

# pour changer les champs de certains enregistrements
my_field_value = 'Hello world!'
for f in vl.getFeatures():
    f[my_field_name] = my_field_value
    vl.updateFeature(f)
 
vl.commitChanges()
 
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry().asPoint())


# finir l'édition
iface.vectorLayerTools().stopEditing(vl) 



# pour faire plus court :
my_field_name = 'new field'
my_field_value = 'Hello world!'
 
with edit(vl):
    vl.addAttribute(QgsField(my_field_name, QVariant.String))
    vl.updateFields()
    for f in vl.getFeatures():
        f[my_field_name] = my_field_value
        vl.updateFeature(f)
