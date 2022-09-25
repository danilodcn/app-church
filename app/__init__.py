"""Módulo Principal"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    """
        Função Home
    """
    return {"hello": "world"}
