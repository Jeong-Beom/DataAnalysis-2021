from typing import Optional
from fastapi import FastAPI
import uvicorn
from fastapi import APIRouter
from pydantic import BaseModel
from schemas import Recipe, RecipeCreate, RecipeSearchResults

app = FastAPI()
router = APIRouter()

class Course(BaseModel):
    name : str
    description: Optional[str] = None
    price: int
    author: Optional[str] = None

@app.post('/courses')
def creat_course(course: Course):
    print('course name:' + course.name)
    if course.description is not None:
        print('description:' + course.description)
    print('price:' + str(course.price))
    if course.author is not None:
        print('author:' + course.author)
    return course

@app.get('/')
def read_root():
    return {'Hello' : 'World'}

@app.get('/items/{item_id}') # 예시 : http://127.0.0.1:8000/items/4?q=test
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}

coures_items = [{'course_name': 'Python'}, {'course_name': 'SQLAlchemy'}, {'course_name': 'NodeJS'}]

@app.get('/courses/{course_name}')
def read_courses(start: int, end: int):
    return coures_items[start: start + end]

@router.get('/recipe/{recipe_id}', status_code = 200)
def fetch_recipe(*,recipe_id: int) -> dict:
    result = [recipe for recipe in RECIPES if recipe['id'] == recipe_id]
    if result:
        return result[0]

RECIPES = [
    {
        'id' : 1,
        'label' : 'Chicken Vesuvio',
        'source' : 'Serious Eats',
        'url' : 'https://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html'
    },
    {
        'id' : 2,
        'label' : 'Chicken Paprikash',
        'source' : 'No Recipes',
        'url' : 'https://norecipes.com/recipe/chicken-paprikash/'
    },
    {
        'id' : 3,
        'label' : 'Cauliflower and Tofu Curry Recipe',
        'source' : 'Serious Eats',
        'url' : 'https://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html'
    }
]


uvicorn.run(app, port = 8000) # http://127.0.0.1:8000/docs로 오류시 발생 메세지 등 추가사항들 확인가능(http://127.0.0.1:8000/redoc)