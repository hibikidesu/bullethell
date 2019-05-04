import math
import cmath


class UserBullet:

    def __init__(self, pos: list, speed: int):
        self.pos = pos
        self.speed = speed

    def update(self):
        self.pos[1] -= self.speed


class EnemyBullet:

    def __init__(self, x, y, speed: int, direction: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = int(direction % 360)
        self._radian = math.radians(self.direction)

    def update(self):
        new_pos_as_clx = cmath.rect(self.speed, self._radian)
        self.x += int(new_pos_as_clx.real)
        self.y += int(new_pos_as_clx.imag)
        # self.x += round(math.sin(self.direction))
        # self.y += round(math.cos(self.direction))
