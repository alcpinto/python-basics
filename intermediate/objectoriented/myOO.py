import pygame
from objectoriented.myModel import *
import numpy as np
import logging


logging.basicConfig(filename='logfile.log', level=logging.INFO)

STARTING_BLUE_BLOBS = 15
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()


def draw_environment(blobs_list):
    blues, reds, greens = handle_collisions(blobs_list)
    game_display.fill(WHITE)
    for blob_dict in blobs_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            if type(blob) == BlueBlob:
                blob.__class__ = BlueBlob
                # blob.move_fast()
                blob.move()
            else:
                blob.move()
    pygame.display.update()
    return blues, reds, greens


def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y])-np.array([b2.x, b2.y])) < (b1.size + b2.size)


def handle_collisions(blob_list):
    blues, reds, greens = blob_list
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug('Checking if blobs touching {} + {}'.format(blue_blob, other_blob))
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]

    return blues, reds, greens


def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for _ in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for _ in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for _ in range(STARTING_GREEN_BLOBS)]))
    # black_blobs = dict(enumerate([Blob(BLACK, WIDTH, HEIGHT) for _ in range(7)]))
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs, red_blobs, green_blobs])
            clock.tick(60)
        except Exception as e:
            logging.critical(str(e))
            pygame.quit()
            quit()
            break

if __name__ == '__main__':
    main()
