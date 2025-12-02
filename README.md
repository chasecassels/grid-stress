**Author:** Chase Cassels  
**Email:** chasecassels@gmail.com  

---

Exploratory data analysis project to study how grid stress may change across NYC due to temperature variance, climate change, land use changes, population change, and technological improvements.

- [Weather Data Ingestion](weather-data-ingestion)
- [Zoning/Land Use Data Ingestion](#usage)
- [To-dos](#to-dos)
- [Contributing](#contributing)
- [License](#license)

---

## Weather Data Ingestion

To ingest NYC Weather Data from the Open Science Foundation API into an empty SQLite database:

```
touch database/weather-data.db
cd file-extraction
bash filerun_import_processes.sh
```










