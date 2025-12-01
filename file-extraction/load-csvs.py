import pandas as pd
import sqlite3
import os

folder_path = "../source-data"
db_path = "../database/weather-data.db"
conn = sqlite3.connect(db_path)

#import all csvs into sqlite db
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        table_name = os.path.splitext(filename)[0]
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Imported '{filename}' into table '{table_name}'", flush=True)

conn.commit()
conn.close()
print("All files imported successfully!", flush=True)
