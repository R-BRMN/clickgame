import time
from clickgame import ClickGame
from game_menu import GameMenu

if __name__ == '__main__':
    click_game = ClickGame()
    click_game.play_game()

#    click_game_menu = GameMenu(options=[{"command":print, "text":"Print"}, {"command":time.sleep, "text":"sleep"}])
#    click_game_menu.menu_do(1, "works")
#    click_game_menu.menu_do(2, 5)
