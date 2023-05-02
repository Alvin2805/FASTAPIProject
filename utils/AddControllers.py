import importlib
import os
from fastapi import APIRouter

populated_router = APIRouter()


moduleNamesOST = os.listdir("controllers")
for moduleName in moduleNamesOST:
    name, ext = os.path.splitext(moduleName)
    if (ext == ".py"):
        module = importlib.import_module("controllers." + name)
        populated_router.include_router(module.router)
