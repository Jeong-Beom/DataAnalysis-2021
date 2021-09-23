from typing import Optional
from fastapi import FastAPI
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

