import arcade

from views.MainMenu import MainMenuView as main

class WinView(arcade.View):
    def __init__(self, elapsed_time):
        super().__init__()
        self.elapsed_time = elapsed_time
        
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
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You won! You are now a stable element!", self.window.get_size()[0]/2, self.window.get_size()[1] / 1.5, arcade.color.BLACK, 30, anchor_x="center")
        arcade.draw_text(f"Time: {self.elapsed_time:.2f}", self.window.get_size()[0]/2, self.window.get_size()[1] / 5, arcade.color.BLACK, 24, anchor_x="center")
        
        self.manager.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
            
    
    def goToMainMenu(self, event):
        print("Returning to the main menu")
        main_menu = main()
        main_menu.setup()
        self.window.show_view(main_menu)
        self.manager.disable()
