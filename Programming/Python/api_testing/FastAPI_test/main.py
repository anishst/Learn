# https://fastapi.tiangolo.com/
# https://medium.com/@tiangolo/introducing-fastapi-fdc1206d453f
# https://www.youtube.com/watch?v=kCggyi_7pHg&t=814s

# pip install fastapi
# pip install uvicorn - ASGI server, for production such as uvicorn

# launch app by: uvicorn main:app --reload
# access by: http://127.0.0.1:8000/items/5?q=somequery.
# access UI interface for requests: http://127.0.0.1:8000/docs\

from fastapi import FastAPI, requests
from pydantic import BaseModel

app = FastAPI()


db = [
]

class City(BaseModel):
    name: str
    timezone: str


@app.get('/')
def index():
    return {'key' : 'value'}

@app.get('/cities')
def get_cities():
    return db

# @app.get('/cities')
# def get_cities():
#     results = []
#     for city in db:
#         r = requests.Request(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
#         current_time = r.json()['datetime']
#         results.append({'name' : city['name'], 'timezone': city['timezone'], 'current_time': current_time})
#     return results

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city = db[city_id-1]
    r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
    current_time = r.json()['datetime']
    return {'name' : city['name'], 'timezone': city['timezone'], 'current_time': current_time}

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}

