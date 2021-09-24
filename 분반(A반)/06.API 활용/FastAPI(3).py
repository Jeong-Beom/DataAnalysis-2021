from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

app = FastAPI()

app.mount('/static', StaticFiles(directory = 'C:\\Workspace\\python\\Data_Science\\분반(A반)\\06.API 활용\\static'), name = 'static')
templates = Jinja2Templates(directory = 'C:\\Workspace\\python\\Data_Science\\분반(A반)\\06.API 활용\\templates')

@app.get('/')
def read_root():
    return {'Hello' : 'World'}

@app.get('/items/{id}', response_class = HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse('item.html', {'request': request, 'id' : id})

uvicorn.run(app, port = 8000)