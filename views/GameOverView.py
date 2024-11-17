import math

import arcade
import arcade.gui
import time as time_module

from services.utils import convert_year_float
from views.MainMenu import MainMenuView as main


class GameOverView(arcade.View):
    def __init__(self, time):
        super().__init__()
        self.time = time or 0 # time  
        self.displayed_time = 0  # for animation
        self.last_update_time = time_module.time()  

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
        arcade.draw_text("Game Over", self.window.get_size()[0] / 2, self.window.get_size()[1] / 1.5,
                         arcade.color.WHITE, 54, anchor_x="center")

        if self.time is not None:
            year, months, days,  hours, minutes, seconds = convert_year_float(self.time)
            height_offset = 40
            arcade.draw_text(f"Your time was... {year} Years, \n",
                             self.window.get_size()[0] / 2, self.window.get_size()[1] / 4 + (height_offset:=height_offset - 40),
                             arcade.color.YELLOW, 24, anchor_x="center")

            arcade.draw_text(f"{months} Months, {days} Days, {hours} Hours, {minutes} Minutes, ",
                             self.window.get_size()[0] / 2, self.window.get_size()[1] / 4 + (height_offset:=height_offset - 40),
                             arcade.color.YELLOW, 24, anchor_x="center")

            arcade.draw_text(f"\n{seconds:.2f} seconds",
                             self.window.get_size()[0] / 2, self.window.get_size()[1] / 4 + height_offset - 40,
                             arcade.color.YELLOW, 24, anchor_x="center")

        self.manager.draw()

    def update(self, delta_time: float):
        pass
        # Here I wanted to animate the time and make it look like it's counting up
        # if this randomly breaks something feel free to delete it and just display the time as is
        #current_time = time_module.time()
        #if self.displayed_time < self.time:
        #    elapsed_since_last_update = current_time - self.last_update_time
        #    self.displayed_time += elapsed_since_last_update * 5  # Speed up animation
        #    self.displayed_time = min(self.displayed_time, self.time)
         #   self.last_update_time = current_time

    def goToMainMenu(self, event):
        print("Returning to the main menu")
        main_menu = main()
        main_menu.setup()
        self.window.show_view(main_menu)
        self.manager.disable()


if __name__ == "__main__":
    window = arcade.Window(800, 600, "Game")
    game_view = GameOverView(123.45)  # Pass a sample time
    window.show_view(game_view)
    arcade.run()
