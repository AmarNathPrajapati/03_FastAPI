from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from model.note import Note
from config.db import conn
from schema.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

note = APIRouter()
note.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Serve index.html from the static directory

# fastAPI to get all notes
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
        })

    return templates.TemplateResponse("index.html", {"request": request,"newDocs":newDocs})

# fastAPI to post the notes
@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    conn.notes.notes.insert_one(formDict)
    return {"Success": True}   