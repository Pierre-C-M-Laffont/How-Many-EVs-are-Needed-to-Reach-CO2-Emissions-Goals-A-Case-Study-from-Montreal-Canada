import pandas as pd

from qgis.core import *

from qgis.gui import *

from qgis.PyQt.QtCore import *


QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# import et connexion avec l'appli ?
project = QgsProject.instance()
canvas = QgsMapCanvas()
bridge = QgsLayerTreeMapCanvasBridge( \
         QgsProject.instance().layerTreeRoot(), canvas)
project.read('Test.qgz')
print(project.fileName())




vl = QgsVectorLayer("Linestring?crs=epsg:4326", "temp", "memory")
if not vl.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vl)
    print("vector layer added")


donnees = pd.read_pickle("donnees_QGIS.pkl")

# ajouter des attributs

pr = vl.dataProvider()
pr.addAttributes([QgsField("vol_ois", QVariant.Double),
                  QgsField("calcule",  QVariant.Double)])
vl.updateFields()

# ajouter des enregistrements
for i in range(len(donnees)) :
	f = QgsFeature()
	l = [[donnees.LONORIG.iloc[i], donnees.LATORIG.iloc[i]], [donnees.LONDEST.iloc[i], donnees.LATDEST.iloc[i]]]
	l2 = [QgsPoint(x[0], x[1]) for x in l]
	f.setGeometry(QgsGeometry.fromPolyline(l2))
	f.setAttributes([donnees.DIST.iloc[i], donnees.distances_calculees.iloc[i]])
	pr.addFeature(f)
vl.updateExtents() 
QgsProject.instance().addMapLayer(vl)

# quelques stats :
print("No. fields:", len(pr.fields()))
print("No. features:", pr.featureCount())
e = vl.extent()
print("Extent:", e.xMinimum(), e.yMinimum(), e.xMaximum(), e.yMaximum())
 
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry())

"""
# ce qui donne 
vl.startEditing()
 
my_field_name = 'new field'
vl.addAttribute(QgsField(my_field_name, QVariant.String))
vl.updateFields()
 
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry())

# pour changer les champs de certains enregistrements
my_field_value = 'Hello world!'
for f in vl.getFeatures():
    f[my_field_name] = my_field_value
    vl.updateFeature(f)
 
vl.commitChanges()
 
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry())


# finir l'édition
iface.vectorLayerTools().stopEditing(vl) 

#"""

# pour faire plus court :
my_field_name = 'new field'
my_field_value = 'Hello world!'
 
with edit(vl):
    vl.addAttribute(QgsField(my_field_name, QVariant.String))
    vl.updateFields()
    for f in vl.getFeatures():
        f[my_field_name] = my_field_value
        vl.updateFeature(f)

"""
crs = QgsCoordinateReferenceSystem("epsg:4326")

error = QgsVectorFileWriter.writeAsVectorFormat(vl, "outShapefile.shp", "UTF-8", crs , "ESRI Shapefile")

if error == QgsVectorFileWriter.NoError:
    print("success! writing new memory layer")


project.write('Test2.qgz')
#"""
qgs.exitQgis()
