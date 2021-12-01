import pandas as pd
import geopandas as gpd

### variables

path_od18 = "../../../pmfartm_2020-05-29/18.2b2/OD18.csv"

path_aires_diff = "../../../eod18_geomatique/shapefile-SM"

colonnes_AD = ['Sm100', 'geometry']

colonnes_od = ["FEUILLET", "FACLOG", "PERSLOGI"]

nom_enreg = "hab_SM.pkl"

CRS_AD = "EPSG:3347"
CRS_domiciles = "EPSG:2950"


### Import bases

print("import bases")
od18 = pd.read_csv(path_od18)
print("OD, {} lignes".format(len(od18)))
AD = gpd.read_file(path_aires_diff)
print("importé\n")



### calculs



print("calcul des aires de diffusion associées aux lignes de l'enquete...")
geoOD18 = gpd.GeoDataFrame(od18[colonnes_od], geometry = gpd.points_from_xy(od18.XDOMI, od18.YDOMI), crs = CRS_domiciles)

print("import aires de diffusion...")
geoAD = gpd.read_file(path_aires_diff).to_crs(CRS_domiciles)[colonnes_AD]

print("Merging...")
od18 = gpd.sjoin(geoOD18, geoAD, how="inner", op='intersects')
print("Mergé\n")


d = {}
for feu, df in od18.groupby(["FEUILLET"]):
	if df.Sm100.iloc[0] in d.keys():
		d[df.Sm100.iloc[0]] += df.PERSLOGI.iloc[0] * df.FACLOG.iloc[0]
	else:
		d[df.Sm100.iloc[0]] = df.PERSLOGI.iloc[0] * df.FACLOG.iloc[0]


d2 = {"SM":[], "nb_pers":[]}
for k in d.keys():
	d2["SM"].append(k)
	d2["nb_pers"].append(d[k])

pers_par_aire = pd.DataFrame(d2)
print(len(pers_par_aire), " lignes créées")
print(pers_par_aire.head(30)) 


print("enregistrement")
pers_par_aire.to_pickle(nom_enreg)
print("enregistré sous {}".format(nom_enreg))

