import pygame

from pygame.sprite import Sprite

class Tiger(Sprite):

    def __init__(self, ai_settings, screen):

        """Initialize the tiger and set its starting position."""
        super(Tiger , self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the tiger image and get its rect.
        self.image = pygame.image.load('image/piggy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new tiger at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the tiger's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the tiger's position based on the movement flags."""

        # Update the tiger's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.tiger_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.tiger_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the tiger at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_tiger(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom