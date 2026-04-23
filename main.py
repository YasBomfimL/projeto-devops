import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Olá": "Mundo"}

@app.get("/teste")
def teste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/ci")
def ci():
    return {"ci": "ok"}

## Teste discord