from fastapi import FastAPI, APIRouter

user = APIRouter()
app = FastAPI(
    title="API Test",
    description="API to manage users",
    version=1.0,
    docs_url='/administration/api/v1/docs',
    redoc_url='/administration/api/v1/redoc',
    openapi_url='/administration/api/v1/openapi.json'
)

@user.get("/users", response_model=str)
def get_users():
    return "Hola Mundo"

app.include_router(user, prefix='/administration/api/v1')


