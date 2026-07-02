"""
Простой backend для приёма данных о сканировании QR-кодов из Mini App.
Требуется: pip install fastapi uvicorn
Запуск: uvicorn server:app --host 0.0.0.0 --port 8000
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Раздаём статику (index.html и все ассеты Mini App)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

DB_FILE = "scans.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.post("/api/scan")
async def scan_qr(request: Request):
    payload = await request.json()
    db = load_db()
    db.append(payload)
    save_db(db)
    return {"status": "ok", "coins_earned": 50}
