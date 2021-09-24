from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from typing import List
import os
import uvicorn

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello' : 'World'}

@app.post('/uploadfiles')
async def creat_upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = './'
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), 'wb') as fp:
            fp.write(contents)
        print(file.filename)
    return {'filenames' : [file.filename for file in files]}

@app.get('/getfile/{fn}')
async def getFile(fn:str):
    file_path = os.getcwd() + '/' + fn
    return FileResponse(path = file_path, media_type = 'application/octet-stream', filename = fn)

uvicorn.run(app, port = 9000)