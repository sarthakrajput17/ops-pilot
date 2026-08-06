from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes.web import router as web_router
from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router
from app.api.routes.kubernetes import router as kubernetes_router
from app.api.routes.docker import router as docker_router
from app.api.routes.terraform import router as terraform_router
from app.api.routes.analyze import router as analyze_router
from app.api.routes.pdf import router as pdf_router


app = FastAPI(
    title="Ops-Pilot AI Service",
    version="2.0.0",
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse(
#         request=request,
#         name="index.html",
#         context={},
#     )


app.include_router(health_router)
app.include_router(chat_router)
app.include_router(kubernetes_router)
app.include_router(web_router)
app.include_router(docker_router)
app.include_router(terraform_router)
app.include_router(analyze_router)
app.include_router(pdf_router)