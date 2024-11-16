import arcade
from Player import Player
from DebuggingSquare import TestSquare

MOVEMENT_SPEED = 5

class DebuggingView(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player = Player(100, 100, 50, 50)
        self.square = TestSquare(200, 200, 50, 50)
        
    def on_draw(self):
        arcade.start_render()
        
        self.player.draw()
        self.square.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player.stop_moving()
            self.player.moving_up = True
        elif key == arcade.key.DOWN:
            self.player.stop_moving()
            self.player.moving_down = True
        elif key == arcade.key.LEFT:
            self.player.stop_moving()
            self.player.moving_left = True
        elif key == arcade.key.RIGHT:
            self.player.stop_moving()
            self.player.moving_right = True
            
    def update(self, delta_time):
        self.player.update(delta_time)
        
        #test collision
        if self.player.isColliding(self.square.x, self.square.y, self.square.width, self.square.height):
            print("Colliding")
            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass
            
if __name__ == "__main__":
    window = DebuggingView(800, 600, "Debugging View")
    arcade.run()