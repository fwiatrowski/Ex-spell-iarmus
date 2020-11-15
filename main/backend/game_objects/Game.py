import time
from .Player import *
from .Spell import *
class Game(object):
    def __init__(self, Player1):
        self.Player1 = Player1
        self.Player2 = None
        self.playerOneObj = None
        self.playerTwoObj = None
        self.Cras = Spell('Cras',40,38,1)
        self.UtEu = Spell('Ut eu',25,23,1)
        self.SpellList = [self.Cras, self.UtEu]

    def addPlayer(self, Player):
        self.Player2 = Player
    
    def instantiatePlayers(self):
        self.playerOneObj = Player(self.Player1, 100, 100, 1, 'Alive', 0, 0)
        self.playerTwoObj = Player(self.Player2, 100, 100, 1, 'Alive', 0, 0)




