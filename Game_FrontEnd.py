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

def GECHeck(url: str) -> int:
    """
    Check if Game Engine is running
    :param url:
    :return: 0 - yes, 1 - no
    """
    resp = rq.get(url + "GECheck")
    if resp.json().get("error"):
        print(resp.json().get("error"))
        return 1
    return 0


def PlayCard(url: str, move: str) -> int:
    if GECHeck(url) != 0:
        return 1

    resp = rq.post(url + "play?move=" + move)
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

    return 0


def GetScore(url: str) -> int:
    if GECHeck(url) != 0:
        return 1

    resp = rq.get(url + "score")
    # print(resp.json())
    print(f"Human: {resp.json().get("human")}")
    print(f"AI: {resp.json().get("ai")}")

    return 0