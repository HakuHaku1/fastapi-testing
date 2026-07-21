
from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/check_password", response_class=HTMLResponse)
async def check_password(request: Request, email: str = Form(...), password: str = Form(...)):
    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required.")
    return templates.TemplateResponse("check_password.html", {"request": request, "email": email})