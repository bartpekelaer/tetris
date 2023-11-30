import pygame


pygame.init()
screen_width, screen_height = 800, 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Block Breaker')
clock = pygame.time.Clock()


def run():
    running = True
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            pass
        if keys[pygame.K_d]:
            pass

        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)
