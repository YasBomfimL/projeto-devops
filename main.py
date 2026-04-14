from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Olá": "Mundo"}

@app.get("/teste")
def teste():
    return {"msg": "teste"}
