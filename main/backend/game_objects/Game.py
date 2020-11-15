import time

class Game(object):
    def __init__(self, Player1):
        self.Player1 = Player1
        self.Player2 = None

    def addPlayer(self, Player):
        self.Player2 = Player



