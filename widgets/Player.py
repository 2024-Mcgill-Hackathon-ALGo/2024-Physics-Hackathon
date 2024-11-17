import arcade
from arcade import Sprite


class Player(Sprite):
    def __init__(self, x, y, width, height):
        
        # initial position
        super().__init__()
        self.center_x = x
        self.center_y = y
        
        # initial size
        self.width = width
        self.height = height
        self.set_hit_box([(width/2, height/2),
                          (width/2, -height/2),
                          (-width/2, -height/2),
                          (-width/2, height/2)])
        
        # movement states
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        
        self.movement_speed = 5
    
    def isColliding(self, x, y, width, height):
        # check if object is colliding with the player
        return self.center_x < x + width and self.center_x + self.width > x and self.center_y < y + height and self.center_y + self.height > y
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, arcade.color.RED)
        self.draw_hit_box(color=arcade.color.WHITE)


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
    