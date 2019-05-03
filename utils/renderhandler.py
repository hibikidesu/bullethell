import pygame


class RenderHandler:

    def __init__(self, game):
        self.game = game
        self.started = False
        self.font = pygame.font.Font(None, 20)
        self.key_start = 0

    def __debug(self):
        self.game.screen.blit(self.font.render("{} FPS".format(int(self.game.clock.get_fps())), True, (0, 0, 0)), (10, 10))
        self.game.screen.blit(self.font.render("Tick: {}ms".format(self.game.ms), True, (0, 0, 0)), (10, 25))

    def render(self):
        if self.game.clock.get_fps() >= 1:
            self.started = True

        if self.started:
            self.game.ms += round(1000 / self.game.clock.get_fps())
            self.game.screen.fill((255, 255, 255))

            self.__debug()
            self.key_start += round(1000 / self.game.clock.get_fps())
            if self.key_start >= 20:
                keys = pygame.key.get_pressed()
                speed = 6
                if keys[pygame.K_LSHIFT]:
                    speed = 3
                if keys[pygame.K_w]:
                    self.game.movement_controller.move_y(-speed)
                if keys[pygame.K_s]:
                    self.game.movement_controller.move_y(speed)
                if keys[pygame.K_a]:
                    self.game.movement_controller.move_x(-speed)
                if keys[pygame.K_d]:
                    self.game.movement_controller.move_x(speed)
                self.key_start = 0

            pygame.draw.circle(self.game.screen, (0, 0, 0), self.game.movement_controller.pos, 15, 0)

            pygame.display.flip()