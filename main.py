from fastapi import FastAPI, APIRouter
from src.config.setup import settings

user = APIRouter()
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url='/administration' + settings.URL_PREFIX + '/docs',
    redoc_url='/administration' + settings.URL_PREFIX + '/redoc',
    openapi_url='/administration' + settings.URL_PREFIX + '/openapi.json'
)

@user.get("/users", response_model=str)
def get_users():
    return "Hola Mundo despliegue"

app.include_router(user, prefix=settings.URL_PREFIX)


