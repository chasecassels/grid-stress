**Author:** Chase Cassels  
**Email:** chasecassels@gmail.com  

---

Exploratory data analysis project to study how grid stress may change across NYC due to temperature variance, climate change, land use changes, population change, and technological improvements.


- [Prerequisites](#prerequisites)
- [Weather Data Ingestion](#installation)
- [Usage](#usage)
- [To-dos](#to-dos)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

Make sure you have the following installed:

- Python 3.x  
- Bash 
- SQLite  

---

### Ingest NYC Weather Data from Open Science Foundation API into an SQLite database.

Create an empty database and run the data extraction scripts:

```
touch database/weather-data.db
cd file-extraction
bash filerun_import_processes.sh
```





