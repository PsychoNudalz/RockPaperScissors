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

    move = move.lower()
    resp = rq.post(url + "play?move=" + move)
    json = resp.json()
    if json.get("error"):
        # logging.error(json.get("error"))
        print(json.get("error"))
        return 1

    result = json.get("result")
    if not result and result != 0:
        print("Result not found.")
        return 3

    if result == 1:
        print("Win")
    elif result == 2:
        print("Lose")
    elif result == 0:
        print("Draw")
    elif result == 3:
        print(f"You don't have a '{move}' Card")
        return 2

    return 0


def GetScore(url: str) -> int:
    if GECHeck(url) != 0:
        return 1

    resp = rq.get(url + "score")
    # print(resp.json())
    print(f"Human: {resp.json().get("human")}")
    print(f"AI: {resp.json().get("ai")}")

    return 0