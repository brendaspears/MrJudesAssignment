import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from tiger import Tiger

from alien import Alien

import game_functions as gf

def run_game():

    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a tiger, a group of bullets, and a group of aliens.
    # Make a tiger.
    tiger = Tiger(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, tiger, aliens)

    # Set the background color.
    bg_color = (180, 190, 250)

    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Start the main loop for the game.
    while True:

        gf.check_events(ai_settings, screen, tiger, bullets)

        if stats.game_active:

            tiger.update()

            gf.update_bullets(ai_settings, screen, tiger, aliens, bullets)

            gf.update_aliens(ai_settings ,stats , screen , tiger , aliens , bullets)

        gf.update_screen(ai_settings, screen, tiger, aliens, bullets)




run_game()
