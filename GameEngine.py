import logging
import random
from enum import Enum
from datetime import datetime


# from typing import List

# states for the game engine
class GameState(Enum):
    PREGAME = 1  # before the game
    PLAY = 2  # in play
    RESULT = 3  # precessing player choice and return result
    GAMEEND = 4  # game end


# Types of card
class Card(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    DYNAMITE = -1


class Player:
    def __init__(self):
        self.cards: list[Card] = []

    def GetCards(self) -> list[Card]:
        return self.cards

    def GetCardsNum(self) -> int:
        return len(self.cards)



class Session:
    def __init__(self, ID: int):
        self.ID = ID
        self.player_Human = Player()
        self.player_AI = Player()



class GameEngine:
    currentGameState: GameState = GameState.PREGAME
    currentSession: Session
    allSessions: list[Session]  # this should be a hash table or dic
    numberOfCards: int = 5

    #
    # def __init__(self):
    #     self.cu

    def StartGame(self):
        # set up players
        self.currentSession = Session(int(datetime.now().timestamp()))
        # TODO: check if ID conflicts with other sessions
        # deal the cards
        self.DealCards()

        return

    def DealCards(self) -> int:
        if not self.currentSession:
            return -1  # TODO: throw an error
        selectedCards: list[Card] = self.GenerateCards(self.numberOfCards)
        self.currentSession.player_Human.cards = selectedCards
        self.currentSession.player_AI.cards = selectedCards

        logging.info(f"Human Cards:{self.currentSession.player_Human.cards}")

        return 0

    def GenerateCards(self, numberOfCards: int) -> list[Card]:
        cards: list[Card] = []
        for x in range(0, numberOfCards):
            cards.append(random.choice(list(Card)))
        return cards

    # return 1 for card 1 win, 2 for card 2, 0 for draw
    def CompareLogic(self, Card1: Card, Card2: Card) -> int:
        # draw
        if Card1 == Card2:
            return 0
        # Dyno
        if Card1 == Card.DYNAMITE:
            return 1
        if Card2 == Card.DYNAMITE:
            return 2

        # Rules:
        # Rock beats Scissor
        # Scissor beats Paper
        # Paper beats Rock
        wins = {
            Card.ROCK: Card.SCISSOR,
            Card.SCISSOR: Card.PAPER,
            Card.PAPER: Card.ROCK,
        }

        if wins[Card1] == Card2:
            return 1  # Card1 wins
        else:
            return 2  # Card2 wins

    def PlayCard(self, card: Card) -> int:
        PlayerCard = card
        AICard = random.choice(list(Card))
        result = self.CompareLogic(PlayerCard, AICard)
        return result

    def GetHand_Player(self) -> list[Card]:
        if not self.currentSession:
            logging.error("Game session not running")
            return []
        human:Player = self.currentSession.player_Human
        if not human:
            logging.error("Human is none")
            return []
        cards = human.GetCards()
        return cards


GE: GameEngine = GameEngine()
GE.StartGame()
# print(GE.currentSession.player_Human.cards)
print(GE.GetHand_Player())

# x = GE.currentSession.player_Human.cards[3]
# y = GE.currentSession.player_AI.cards[3]
# print(x)
# print(y)
#
#
# print(GE.CompareLogic(x,y))
