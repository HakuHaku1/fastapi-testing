
from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/check_password", response_class=HTMLResponse)
async def check_password_get(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="check_password.html",
        context={"email": "", "password": ""}
    )


@app.post("/check_password", response_class=HTMLResponse)
async def check_password(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    return templates.TemplateResponse(
        request=request,
        name="check_password.html",
        context={"email": email, "password": password}
    )