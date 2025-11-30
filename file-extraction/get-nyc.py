#Downloads NYC station CSVs from CHUWD-H v1.0 project (from Open Science Foundation)

import re
import requests
import os
from osfclient.api import OSF
import geopandas as gpd
from shapely.geometry import Point

nyc_boundary = gpd.read_file("nybb_25c/nybb.shp")
nyc_boundary = nyc_boundary.to_crs(epsg=4326)

target_folder = "../source-data"
nyc_files = []
yrs = []

PARENT_ID = "5dp8e"
url = f"https://api.osf.io/v2/nodes/{PARENT_ID}/children/"

yrs = []

while url:
    resp = requests.get(url).json()

    for child in resp["data"]:
        print(child["id"])
        yrs.append(child["id"])

    url = resp["links"].get("next")



#file_data = meta["data"]
#filename = file_data["attributes"]["name"]
#download_url = file_data["links"]["download"]

#content = requests.get(download_url).content
#output_path = os.path.join(target_folder, filename)

#with open(output_path, "wb") as f:
#    f.write(content)
#    print("Saved " + filename + " in " + target_folder)
