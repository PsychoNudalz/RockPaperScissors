import uvicorn
import nest_asyncio
import threading
import time

from fastapi import FastAPI
from GameEngine import *
import logging

# Patch Jupyter's event loop
nest_asyncio.apply()

# -----------------------
# Define the FastAPI app
# -----------------------
app = FastAPI()




# -----------------------
# Server controls
# -----------------------
server = None
thread = None

def start_server():
    global server, thread
    config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    print("Server running at http://127.0.0.1:8000")

def stop_server():
    global server
    if server:
        server.should_exit = True
        print("Stopping server...")


@app.get("/ping")
def ping():
    return {"status": "alive"}

@app.get("/start")
def start_game():
    GE.StartGame()
    return {"message": "Rock, Paper, Scissors, Dynamite has begun!"}


@app.post("/play")
def play_game(move: str):
    if move not in choices:
        return {"error": "Invalid move"}
    logging.info(f"Player {move} is playing")



#Starting the App
choices = ["rock", "paper", "scissors", "dynamite"]
GE: GameEngine = GameEngine()


