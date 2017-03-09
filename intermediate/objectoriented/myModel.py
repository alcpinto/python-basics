import random
import logging


class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 8), movement_range=(-1, 2)):
        self.x = random.randrange(0, x_boundary)
        self.y = random.randrange(0, y_boundary)
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.movement = movement_range

    def __repr__(self):
        return 'Blob({},{},({},{}))'.format(self.color,
                                            self.size,
                                            self.x,
                                            self.y)

    def __str__(self):
        return "Color: {} blobject of size {}. Located at {},{}".format(self.color,
                                                                        self.size,
                                                                        self.x,
                                                                        self.y)

    def move(self):
        move_x = random.randrange(self.movement[0], self.movement[1])
        move_y = random.randrange(self.movement[0], self.movement[1])
        self.x += move_x
        self.y += move_y
        self.check_boundaries()

    def check_boundaries(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary


class BlueBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        super().__init__((0, 0, 255), x_boundary, y_boundary)

    def move_fast(self):
        self.x += random.randrange(-7, 7)
        self.y += random.randrange(-7, 7)
        self.check_boundaries()

    def __add__(self, other_blob):
        logging.info('Blob add op: {} + {}'.format(self.color, other_blob))
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size

        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0

        elif other_blob.color == (0, 0, 255):
            # for now, nothing. Maybe later it does something more.
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')


class RedBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        super().__init__((255, 0, 0), x_boundary, y_boundary)


class GreenBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        super().__init__((0, 255, 0), x_boundary, y_boundary)
