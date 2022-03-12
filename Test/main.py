from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

templates = Jinja2Templates(directory="templates") 

app = FastAPI()

# 设置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextArea(BaseModel):
    content: str


@app.post("/add")
async def post_textarea(data: TextArea):
    print(data.dict())
    return {**data.dict()}


@app.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})