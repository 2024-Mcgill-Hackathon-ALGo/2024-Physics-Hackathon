from arcade import Window
import arcade


def view_graph():
    arcade.draw_lrtb_rectangle_outline(100, 200, 300, 200, color=(0, 255, 0))


if __name__ == '__main__':
    class Win(Window):
        def __init__(self):
            super().__init__()

        def setup(self):
            self.background_color = (0, 0, 0)

        def on_draw(self):
            view_graph()


    def main():
        window = Win()

        arcade.run()


    main()
