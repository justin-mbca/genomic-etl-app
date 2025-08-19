
import csv
import subprocess
import sys
import csv
import sqlite3
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
DB_PATH = Path(__file__).parent / 'variants.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS annotated_variants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chrom TEXT,
        pos INTEGER,
        ref TEXT,
        alt TEXT,
        clin_sig TEXT
    )''')
    conn.commit()
    conn.close()

def insert_variants_from_csv(csv_path):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute('INSERT INTO annotated_variants (chrom, pos, ref, alt, clin_sig) VALUES (?, ?, ?, ?, ?)',
                      (row['CHROM'], int(row['POS']), row['REF'], row['ALT'], row['CLIN_SIG']))
    conn.commit()
    conn.close()




app = FastAPI()

# Allow CORS for frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()


@app.get('/')
def root():
    return {"message": "Genomic ETL API is running"}


@app.post('/upload')
def upload_file(file: UploadFile = File(...)):
    # Save uploaded file to etl/data
    data_dir = Path(__file__).parent.parent / 'etl' / 'data'
    data_dir.mkdir(exist_ok=True)
    file_path = data_dir / file.filename
    with open(file_path, 'wb') as f:
        f.write(file.file.read())
    # Trigger the ETL pipeline
    etl_script = Path(__file__).parent.parent / 'etl' / 'simulated_pipeline.py'
    python_exe = sys.executable
    try:
        result = subprocess.run([python_exe, str(etl_script)], capture_output=True, text=True, check=True)
        etl_status = 'success'
        etl_output = result.stdout
        # Insert ETL results into SQLite
        annotated_csv = data_dir / 'annotated_variants.csv'
        if annotated_csv.exists():
            insert_variants_from_csv(annotated_csv)
    except subprocess.CalledProcessError as e:
        etl_status = 'error'
        etl_output = e.stderr
    return {"filename": file.filename, "status": "uploaded", "etl_status": etl_status, "etl_output": etl_output}


@app.get('/results')
def get_results():
    # Fetch annotated variants from SQLite
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT chrom, pos, ref, alt, clin_sig FROM annotated_variants')
    rows = c.fetchall()
    conn.close()
    results = [
        {"CHROM": row[0], "POS": row[1], "REF": row[2], "ALT": row[3], "CLIN_SIG": row[4]}
        for row in rows
    ]
    return {"results": results}
