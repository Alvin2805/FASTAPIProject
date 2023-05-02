from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# manual function that created using basic libraries in python
import utils.AddControllers
from utils.AddModels import addModels

app = FastAPI()

# utilized for incoming request from Front End / API Gateway
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


addModels()

app.include_router(utils.AddControllers.populated_router)
