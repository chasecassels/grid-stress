import pandas as pd
import sqlite3
import os

folder_path = "../source-data"
db_path = "../database/weather-data.db"
conn = sqlite3.connect(db_path)
file = 'New_York_City_Population_by_Borough,_1950_-_2040_20251203.csv'
df = pd.DataFrame()

#transpose and format input data
def process_input(df) -> pd.DataFrame:
    df = df.drop(df.columns[0], axis = 1)
    df = df.drop(df.columns[2::2], axis = 1)
    df_with_names = df.copy()
    df = df_with_names.T
    df = df.drop(df.columns[[0, 1, 5]], axis = 1)
    return df

#import population csv into sqlite db
for filename in os.listdir(folder_path):
    if filename == file:
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        df = process_input(df)
        table_name = os.path.splitext(filename)[0]
        parts = table_name.split("_")
        output_table_name = "nyc_population"
        df.index.values[0] = "Decade"
        df = df.set_axis(list(range(len(df.columns))), axis=1)
        df.to_sql(output_table_name, conn, if_exists="replace", index=True)
        print(f"Imported '{filename}' into table '{output_table_name}'", flush=True)


#temporal downscaling to minutes (unnecessary but why not)
#def interpolate(df) -> DataFrame:







conn.commit()
conn.close()
print("All files imported successfully!", flush=True)
