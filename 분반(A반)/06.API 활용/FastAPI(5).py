from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get('/iris/', response_class = HTMLResponse)
async def iris_classifier(sl:float, sw:float, pl:float, pw:float):
    species = mod_dt.predict([[sl,sw,pl,pw]])[0]
    return templates.TemplateResponse("result.html",
                                      {"request" : request,
                                       "sl" : sl,
                                       "sw" : sw,
                                       "pl" : pl,
                                       "pw" : pw
                                       "result" : species})
                                       
http://......../iris/?sl=1.2&sw=3.1&pl=3.0&pw=2.1