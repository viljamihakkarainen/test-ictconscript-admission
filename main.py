from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
import sqlite3
from datetime import datetime
import os
import json
import uvicorn

app = FastAPI(title="Unit Logbook API", version="1.0.0")

DB_PATH = "logbook.db"

class LogEntry(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., max_length=120)
    body: str
    isoTime: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None

def load_sample_data():
    """Load sample data from the given JSON file."""
    try:
        with open('sample-data/data.json', 'r') as f:
            data = json.load(f)
            return [LogEntry(**entry) for entry in data]
    except FileNotFoundError:
        print("Warning: sample-data/data.json not found, using empty dataset")
        return []

SAMPLE_ENTRIES = load_sample_data()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            isoTime TEXT NOT NULL,
            lat REAL,
            lon REAL
        )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM entries')
    if cursor.fetchone()[0] == 0:
        for entry in SAMPLE_ENTRIES:
            cursor.execute('''
                INSERT INTO entries (title, body, isoTime, lat, lon)
                VALUES (?, ?, ?, ?, ?)
            ''', (entry.title, entry.body, entry.isoTime, entry.lat, entry.lon))
    
    conn.commit()
    conn.close()

init_db()

@app.get("/health")
async def health_check():
    return "OK"

@app.get("/entries", response_model=List[LogEntry])
async def get_entries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, body, isoTime, lat, lon FROM entries ORDER BY isoTime ASC')
    rows = cursor.fetchall()
    conn.close()
    return [LogEntry(id=row[0], title=row[1], body=row[2], isoTime=row[3], lat=row[4], lon=row[5]) for row in rows]

@app.get("/entries/{entry_id}", response_model=LogEntry)
async def get_entry(entry_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, body, isoTime, lat, lon FROM entries WHERE id = ?', (entry_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Entry not found")
    
    return LogEntry(id=row[0], title=row[1], body=row[2], isoTime=row[3], lat=row[4], lon=row[5])

@app.post("/entries", response_model=LogEntry, status_code=status.HTTP_201_CREATED)
async def create_entry(entry: LogEntry):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    iso_time = datetime.utcnow().isoformat() + "Z"
    cursor.execute('''
        INSERT INTO entries (title, body, isoTime, lat, lon)
        VALUES (?, ?, ?, ?, ?)
    ''', (entry.title, entry.body, iso_time, entry.lat, entry.lon))
    
    entry_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return LogEntry(id=entry_id, title=entry.title, body=entry.body, isoTime=iso_time, lat=entry.lat, lon=entry.lon)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)