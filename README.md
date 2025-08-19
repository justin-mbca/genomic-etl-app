# Genomic ETL Project

## 🗺️ Architecture Diagram (Mermaid)

```mermaid
flowchart TD
  A[FASTQ Upload] --> B[FastAPI Backend]
  B --> C[ETL Pipeline (Python)]
  C --> D[Annotated CSV]
  D --> E[SQLite DB]
  E --> F[React Frontend]
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
