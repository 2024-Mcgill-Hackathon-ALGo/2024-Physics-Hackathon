import arcade
from arcade import Sprite


class DecaySprint(Sprite):
    def __init__(self):
        super().__init__(hit_box_algorithm="None")
        self.radius = 20
        self.set_hit_box([(20, 20), (-20, 20), (-20, -20), (20, -20)])

    def on_update(self, delta_time: float = 1 / 60):
        pass

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.PINK)
        self.draw_hit_box(color=arcade.color.WHITE)
