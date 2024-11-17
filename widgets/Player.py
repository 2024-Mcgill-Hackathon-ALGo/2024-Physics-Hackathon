import arcade
from arcade import Sprite

from widgets.ElementBox import category_colors


class Player(Sprite):
    def __init__(self, x, y, width, height, element):

        # initial position
        super().__init__()
        self.center_x = x
        self.center_y = y

        # initial size
        self.width = width
        self.height = height
        self.set_hit_box([(width / 2, height / 2),
                          (width / 2, -height / 2),
                          (-width / 2, -height / 2),
                          (-width / 2, height / 2)])

        # movement states
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        self.movement_speed = 5
        self.element = element

    def isColliding(self, x, y, width, height):
        # check if object is colliding with the player
        return self.center_x < x + width and self.center_x + self.width > x and self.center_y < y + height and self.center_y + self.height > y

    def draw(self, **kwargs):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height,
                                     arcade.color.WHITE)
        arcade.draw_rectangle_outline(self.center_x, self.center_y, self.width, self.height, arcade.color.BLACK, 2)
        arcade.draw_text(self.element.symbol, self.center_x - 15, self.center_y - 5, arcade.color.BLACK, 14, bold=True)
        arcade.draw_text(self.element.atomic_weight, self.center_x - 15, self.center_y + 10, arcade.color.BLACK, 9,
                         anchor_x="left")
        self.draw_hit_box(color=arcade.color.RED)

    def update(self, delta_time):
        if self.moving_up:
            self.center_y += self.movement_speed
        elif self.moving_down:
            self.center_y -= self.movement_speed
        elif self.moving_left:
            self.center_x -= self.movement_speed
        elif self.moving_right:
            self.center_x += self.movement_speed

    def stop_moving(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
