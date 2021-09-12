import sqlite3
from typing import ContextManager
import sqlite3
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE


class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database():
    def __init__(self, banco):
        self.banco = banco
        self.conn = sqlite3.connect(self.banco+".db")
        cur = self.conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL)"
        cur.execute(sql)

    def add(self, note):
        self.note = note
        tasks = ((note.id), (note.title), (note.content))
        sql = "INSERT INTO note (id, title, content) VALUES (?,?,?)"
        cur = self.conn.cursor()
        cur.execute(sql, tasks)
        self.conn.commit()

    def get_all(self):
        sql = "SELECT id, title, content FROM note"
        cursor = self.conn.execute(sql)

        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id=id, title = title, content=content))

        return lista

    def update(self,entry):
        self.entry = entry
        sql1 = (f"UPDATE note SET title='{entry.title}' WHERE id={entry.id}")
        sql2 = (f"UPDATE note SET content='{entry.content}' WHERE id={entry.id}")

        self.conn.execute(sql1)
        self.conn.execute(sql2)

        self.conn.commit()

    def delete(self, note_id):
        sql = (f"DELETE FROM note WHERE id={note_id}")
        self.conn.execute(sql)
        self.conn.commit()
