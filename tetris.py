import sys

import pygame

from game.main import run


pygame.init()


try:
    if __name__ == "__main__":
        run()
except Exception as e:
    print(f'An error occurred during startup: {e}')
finally:
    pygame.quit()
    sys.exit()
