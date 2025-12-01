import re
import requests
import os
from osfclient.api import OSF
import geopandas as gpd
from shapely.geometry import Point

nyc_boundary = gpd.read_file("nybb_25c/nybb.shp")
nyc_boundary = nyc_boundary.to_crs(epsg=4326)
nyc_boundary = nyc_boundary.union_all()
target_folder = "../source-data"
nyc_files = []
yrs = []

#test projection
if nyc_boundary.contains(Point(-74.0060, 40.7128)):
    print("Projection test passed", flush=True)
else:
    print("Projection error", flush=True)

#retrieve ID's for individual years from parent project
PARENT_ID = "5dp8e"
parent_url = f"https://api.osf.io/v2/nodes/{PARENT_ID}/children/"
while parent_url:
    resp = requests.get(parent_url).json()
    for child in resp["data"]:
        yrs.append(child["id"])
    parent_url = resp["links"].get("next")

#file download function
def download_file(file):
    filename = file["attributes"]["name"]
    download_url = file["links"]["download"]
    content = requests.get(download_url).content
    output_path = os.path.join(target_folder, filename)
    with open(output_path, "wb") as f:
        f.write(content)
        print("Saved " + filename + " in " + target_folder, flush=True)

#retrieve all files with location in nyc boundary
for i in range(len(yrs)):
    year_id = yrs[i]
    year_url = f"https://api.osf.io/v2/nodes/{year_id}/files/osfstorage/"
    while year_url:
        resp = requests.get(year_url).json()
        for file in resp["data"]:
            match = re.search(r"Lat_([-\d\.]+)_Lon_([-\d\.]+)", file["attributes"]["name"])
            lat, lon = float(match.group(1)), float(match.group(2))
            if nyc_boundary.contains(Point(lon, lat)):
                nyc_files.append(file["attributes"]["name"])
                download_file(file)
        year_url = resp["links"].get("next")