import math

import arcade

from views.MainMenu import MainMenuView as main
from widgets.Player import Player
from services.utils import convert_year_float

class WinView(arcade.View):
    def __init__(self, elapsed_time, stable_element):
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
        
        self.stable_element = stable_element
        
        self.player = Player(self.window.get_size()[0] / 2, self.window.get_size()[1] / 1.5, 50, 50,  self.stable_element)

    def on_show(self):
        arcade.set_background_color(arcade.color.GHOST_WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You won! You are now a stable element!", self.window.get_size()[0]/2, self.window.get_size()[1] / 1.25, arcade.color.BLACK, 30, anchor_x="center")
        year, months, days, hours, minutes, seconds = convert_year_float(self.elapsed_time)

        height_offset = 40
        arcade.draw_text(f"Your time was... {year} Years, \n",
                         self.window.get_size()[0] / 2,
                         self.window.get_size()[1] / 4 + (height_offset := height_offset - 40),
                         arcade.color.BLACK, 24, anchor_x="center")

        arcade.draw_text(f"{months} Months, {days} Days, {hours} Hours, {minutes} Minutes, ",
                         self.window.get_size()[0] / 2,
                         self.window.get_size()[1] / 4 + (height_offset := height_offset - 40),
                         arcade.color.BLACK, 24, anchor_x="center")

        arcade.draw_text(f"\n{seconds:.2f} seconds",
                         self.window.get_size()[0] / 2, self.window.get_size()[1] / 4 + height_offset - 40,
                         arcade.color.BLACK, 24, anchor_x="center")

        
        self.player.draw()
        
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
