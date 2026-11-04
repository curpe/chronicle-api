# Ticket 5
# Create CRUD Function

from database import get_db_connection

def insert_note(title: str, content: str):
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content) # --> insert note will connected and stored to this placeholder
        # and passes to INSERT INTO syntax VALUES
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


# Ticket 6
# Wire insert_note

def get_entire_notes():
    conn = get_db_connection()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return notes

def note_by_id(note_id: int):
    conn = get_db_connection()
    note = conn.execute("SELECT * FROM notes WHERE id = ?",(note_id, )).fetchone()
    conn.close()
    return note

# Ticket 7
# delete feature

def delete_note(note_id: int):
    conn = get_db_connection()
    conn.execute("DELETE FROM notes WHERE id = ?",(note_id, ))
    conn.commit() # Commit() to change within the database, safety
    conn.close()

# Ticket 8
# update_note
def update_note(note_id: int, title: str, content: str):
    conn = get_db_connection()
    conn.execute(
        "UPDATE notes SET title = ?, content = ? WHERE id = ?",
        (title, content, note_id)
    )
    conn.commit()
    conn.close()

