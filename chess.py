from game import Game
from game_objects import Board, King
import config as c
import pygame

class Chess(Game):
    def __init__(self):
        super(Chess, self).__init__()
        self.create_objects()
    def create_objects(self):
        self.objects.append(Board())
        self.create_king([4, 7], "white")
    def create_king(self, pos, color):
        k = King(pos, color)
        self.objects.append(k)
        self.handlers_mouse_event.append(k.handle)
    
Chess().run()
