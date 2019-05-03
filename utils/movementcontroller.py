class MovementController:

    def __init__(self, game):
        self.game = game
        self.pos = [250, 350]

    def update(self):
        self.pos = [min(486, max(14, self.pos[0])), min(686, max(14, self.pos[1]))]

    def move_x(self, amount: int):
        self.pos[0] += amount
        self.update()

    def move_y(self, amount: int):
        self.pos[1] += amount
        self.update()
