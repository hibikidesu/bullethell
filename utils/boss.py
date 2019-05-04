class Boss:

    def __init__(self, spin: int):
        self.direction = 180
        self.pos = [250, 100]
        self.spin = spin

    def update(self):
        self.direction = min(360, self.direction + self.spin)
        if self.direction >= 360:
            self.direction = 0
