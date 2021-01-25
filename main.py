# space invaders

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 720
HEIGHT = 1000
TITLE = "SPACE INVADERS"
NUM_ROWS = 8

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/space_invader_ship.jpg")
        # scaling the image down .5x
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()
        self.vel_x = 0

    def update(self):
        self.rect.x += self.vel_x

        if self.rect.top < HEIGHT - 100:
            self.rect.top = HEIGHT - 100

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self, y_coord):
        """
        Arguments:
            y_coord - initial y=coordinate
        """
        super().__init__()

        self.image = pygame.image.load("./images/space_invader_1.jpg")
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.image.set_colorkey(WHITE)


        self.rect = self.image.get_rect()

        # initial location middle of the screen at y_coord
        self.rect.centerx = WIDTH / 2
        self.rect.centery = y_coord

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        """
        Arguments:
            coords - tuple of x, y
        """
        self.image = pygame.image.load("./images/bullet.png")
        # scale to 22x36px
        self.image = pygame.transform.scale(self.image, (22, 36))

        self.rect = self.image.get_rect()
        # Start the bullet at coords
        self.rect.centerx, self.rect.bottom = coords

        self.y_vel = -3

    def update(self):
        self.rect.y += self.y_vel


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite Groups
    all_sprites = pygame.sprite.RenderUpdates()
    enemy_sprites = pygame.sprite.Group()
    player_bullet_sprites = pygame.sprite.Group()

    #   --- enemies
    for i in range(NUM_ROWS):
        # enemy 1
        enemy = Enemy(100 + i * 75)
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 2
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x - 80
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 3
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x - 155
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 4
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x - 230
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 5
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x - 305
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 6
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x + 80
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 7
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x + 155
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 8
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x + 230
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        # enemy 9
        enemy = Enemy(100 + i * 75)
        enemy.rect.x = enemy.rect.x + 305
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    #   --- player
    player = Player()
    all_sprites.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(player_bullet_sprites) < 3:
                    # create a bullet
                    bullet = Bullet(player.rect.midtop)
                    all_sprites.add(bullet)
                    player_bullet_sprites.add(bullet)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.vel_x < 0:
                    player.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.go_right()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d and player.vel_x < 0:
                    player.stop()

        # ----- LOGIC
        all_sprites.update()

        # check if every bullet had collided with enemy
        for bullet in player_bullet_sprites:
            # Kill if off screen
            if bullet.rect.bottom < 0:
                bullet.kill()

            # Enemy collision
            enemies_hit_group = pygame.sprite.spritecollide(bullet, enemy_sprites, True)
            if len(enemies_hit_group) > 0:
                bullet.kill()


        # ----- DRAW
        screen.fill(WHITE)
        # draw
        dirty_rectangles = all_sprites.draw(screen)

        # ----- UPDATE
        # update only dirty rectangles
        pygame.display.update(dirty_rectangles)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()