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

To ingest NYC Weather Data from the Open Science Foundation API into an empty SQLite database:

```
touch database/weather-data.db
cd file-extraction
bash filerun_import_processes.sh
```

---

## Zoning/Land Use Data Ingestion


---

## Preprocessing


---

## To-dos

Data sourcing:

-Source land-use historical data and future data
-Source grid use historical data
-Source projected annual temperature rise data 
-Create future weather data tables (emulate format of historical data and use averages + projected increases to fill)









