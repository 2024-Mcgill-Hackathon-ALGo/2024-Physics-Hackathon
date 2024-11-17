import arcade

from views.MainMenu import MainMenuView

# Constants for the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Main Menu with Arcade GUI Buttons"


# Main function
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    main_menu = MainMenuView()
    main_menu.setup()

    window.show_view(main_menu)
    arcade.run()


if __name__ == "__main__":
    main()

