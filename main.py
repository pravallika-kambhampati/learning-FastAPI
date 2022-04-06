from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Data": "Hello World"}


@app.get("/about")
def about():
    return {"Data":"About"}