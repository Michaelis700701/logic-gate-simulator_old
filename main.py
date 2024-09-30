import pygame
from settings import *
from game import ChessBoard

class Main():
    def __init__(self) -> None:
        """
        Manages the screen and updating the program.
        """
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE | pygame.SCALED).convert_alpha()
        self.clock = pygame.time.Clock()
        self.app_state_manager = AppStateManager()

    def run(self) -> None:
        """
        Runs the while loop of the code 30 times every second and updates display.
        """
        while True:
            
            self.app_state_manager.run_state()
            
            pygame.display.update()
            self.clock.tick(30)
            #print(self.clock.get_fps())

class AppStateManager():
    def __init__(self) -> None:
        """
        Manages the current state that needs to run.
        """
        self.chess_board = ChessBoard()
        ACTIVE_STATE['active_state'] = 'chess_board'

    def run_state(self) -> None:
        """
        Runs which ever state is currently active.
        """
        if ACTIVE_STATE['active_state'] == 'chess_board':
            self.chess_board.run()

if __name__ == '__main__':
    main = Main()
    main.run()
    
    #profile.runctx('main.run()', globals(), locals())