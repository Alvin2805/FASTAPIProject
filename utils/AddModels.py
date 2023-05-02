import importlib
import os
from configs.database import engine


def addModels():
    moduleNamesOST = os.listdir("models")
    for moduleName in moduleNamesOST:
        name, ext = os.path.splitext(moduleName)
        if ext == ".py":
            module = importlib.import_module("models." + name)
            module.SQLModel.metadata.create_all(engine)
