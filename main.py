'''
    Fast Api based on the pydentic library
    It provide a base model and help in data validation
'''
from fastapi import FastAPI
from routes.note import note
app = FastAPI()
app.include_router(note)





