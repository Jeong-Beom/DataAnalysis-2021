from typing import Optional
from fastapi import FastAPI
from starlette.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel

import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.parse import quote

app = FastAPI()

@app.get('/', response_class = HTMLResponse)
def read_movie_rank():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # 화면없이 실행
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('C:\\Users\\Bestc\\Desktop\\빅데이터 지능형 서비스 개발과정(멀티캠퍼스)\\설치프로그램\\Selenium\\chromedriver.exe', options = options)
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('.list_ranking').text
    driver.close()
    import re
    content_change = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣0-9: ]','/', content)
    raw_contents_list = content_change.split('//')
    contents_list = []
    for v in raw_contents_list:
        if v not in contents_list and v != '':
            contents_list.append(v)
    contents_list = [str(contents).replace('/', '') for contents in contents_list][2:]
    for contents in contents_list:
        try:
            int(contents)
            del contents_list[contents_list.index(contents)]
        except:
            pass
    movie_list = []
    for i in range(50):
        movie_list.append([i+1, contents_list[i]])
    result = ''
    for i in range(len(movie_list)):
        result += f'<p>{movie_list[i][0]}위 : {movie_list[i][1]}\n'
    return result


@app.get('/rank/{top}', response_class = HTMLResponse)
async def read_movie_rank(top: int):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # 화면없이 실행
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('C:\\Users\\Bestc\\Desktop\\빅데이터 지능형 서비스 개발과정(멀티캠퍼스)\\설치프로그램\\Selenium\\chromedriver.exe', options = options)
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('.list_ranking').text
    driver.close()
    import re
    content_change = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣0-9: ]','/', content)
    raw_contents_list = content_change.split('//')
    contents_list = []
    for v in raw_contents_list:
        if v not in contents_list and v != '':
            contents_list.append(v)
    contents_list = [str(contents).replace('/', '') for contents in contents_list][2:]
    for contents in contents_list:
        try:
            int(contents)
            del contents_list[contents_list.index(contents)]
        except:
            pass
    movie_list = []
    for i in range(50):
        movie_list.append([i+1, contents_list[i]])
    result = ''
    for i in range(top):
        result += f'<p>{movie_list[i][0]}위 : {movie_list[i][1]}\n'
    return result

uvicorn.run(app, port = 8000)