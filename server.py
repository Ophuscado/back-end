from fastapi import FastAPI
from player1dev.server import app as player1dev_app

app = FastAPI()
app.mount("/", player1dev_app)
