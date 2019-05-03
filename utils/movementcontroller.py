class MovementController:

    def __init__(self, game):
        self.game = game
        self.pos = [250, 350]

    def move_x(self, amount: int):
        self.pos[0] += amount

    def move_y(self, amount: int):
        self.pos[1] += amount
