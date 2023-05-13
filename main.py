from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import db


app = FastAPI()

import db_api

@app.get("/")
async def root():
    return {"message": "Hello World"}

