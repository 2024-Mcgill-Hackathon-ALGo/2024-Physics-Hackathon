from arcade import Window
import arcade
from MainMenu import SCREEN_WIDTH, SCREEN_HEIGHT


def view_graph():
    arcade.draw_lrtb_rectangle_outline((SCREEN_WIDTH / 8) * 7, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                       arcade.color.GREEN)
    arcade.draw_line((SCREEN_WIDTH / 8) * 7, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT / 2, arcade.color.GREEN)



if __name__ == '__main__':
    class Win(Window):
        def __init__(self):
            super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        def setup(self):
            self.background_color = (0, 0, 0)

        def on_draw(self):
            self.clear()
            arcade.start_render()
            view_graph()
            arcade.finish_render()


    def main():
        window = Win()
        window.setup()

        arcade.run()


    main()
