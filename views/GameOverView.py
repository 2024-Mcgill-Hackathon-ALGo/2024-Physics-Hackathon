import arcade
import arcade.gui

from views.MainMenu import MainMenuView as main

class GameOverView(arcade.View):
    def __init__(self, time=None):
        super().__init__()
        self.time = time
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        
        self.v_box = arcade.gui.UIBoxLayout()
        
        restart_button = arcade.gui.UIFlatButton(text="Return to main menu", width=200)
        
        self.v_box.add(restart_button.with_space_around(bottom=20))
        
        restart_button.on_click = self.goToMainMenu
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.v_box,
            )
        )

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Game Over", self.window.get_size()[0]/2, self.window.get_size()[1]/1.5, arcade.color.WHITE, 54, anchor_x="center")
        arcade.draw_text(f"time: {self.time}", 310, 300, arcade.color.WHITE, 24)
        
        self.manager.draw()

    def goToMainMenu(self, event):
        print("go to main menu")
        main_menu = main()
        main_menu.setup()
        self.window.show_view(main_menu)
        self.manager.disable()
        
if __name__ == "__main__":
    window = arcade.Window(800, 600, "Game")
    game_view = GameOverView(0)
    window.show_view(game_view)
    arcade.run()