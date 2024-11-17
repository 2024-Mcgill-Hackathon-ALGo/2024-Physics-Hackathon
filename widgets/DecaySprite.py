import random
import math
import arcade
from arcade import Sprite
from pyglet.math import Vec2

from model.DecayType import DecayType


class DecaySprite(Sprite):
    def __init__(self, decay_type, center_x, center_y, radius=20):
        super().__init__(hit_box_algorithm="None", center_x=center_x, center_y=center_y)
        self.radius = radius
        self.max_speed = 10
        self.set_hit_box([(radius, radius), (-radius, radius), (-radius, -radius), (radius, -radius)])
        self.decay_type = decay_type

        # Set color based on decay type
        # add labels for decay types
        if decay_type == DecayType.ALPHA:
            self.color = arcade.color.ORANGE
            self.label = "A"
        elif decay_type == DecayType.BETA_MINUS:
            self.color = arcade.color.BLUE
            self.label = "B-"
        elif decay_type == DecayType.BETA_PLUS:
            self.color = arcade.color.BLUE
            self.label = "B+"
        else:
            self.color = arcade.color.LIGHT_BLUE
            self.label = "Unknown"

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

        new_x = self.center_x + self.change_x * delta_time * self.max_speed
        new_y = self.center_y + self.change_y * delta_time * self.max_speed

        # Check for collision with screen borders
        if new_x - self.radius < 0 or new_x + self.radius > arcade.get_window().get_size()[0]:
            self.change_x = 0
        else:
            self.center_x = new_x

        if new_y - self.radius < 0 or new_y + self.radius > arcade.get_window().get_size()[1]:
            self.change_y = 0
        else:
            self.center_y = new_y

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
        
        # put the labels above the decay sprites
        arcade.draw_text(self.label, self.center_x - self.radius / 2, self.center_y + self.radius + 5, arcade.color.WHITE, 12)
        self.draw_hit_box(color=arcade.color.RED_BROWN)


    @staticmethod
    def get_number_of_decay_sprites(half_life):
        if half_life is None:
            return 0  # no decay opportunities : Element is stable
        else:
            
            if half_life <= 0:
                return 10
            log_half_life = math.log10(half_life)
            if log_half_life <= -3:  
                return 10
            elif log_half_life <= 0:  
                return 8
            elif log_half_life <= 3: 
                return 6
            elif log_half_life <= 6:  
                return 4
            else:  
                return 2
