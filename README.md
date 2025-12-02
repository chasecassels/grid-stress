# NYC Grid Stress

**Author:** Chase Cassels  
**Email:** chasecassels@gmail.com  

---

Exploratory data analysis project to study how grid stress may change across NYC due to temperature variance, climate change, land use changes, population change, and technological improvements.

- [Weather Data Ingestion](#weather)
- [Zoning/Land Use Data Ingestion](#zoning)
- [Preprocessing](#preproc)
- [To-dos](#to-dos)

---

## Weather Data Ingestion

To ingest Historical NYC Weather Data from the Open Science Foundation API into an empty SQLite database:

```
touch database/weather-data.db
cd file-extraction
bash run_import_processes.sh
```

---

## Zoning/Land Use Data Ingestion


---

## Population Data Ingestion


---

## Preprocessing


---

## To-dos

Data sourcing:

-Source land-use historical data and future data  
-Source population historical and future data
-Source grid use historical data  
-Source annual temperature rise projections  



Preprocessing:  
  
-Create future weather data tables (emulate format of historical data and use averages + projected increases to fill)  
-Temporally downscale population and land use data  
-Write and test Joins/Unions to create one comprehensive historical table and one comprehensive future table with an  
 empty grid use column
















