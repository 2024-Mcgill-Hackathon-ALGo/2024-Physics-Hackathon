import arcade

class Player:
    def __init__(self, x, y, width, height):
        
        # initial position
        self.x = x
        self.y = y
        
        # initial size
        self.width = width
        self.height = height
        
        # movement states
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        
        self.movement_speed = 5
    
    def isColliding(self, x, y, width, height):
        # check if object is colliding with the player
        return self.x < x + width and self.x + self.width > x and self.y < y + height and self.y + self.height > y
    
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.RED)
        
    
    def update(self, delta_time):
        if self.moving_up:
            self.y += self.movement_speed
        elif self.moving_down:
            self.y -= self.movement_speed
        elif self.moving_left:
            self.x -= self.movement_speed
        elif self.moving_right:
            self.x += self.movement_speed    
    
    def stop_moving(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
    