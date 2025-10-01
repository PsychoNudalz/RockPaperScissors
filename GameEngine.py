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
    ROCK = 1,
    PAPER = 2,
    SCISSOR = 3,
    DYNAMITE = -1


class Player:
    cards: list[Card] = []

    #
    # def __init__(self):
    #     self.cards: list[Card] = []

    # getting list of cards back, will be used to display on the player
    def GetCards(self) -> list[Card]:
        return self.cards

    # get the number of cards back
    def GetCardsNum(self) -> int:
        return len(self.cards)


class Session:
    ID: int
    player_Human: Player = Player
    player_AI: Player = Player

    def __init__(self, ID: int):
        self.ID = ID


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

        selectedCards: list[Card] = self.SelectCards(self.numberOfCards)
        self.currentSession.player_Human.cards = selectedCards
        self.currentSession.player_AI.cards = selectedCards

    def SelectCards(self, numberOfCards: int) -> list[Card]:
        cards: list[Card] = []
        for x in range(0, numberOfCards):
            cards.append(random.choice(list(Card)))
        return cards

    #return 1 for card 1 win, 2 for card 2, 0 for draw
    def CompareLogic(self,Card1:Card,Card2:Card) -> int:
        #draw
        if Card1 == Card2:
            return 0
        #Dyno
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

# GE: GameEngine = GameEngine()
# GE.StartGame()
# x = GE.currentSession.player_Human.cards[3]
# y = GE.currentSession.player_AI.cards[3]
# print(x)
# print(y)
#
#
# print(GE.CompareLogic(x,y))
