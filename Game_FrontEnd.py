# import Game_API
import logging

import requests as rq

# def StartGame():

# def get(url:str,req:str) -> requests.Response:
#     return requests.get(url+req)
#
# def post(url:str,req:str) -> requests.Response:
#     return requests.post(url+req)

# def StartGame(url:str) -> requests.Response:
#     return requests.post(url)

def PlayCard(url:str, move:str):
    resp = rq.post(url + "play?move="+move)
    move = move.lower()
    json = resp.json()
    if json.get("error"):
        # logging.error(json.get("error"))
        print(json.get("error"))
    result = json.get("result")
    if result == 1:
        print("Win")
    elif result == 2:
        print("Lose")
    elif result == 0:
        print("Draw")




