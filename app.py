import pygame
from utils import *


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("Bullethell")
        self.clock = pygame.time.Clock()

        self.is_running = False
        self.event_handler = EventHandler(self)
        self.movement_controller = MovementController(self)
        self.render_handler = RenderHandler(self)
        self.ms = 0

    def run(self):
        self.is_running = True

        while self.is_running:

            for event in pygame.event.get():
                self.event_handler.handle_event(event)

            self.render_handler.render()

            self.clock.tick(144)


if __name__ == "__main__":
    Game().run()
