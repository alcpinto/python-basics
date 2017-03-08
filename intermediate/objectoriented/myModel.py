import random


class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 8), movement_range=(-1, 2)):
        self.x = random.randrange(0, x_boundary)
        self.y = random.randrange(0, y_boundary)
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.movement = movement_range

    def move(self):
        move_x = random.randrange(self.movement[0], self.movement[1])
        move_y = random.randrange(self.movement[0], self.movement[1])
        self.x += move_x
        self.y += move_y

        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary
