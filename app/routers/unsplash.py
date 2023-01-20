import os
from fastapi import Request, APIRouter, Depends, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
load_dotenv()

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/unsplash", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    key = os.getenv("unsplash_key")
    print(key)
    return templates.TemplateResponse("unsplash.html", {"request": request})

@router.post("/unsplash")
def hello(data = Body(default=0)):
    name = data["name"]
    age = data["age"]
    return {"message": f"{name}, ваш возраст - {age}"}