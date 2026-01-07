
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status":"running"}

@app.get("/info")
def info():
    return {"system":"MT5 AI Trading Ultimate"}
