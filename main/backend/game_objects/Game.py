import time
from Player import *
class Game(object):
    def __init__(self, Player1):
        self.Player1 = Player1
        self.Player2 = None
        self.playerOneObj = None
        self.PlayerTwoObj = None

    def addPlayer(self, Player):
        self.Player2 = Player
    
    def instantiatePlayers(self):
        self.playerOneObj = Player(self.Player1, 100, 100, 1, 'Alive', 0, 0)
        self.PlayerTwoObj = Player(self.Player2, 100, 100, 1, 'Alive', 0, 0)




