from fastapi import FastAPI

app = FastAPI(title="DMS Microservices")

@app.get("/")
def getroot():
    return {"hello":"world"}