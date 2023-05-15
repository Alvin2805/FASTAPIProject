from fastapi import FastAPI
from controller import router
from config import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(router)