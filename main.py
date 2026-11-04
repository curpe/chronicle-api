from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from database import init_db
from crud import insert_note, get_entire_notes, note_by_id, delete_note, update_note
from summarize import summarize_content
from models import NoteCreate


# Ticket 4
# Create database from scratch using lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Ticket 1
# GET / route confirmation
@app.get("/")
def status():
    return {"status" : "ok" }

# Ticket 6
# POST /notes end point
@app.post("/notes")
def create_note(note: NoteCreate):
    new_id = insert_note(note.title, note.content)
    return {"id": new_id, "title": note.title, "content": note.content}


# GET /notes end point
@app.get("/notes")
def read_note():
    notes = get_entire_notes()
    return notes

# Put the id on endpoint, make a path parameter
@app.get("/notes/{note_id}")
def read_note_by_id(note_id: int):
    note = note_by_id(note_id)
    return note

# delete
@app.delete("/notes/{note_id}")
def get_note_delete(note_id: int):
    delete_note(note_id)
    return {"message": f"Note {note_id} deleted" }

# update
@app.put("/notes/{note_id}")
def patch_update_note(note_id: int, note: NoteCreate): # --> reusing NoteCreate is identical and ok
    update_note(note_id, note.title, note.content)
    return {"message": f"Note {note_id} has been updated!"}

# Ticket 9
# summarization endpoint using AI
# error handling if note does not found
# error handling if AI model doesn't work
# this endpoint is currently on patch -- 21 July 2026
@app.post("/notes/{note_id}/summarize")
def ai_summarize_note_endpoint(note_id: int):
    note = note_by_id(note_id)
    #error handling for database
    if not note:
        raise HTTPException(status_code=404, detail="Note not found in database")

    #error handling for AI
    try:
        summary = summarize_content(note["content"])
    except Exception as error_handling:
        print(f"\n[DEBUG] Caught error: {type(error_handling).__name__} - {error_handling}\n")
        raise HTTPException(status_code=429, detail="Summarization rate limit reached. Please try again in a minute")

    return {"id":note_id, "summary": summary}