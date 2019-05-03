class Bullet:

    def __init__(self, pos: list, speed: int):
        self.pos = pos
        self.speed = speed

    def update(self):
        self.pos[1] -= self.speed
