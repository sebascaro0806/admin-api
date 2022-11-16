from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import HTTPBearer
from src.config.setup import settings

user = APIRouter()
security = HTTPBearer()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url=settings.URL_PREFIX + '/docs',
    redoc_url=settings.URL_PREFIX + '/redoc',
    openapi_url=settings.URL_PREFIX + '/openapi.json'
)

@user.get("/root", response_model=str, dependencies=[Depends(security)])
def root():
    return "Test " + settings.PROJECT_NAME

app.include_router(user, prefix=settings.URL_PREFIX)


