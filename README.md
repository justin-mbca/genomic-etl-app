# Genomic ETL Project

## 🗺️ Architecture Diagram (Mermaid)

## Technologies Used Diagram

```mermaid
graph TD
    A(Project) --> B(Python 3.9+)
    A --> C(Gradio)
    A --> D(Hugging Face Transformers)
    D --> D1(BioBERT)
    D --> D2(PubMedBERT)
    D --> D3(ClinicalBERT)
    A --> E(OpenAI API)
    A --> G(Custom Rule-based Logic)
    A --> H(JSON, Regex, Standard Libraries)
```

```mermaid
graph TD
    A(FASTQ Upload) --> B(FastAPI Backend)
    B --> C(ETL Pipeline (Python))
    C --> D(Annotated CSV)
    D --> E(SQLite DB)
    E --> F(React Frontend)
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
