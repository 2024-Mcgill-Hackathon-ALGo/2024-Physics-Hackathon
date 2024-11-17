import arcade
from arcade import SpriteList

from model.DecayType import DecayType
from model.DecayingElement import DecayingElement
from widgets.DecaySprite import DecaySprite
from widgets.Player import Player
from widgets.DebuggingSquare import TestSquare

MOVEMENT_SPEED = 5

class GameView(arcade.View):
    def __init__(self, element: DecayingElement | None):
        super().__init__()
        self.player = Player(100, 100, 50, 50)

        self.background = None
        self.camera = None
        self.element = element
        self.decay_opportunities = SpriteList()
        for decay_type in DecayType:
            self.decay_opportunities.append(DecaySprite(decay_type))
        
    def setup(self):
        width, height = self.window.get_size()
        self.camera = arcade.Camera(width, height)
        try:    
            self.background = arcade.load_texture(r"./ressources/CharacterBranch/34713.jpg")
        except:
            print("Error loading background image")
            self.background = None
    
    def on_draw(self):
        self.clear()
        
        self.camera.use()
        arcade.start_render()
        
        #region drawing background
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            480, 270,
                                            self.background)

        arcade.draw_lrwh_rectangle_textured(480, 270,
                                            480, 270,
                                            self.background)

        arcade.draw_lrwh_rectangle_textured(0, 270,
                                            480, 270,
                                            self.background)
        arcade.draw_lrwh_rectangle_textured(480, 0,
                                            480, 270,
                                            self.background)
        arcade.draw_lrwh_rectangle_textured(480, 270*2,
                                            480, 270,
                                            self.background)

        arcade.draw_lrwh_rectangle_textured(0, 270*2,
                                            480, 270,
                                            self.background)
        # endregion
        self.player.draw()
        for sprite in self.decay_opportunities.sprite_list:
            sprite.draw()

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
        player_collision_list = arcade.check_for_collision_with_lists(self.player, [self.decay_opportunities])
        for sprit in player_collision_list:
            print(sprit.center_x)
            if isinstance(sprit, DecaySprite):
                pass

        self.decay_opportunities.on_update(delta_time)
            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass
            
if __name__ == "__main__":
    window = arcade.Window(1920, 1080)
    gameview = GameView()
    gameview.setup()
    window.show_view(gameview)
    arcade.run()