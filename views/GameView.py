import random
import time

import arcade
from arcade import SpriteList

from model.DecayType import DecayType
from model.DecayingElement import DecayingElement
from widgets.DecaySprite import DecaySprite
from widgets.Player import Player

MOVEMENT_SPEED = 5
PLAYER_SIZE = 30


class GameView(arcade.View):
    def __init__(self, element: DecayingElement | None):
        super().__init__()
        self.player = Player(100, 100, PLAYER_SIZE, PLAYER_SIZE)

        self.background = None
        self.camera = None
        self.element = element
        self.decay_opportunities = SpriteList()

        self.start_time = time.time()  # Record the starting time
        self.elapsed_time = 0  # var that we will eventually pass to game over view to display the time

    def setup(self):
        self.reset()
        width, height = self.window.get_size()
        self.camera = arcade.Camera(width, height)
        try:
            self.background = arcade.load_texture(r"./ressources/CharacterBranch/34713.jpg")
        except:
            print("Error loading background image")
            self.background = None

    def reset(self):
        # self.decay_opportunities.sprite_list = []
        
        # for sprite in self.decay_opportunities.sprite_list:
        self.decay_opportunities.clear()
        
        for decay_type in DecayType:
            self.decay_opportunities.append(DecaySprite(decay_type,
                                                        random.uniform(100, self.window.width - 100),
                                                        random.uniform(100, self.window.height - 100)))

    def on_draw(self):
        self.clear()

        self.camera.use()
        arcade.start_render()

        #region Draw the background
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            480, 270,
                                            self.background, alpha=125)

        arcade.draw_lrwh_rectangle_textured(480, 270,
                                            480, 270,
                                            self.background, alpha=125)

        arcade.draw_lrwh_rectangle_textured(0, 270,
                                            480, 270,
                                            self.background, alpha=125)
        arcade.draw_lrwh_rectangle_textured(480, 0,
                                            480, 270,
                                            self.background, alpha=125)
        arcade.draw_lrwh_rectangle_textured(480, 270 * 2,
                                            480, 270,
                                            self.background, alpha=125)

        arcade.draw_lrwh_rectangle_textured(0, 270 * 2,
                                            480, 270,
                                            self.background, alpha=125)
        # endregion

        # Draw the player and decay opportunities
        self.player.draw()
        for sprite in self.decay_opportunities.sprite_list:
            sprite.draw()

        # timer :D
        arcade.draw_text(f"Time: {self.elapsed_time:.2f} seconds",
                         10, self.window.height - 30,
                         arcade.color.WHITE, 18)

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
        # Update elapsed time
        self.elapsed_time = time.time() - self.start_time

        self.player.update(delta_time)

        # Check for collisions
        player_collision_list = arcade.check_for_collision_with_lists(self.player, [self.decay_opportunities])
        for sprite in player_collision_list:
            print(sprite.center_x)
            if isinstance(sprite, DecaySprite) and self.element.possible_decays.get(sprite.decay_type) is not None:
                # print("Decay type: ", sprite.decay_type)
                # print("Element: ", self.element.possible_decays.get(sprite.decay_type).possible_decays)
                
                if self.element.possible_decays.get(sprite.decay_type).possible_decays == {}:
                    self.win()
                    return
                
                self.element = self.element.possible_decays.get(sprite.decay_type)
                self.reset()

        self.decay_opportunities.on_update(delta_time)

        # Stop player if colliding with screen borders
        if self.player.left < 0 or self.player.right > self.window.get_size()[0]:
            self.player.stop_moving()
            self.die()
        if self.player.bottom < 0 or self.player.top > self.window.get_size()[1]:
            self.player.stop_moving()
            self.die()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def die(self):
        from views.GameOverView import GameOverView
        self.window.show_view(GameOverView(self.elapsed_time))
        
    def win(self):
        from views.WinView import WinView
        self.window.show_view(WinView(self.elapsed_time))


