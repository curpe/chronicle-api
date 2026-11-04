# Ticket 2
# Defining Pydantic Schemas

from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel): #--> What the client sends
    title: str
    content: str

class NoteResponse(NoteCreate): #--> What the server sends back + adds stamps (id, created_at)
    id: int
    created_at: datetime