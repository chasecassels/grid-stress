import pandas as pd
import sqlite3
import os

folder_path = "../source-data"
db_path = "../database/weather-data.db"
conn = sqlite3.connect(db_path)

file = 'New_York_City_Population_by_Borough,_1950_-_2040_20251203.csv'

#import population csv into sqlite db
for filename in os.listdir(folder_path):
    if filename == file:
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        table_name = os.path.splitext(filename)[0]
        parts = table_name.split("_")
        output_table_name = "NYC_Pop_by_Borough"
        df.to_sql(output_table_name, conn, if_exists="replace", index=False)
        print(f"Imported '{filename}' into table '{output_table_name}'", flush=True)

conn.commit()
conn.close()
print("All files imported successfully!", flush=True)
