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


def start_server(ip: str = "127.0.0.1", port: int = 8000):
    global server, thread
    config = uvicorn.Config(app=app, host=ip, port=port, log_level="info")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    logging.info(f"Server running at http://{ip}:{port}/")


def stop_server():
    global server
    if server:
        server.should_exit = True
        logging.info("Stopping server...")


@app.get("/ping")
def ping():
    return {"status": "alive"}

@app.get("/GECheck")
def GECheck():
    global GE
    if not GE:
        logging.error("Game Engine not running")
        return {"error": "Game engine not running"}
    return {"message": "Game Engine is running"}


@app.get("/start")
def start_game():
    GE.StartGame()
    # display_hand()
    return {"message": "Rock, Paper, Scissors, Dynamite has begun!"}


@app.post("/play")
def play_card(move: str):
    global GE

    if move not in ["rock", "paper", "scissors", "dynamite"]:
        logging.error(f"Invalid move: {move}")
        return {"error": "Invalid move"}
    if not GE:
        logging.error("Game Engine not running")
        return {"error": "Game engine not running"}
    logging.info(f"Player {move} received")

    card: Optional[Card] = None

    if move == "rock":
        card: Card = Card.ROCK
    elif move == "paper":
        card: Card = Card.PAPER
    elif move == "scissors":
        card: Card = Card.SCISSOR
    elif move == "dynamite":
        card: Card = Card.DYNAMITE

    if not card:
        return {"error": "Invalid move"}

    logging.info(f"Player {card} is playing")
    result : int =  GE.PlayCard(card)
    return {"result": result}


@app.get("/display")
def display_hand():
    global GE
    if not GE:
        logging.info("Game engine not running")
        return {"message": "Game engine not running"}
    PlayerHand = GE.GetHand_Player()
    HandStr = [str(card.name) for card in PlayerHand]  # Convert Enum -> str
    logging.info(f"Player hand: {HandStr}")
    return {"hand": str(HandStr)}

@app.get("/test")
def test():
    return {"test": "test"}

@app.get("/score")
def get_score():
    human, ai = GE.GetScore()
    return {"human": human, "ai": ai}

# Starting the App
GE: GameEngine = GameEngine()
