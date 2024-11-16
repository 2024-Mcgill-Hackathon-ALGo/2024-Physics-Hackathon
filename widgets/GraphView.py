from arcade import Window
import arcade
import arcade.color

from main import SCREEN_WIDTH, SCREEN_HEIGHT


def view_graph():
    arcade.draw_lrtb_rectangle_filled((SCREEN_WIDTH / 8) * 5, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                       arcade.color.GRAY)
    arcade.draw_lrtb_rectangle_outline((SCREEN_WIDTH / 8) * 5, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                       arcade.color.GREEN)
    arcade.draw_line((SCREEN_WIDTH / 8) * 5, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT / 2, arcade.color.GREEN)

def view_circle():
    arcade.draw_circle_filled((SCREEN_WIDTH/10)*7 , (SCREEN_HEIGHT/100)*89, 20,
                              arcade.color.GREEN)
    arcade.draw_line((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/100)*87 , (SCREEN_WIDTH/10)*7 , (SCREEN_HEIGHT/100)*74, arcade.color.ORANGE_RED,2)
    arcade.draw_circle_outline((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/100)*89, 20,
                              arcade.color.ORANGE_RED)
    arcade.draw_circle_filled((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/4)*3, 20,
                              arcade.color.YELLOW)
    arcade.draw_circle_outline((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/4)*3, 20,
                              arcade.color.ORANGE_RED)
    arcade.draw_circle_filled((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/8)*3, 20,
                              arcade.color.YELLOW)
    arcade.draw_circle_outline((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/8)*3, 20,
                              arcade.color.ORANGE_RED)
    arcade.draw_circle_outline((SCREEN_WIDTH/2), (SCREEN_HEIGHT/20)*13, 10,
                              arcade.color.GREEN)
    arcade.draw_circle_outline((SCREEN_WIDTH/4), (SCREEN_HEIGHT/20)*13, 30,
                              arcade.color.GREEN)



if __name__ == '__main__':
    class Win(Window):
        def __init__(self):
            super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        def setup(self):
            self.background_color = (0, 0, 0)

        def on_draw(self):
            self.clear()
            # arcade.start_render()
            view_graph()
            view_circle()
            # arcade.finish_render()
            


    def main():
        window = Win()
        window.setup()
        
        arcade.run()


    main()
