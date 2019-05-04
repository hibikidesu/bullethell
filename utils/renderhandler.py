import pygame
from .bullet import UserBullet, EnemyBullet
from .boss import Boss


class RenderHandler:

    def __init__(self, game):
        self.game = game
        self.started = False
        self.font = pygame.font.Font(None, 20)
        self.key_start = 0
        self.bullet_start = 0
        self.boss_bullet_time = 0
        self.player_bullets = []
        self.boss_bullets = []
        self.boss = Boss(30)

    def __debug(self):
        self.game.screen.blit(self.font.render("{} FPS".format(int(self.game.clock.get_fps())), True, (0, 0, 0)), (10, 10))
        self.game.screen.blit(self.font.render("Tick: {}ms".format(self.game.ms), True, (0, 0, 0)), (10, 25))
        self.game.screen.blit(self.font.render("Bullets: {}".format(len(self.player_bullets) + len(self.boss_bullets)), True, (0, 0, 0)), (10, 40))

    def render(self):
        if self.game.clock.get_fps() >= 1:
            self.started = True

        if self.started:
            tick = round(1000 / self.game.clock.get_fps())
            self.game.ms += tick
            self.game.screen.fill((240, 240, 240))

            self.__debug()
            self.key_start += tick
            self.bullet_start += tick
            self.boss_bullet_time += tick

            if self.key_start >= 20:
                keys = pygame.key.get_pressed()
                speed = 6
                if keys[pygame.K_LSHIFT]:
                    speed = 3
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    self.game.movement_controller.move_y(-speed)
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.game.movement_controller.move_y(speed)
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    self.game.movement_controller.move_x(-speed)
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    self.game.movement_controller.move_x(speed)
                if keys[pygame.K_SPACE] or keys[pygame.K_z]:
                    self.player_bullets.append(UserBullet([self.game.movement_controller.pos[0],
                                                           self.game.movement_controller.pos[1] - 10], 20))

                self.key_start = 0

            if self.boss_bullet_time >= 70:
                self.boss.update()
                self.boss_bullets.append(EnemyBullet(self.boss.pos[0], self.boss.pos[1], 10, self.boss.direction))
                self.boss_bullet_time = 0

            if self.bullet_start >= 10:
                for i, bullet in enumerate(self.boss_bullets):
                    if bullet.y not in range(-50, 750):
                        self.boss_bullets.pop(i)
                    else:
                        bullet.update()
                for i, bullet in enumerate(self.player_bullets):
                    if bullet.pos[1] not in range(-50, 750):
                        self.player_bullets.pop(i)
                    else:
                        bullet.update()
                self.bullet_start = 0

            pygame.draw.circle(self.game.screen, (0, 0, 0), self.game.movement_controller.pos, 15, 0)
            pygame.draw.circle(self.game.screen, (255, 0, 0), self.boss.pos, 15, 0)

            for bullet in self.player_bullets:
                pygame.draw.circle(self.game.screen, (0, 0, 0), bullet.pos, 10)
            for bullet in self.boss_bullets:
                pygame.draw.circle(self.game.screen, (0, 0, 0), [bullet.x, bullet.y], 10)

            pygame.display.flip()
