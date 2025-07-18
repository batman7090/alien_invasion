import sys
import pygame

from settings import Setting


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the mainloop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw teh screen during each pass through the loop
            self.screen.fill(self.setting.bg_color)
            
            # Make the most recently drawn screen visible
            pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion().run_game()