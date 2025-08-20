# Genomic ETL Project

## 🗺️ Architecture Diagram

```mermaid
graph TD
    A(FASTQ Upload) --> B(FastAPI Backend)
    B --> C(ETL Pipeline Python)
    C --> D(Annotated CSV)
    D --> E(SQLite DB)
    E --> F(React Frontend)
```

## Technologies Used Diagram

```mermaid
graph TD
    FastAPI[FastAPI Backend] -->|built with| Python[Python 3]
    FastAPI -->|framework| FastAPI_Lib[FastAPI]
    ETL[ETL Pipeline] -->|built with| Python
    ETL -->|data wrangling| Pandas[Pandas]
    SQLite[SQLite DB] -->|database| SQLite_Lib[SQLite]
    React[React Frontend] -->|built with| JS[JavaScript]
    React -->|framework| React_Lib[React]
    FastAPI --> SQLite
    FastAPI --> ETL
    FastAPI --> React
```

## Backend (FastAPI)
- Run: `uvicorn main:app --reload`
- Endpoints:
  - `/` : Health check
  - `/upload` : Upload genomic data file
  - `/results` : Query processed results

## ETL
- Place Snakemake/Nextflow pipelines and scripts here

## Frontend
- React app for curation and review UI

---

### Next Steps
- Implement ETL scripts in `etl/`
- Scaffold React app in `frontend/`
- Connect backend to SQL Server
- Add unit tests and CI/CD
