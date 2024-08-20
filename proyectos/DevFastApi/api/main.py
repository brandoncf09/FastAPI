from fastapi import FastAPI
from .routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(products.router)
app.mount("/static", app)

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

@app.get("/url_google")
async def url_google():
    return {"url_curso":"https://www.google.com"}


