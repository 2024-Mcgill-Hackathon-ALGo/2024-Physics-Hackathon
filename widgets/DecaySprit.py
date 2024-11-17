import random

import arcade
from arcade import Sprite
from pyglet.math import Vec2


class DecaySprint(Sprite):
    def __init__(self):
        super().__init__(hit_box_algorithm="None")
        self.radius = 20
        self.max_speed = 10
        self.set_hit_box([(20, 20), (-20, 20), (-20, -20), (20, -20)])

    def on_update(self, delta_time: float = 1 / 60):
        vector = Vec2(random.uniform(-1, 1),
                      random.uniform(-1, 1))
        vector.normalize()
        self.change_x += vector.x
        self.change_y += vector.y
        vector = Vec2(self.change_x,
                      self.change_y)
        if vector.mag > 20:
            vector = vector.clamp(-10, 10)
            self.change_x = vector.x
            self.change_y = vector.y

        self.center_x += self.change_x * delta_time * self.max_speed
        self.center_y += self.change_y * delta_time * self.max_speed

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.PINK)
        self.draw_hit_box(color=arcade.color.WHITE)
