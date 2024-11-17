import random

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
        
        # Feedback variables 
        self.message = ""
        self.message_duration = 2.0 
        self.message_timer = 0.0

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
        self.decay_opportunities.sprite_list = []
        
        # RealTimeFeedBack
        num_sprites = DecaySprite.get_number_of_decay_sprites(self.element.half_life)
        
       

        for _ in range(num_sprites):
            # Decide whether to include valid or invalid decay types
            if random.random() < 0.5 and self.element.possible_decays:
               
                decay_type = random.choice(list(self.element.possible_decays.keys()))
            else:
            
                decay_type = random.choice(list(DecayType))
            self.decay_opportunities.append(DecaySprite(
                decay_type,
                random.uniform(100, self.window.width - 100),
                random.uniform(100, self.window.height - 100)
            ))
        
        
        
        # for decay_type in DecayType:
        #     self.decay_opportunities.append(DecaySprite(decay_type,
        #                                                 random.uniform(100, self.window.width - 100),
        #                                                 random.uniform(100, self.window.height - 100)))
    def on_draw(self):
        self.clear()

        self.camera.use()
        arcade.start_render()

        #region drawing background
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

        self.player.draw()
        for sprite in self.decay_opportunities.sprite_list:
            sprite.draw()
            
        # Feedback 
        arcade.draw_text(
        f"Current Element: {self.element.symbol} (Atomic Number: {self.element.atomic_number})",
        10, self.window.height - 30, arcade.color.WHITE, 14
    )

    # Draw the message if it's active
        if self.message:
            arcade.draw_rectangle_filled(
                self.window.width / 2, self.window.height / 2, 400, 50, arcade.color.BLACK + (200,)
            )
            arcade.draw_text(
                self.message, self.window.width / 2, self.window.height / 2,
                arcade.color.WHITE, 14, anchor_x="center", anchor_y="center", align="center", width=380
            )
                

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
                if self.element.possible_decays.get(sprit.decay_type) is not None:
                    old_element = self.element
                    self.element = self.element.possible_decays.get(sprit.decay_type)
                    self.reset()
    
            # Feeback message 
            # Valid decay mode
                    self.message = f"Successful decay: {old_element.symbol} decayed into {self.element.symbol} via {sprit.decay_type.name} decay."
                    self.message_timer = self.message_duration
                else:
                
                    self.message = f"{sprit.decay_type.name} decay not possible for {self.element.symbol}."
                    self.message_timer = self.message_duration

        self.decay_opportunities.on_update(delta_time)

        # if player is colliding with screen border stop moving
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
        self.window.show_view(GameOverView())


if __name__ == "__main__":
    window = arcade.Window(1920, 1080)
    gameview = GameView()
    gameview.setup()
    window.show_view(gameview)
    arcade.run()
    