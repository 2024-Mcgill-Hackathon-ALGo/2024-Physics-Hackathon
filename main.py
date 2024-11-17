import arcade
from views import MainMenu


# Constants for the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Main Menu with Arcade GUI Buttons"

# Main function
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    main_menu = MainMenu.MainMenuView()
    main_menu.setup()
    
    # Show the main menu view
    window.show_view(main_menu)

    # Start the arcade window and game loop
    arcade.run()

if __name__ == "__main__":
    main()
