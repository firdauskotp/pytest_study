from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
db=[]

class FE4(BaseModel):
    name: str
    char_class: str

@app.get('/')
def index():
    return{'test':'value'}

@app.get('/characters')
def get_characters():
    return db

@app.post('/characters')
def create_characters(character: FE4):
    db.append(character.dict())
    return db[-1]

@app.delete('/characters/{char_id}')
def delete_char(char_id:int):
    db.pop(char_id-1)
    return{}

@app.get('/characters/{char_id}')
def get_spefcharacter(char_id:int):
    return db[char_id-1]