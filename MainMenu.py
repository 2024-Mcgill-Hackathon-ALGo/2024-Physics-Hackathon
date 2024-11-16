import arcade
import arcade.gui

# Constants for the screen
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Main Menu with Arcade GUI Buttons"


class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Background image var
        self.background = None

        # button layout
        self.v_box = arcade.gui.UIBoxLayout()

        # region buttons
        # Buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        settings_button = arcade.gui.UIFlatButton(text="Options", width=200)
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)

        # buttons added onto the layout
        self.v_box.add(start_button.with_space_around(bottom=20))
        self.v_box.add(settings_button.with_space_around(bottom=20))
        self.v_box.add(quit_button)

        # button events
        start_button.on_click = self.start_game
        settings_button.on_click = self.start_settings
        quit_button.on_click = self.quit_button
        # endregion buttons

        # Add the layout to the ui
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.v_box,
            )
        )

    def setup(self):
        try:
            # Load the background image
            self.background = arcade.load_texture(r"ressources\MainMenu\images\Atom-Desktop-Wallpaper-1183943868.jpeg")
        except FileNotFoundError:
            print("Background image not found. Ensure the path is correct.")
            self.background = None

    def on_draw(self):
        self.clear()

        # background color
        # arcade.set_background_color(arcade.color.BLACK)
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(
            0,
            0,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background
        )

        # draw the ui
        self.manager.draw()

        # Title
        arcade.draw_text(
            # text
            "ALGo periodic game",

            # position
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 150,

            # color
            arcade.color.BLACK,

            # font
            font_size=50,
            font_name="Kenney High Square",

            # alignment
            anchor_x="center"
        )

    def start_game(self, event):
        print("Start Game clicked")
        #

    def start_settings(self, event):
        print("Options clicked")
        #

    def quit_button(self, event):
        print("Quit clicked")
        arcade.close_window()


# Main function
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    main_menu = MainMenuView()
    main_menu.setup()

    window.show_view(main_menu)
    arcade.run()


if __name__ == "__main__":
    main()
