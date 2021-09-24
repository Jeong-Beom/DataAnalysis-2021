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


@app.get('/iris', response_class = HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('iris.html',  {'request': request})

@app.get('/details/sl={sl}&sw={sw}&pl={pl}&pw={pw}', response_class = HTMLResponse)
async def read_iris(request: Request, sl: float, sw = float, pl = float, pw = float, result = str):
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from pandas.plotting import parallel_coordinates
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    from sklearn import metrics

    data = pd.read_csv('C:\\Workspace\\python\\Data_Science\\dataA\\분반(A반)\\data.csv')
    train, test = train_test_split(data, test_size = 0.4, stratify = data['species'], random_state = 42)
    X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
    y_train = train.species
    X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
    y_test = test.species
    mod_dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
    mod_dt.fit(X_train,y_train)
    prediction=mod_dt.predict(X_test)
    result = mod_dt.predict([[sl, sw, pl, pw]])[0]
    return templates.TemplateResponse('iris2.html', {'request': request, 'sl' : sl, 'sw' : sw, 'pl' : pl, 'pw': pw, 'result' : result})

uvicorn.run(app, port = 8000)

# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# app = FastAPI()

# @app.get('/iris/', response_class = HTMLResponse)
# async def iris_classifier(sl:float, sw:float, pl:float, pw:float):
#     species = mod_dt.predict([[sl,sw,pl,pw]])[0]
#     return templates.TemplateResponse("result.html",
#                                       {"request" : request,
#                                        "sl" : sl,
#                                        "sw" : sw,
#                                        "pl" : pl,
#                                        "pw" : pw
#                                        "result" : species})
                                       
# http://......../iris/?sl=1.2&sw=3.1&pl=3.0&pw=2.1