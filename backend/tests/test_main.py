
import os
import sys
import tempfile
import pytest
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
from fastapi.testclient import TestClient
from main import app, DB_PATH, init_db

client = TestClient(app)

def setup_module(module):
    # Use a temporary database for testing
    db_fd, db_path = tempfile.mkstemp()
    os.close(db_fd)
    app.dependency_overrides[DB_PATH] = db_path
    init_db()
    module._db_path = db_path

def teardown_module(module):
    os.unlink(module._db_path)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Genomic ETL API is running"

def test_results_empty():
    # Clear the table before testing
    import sqlite3
    from main import DB_PATH
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM annotated_variants')
    conn.commit()
    conn.close()
    response = client.get("/results")
    assert response.status_code == 200
    assert response.json()["results"] == []
