from fastapi import FastAPI

from app.api.login import router as login_router

app = FastAPI(
    title="Franke Network Solutions Monitor Manager",
    version="1.0.0"
)

app.include_router(
    login_router,
    prefix="/api"
)


@app.get("/")
def root():

    return {
        "application": "FNS Monitor Manager"
    }
