from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Хранилище заметок в памяти (для скорости разработки)
notes_db = []

class Note(BaseModel):
    title: str
    content: str

# API для получения всех заметок
@app.get("/api/notes", response_model=List[Note])
async def get_notes():
    return notes_db

# API для добавления заметки
@app.post("/api/notes")
async def add_note(note: Note):
    notes_db.append(note)
    return {"message": "Заметка добавлена!"}

# Главная страница
@app.get("/")
async def read_index():
    return FileResponse('index.html')