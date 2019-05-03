import pygame


class EventHandler:

    def __init__(self, game):
        self.game = game

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.game.is_running = False
