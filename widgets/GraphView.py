from enum import Enum
from arcade import Window
import arcade
import arcade.color

class Element:
    # region constructeurs
    def __init__(self, symbol, name, atomic_number, atomic_weight):
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.atomic_weight = atomic_weight
    # endregion constructeurs 
             
    # region méthodes
    
    def equals(self, other):
        return self.symbol == other.symbol and self.name == other.name and self.atomic_number == other.atomic_number and self.atomic_weight == other.atomic_weight
    
    # endregion méthodes
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class DecayType(Enum):
    BETA_MINUS = 1
    BETA_PLUS = 2
    ALPHA = 3

class DecayingElement(Element):
    def __init__(self, symbol, atomic_number, atomic_weight, possible_decays):
        self.name = "Decaying Element"
        super().__init__(symbol, self.name, atomic_number, atomic_weight)
        
        # possible decays should be a dictionnary with this structure:
        # {decay_type: child isotope}
        # example: {"alpha": "He"}
        # example: {"beta-": "B"}
        # example: {"beta+": "C"}
        self.possible_decays = possible_decays
        
    def decay(self, decay_type):
        if decay_type in self.possible_decays:
            self.fetchDecayingElementData(self.possible_decays[decay_type])
        else:
            print(f"Decay type {decay_type} not possible for {self.symbol}")
            
    def fetchDecayingElementData(self, symbol):
        # fetch data from json
        pass
    # for debugging purposes
    def helloWorld(self):
        print("Hello World! I am " + self.symbol + " and I am a Decaying Element!" + " I can decay into " + str(self.possible_decays))
        
    def printDecayers(self):
        for value in self.possible_decays.values():
            value.helloWorld()
            value.printDecayers()


def view_graph():
    arcade.draw_lrtb_rectangle_filled((SCREEN_WIDTH / 8) * 5, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                       arcade.color.GRAY)
    arcade.draw_lrtb_rectangle_outline((SCREEN_WIDTH / 8) * 5, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                       arcade.color.GREEN)
    arcade.draw_line((SCREEN_WIDTH / 8) * 5, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT / 2, arcade.color.GREEN)

def view_circle():
    element = DecayingElement("He",2,4,{DecayType.ALPHA:DecayingElement("e",-1,0,{DecayingElement("e",1,0, None)})})
    arcade.draw_circle_filled((SCREEN_WIDTH/10)*7 , (SCREEN_HEIGHT/100)*89, 35,
                              arcade.color.YELLOW)
    arcade.draw_line((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/100)*86 , (SCREEN_WIDTH/10)*7 , (SCREEN_HEIGHT/100)*77, arcade.color.ORANGE_RED,2)
    arcade.draw_circle_outline((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/100)*89, 35,
                              arcade.color.ORANGE_RED)
    arcade.draw_circle_filled((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/4)*3, 35,
                              arcade.color.YELLOW)
    arcade.draw_circle_outline((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/4)*3, 35,
                              arcade.color.ORANGE_RED)
    arcade.draw_circle_filled((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/8)*3, 35,
                              arcade.color.YELLOW)
    arcade.draw_circle_outline((SCREEN_WIDTH/10)*7, (SCREEN_HEIGHT/8)*3, 35,
                              arcade.color.ORANGE_RED)
def view_player():
    arcade.draw_circle_outline((SCREEN_WIDTH/2), (SCREEN_HEIGHT/20)*13, 15,
                              arcade.color.GREEN)
    arcade.draw_circle_outline((SCREEN_WIDTH/4), (SCREEN_HEIGHT/20)*13, 45,
                              arcade.color.GREEN)

def text():
    arcade.draw_text("4He2",(SCREEN_WIDTH/5),((SCREEN_HEIGHT/100)*88),arcade.color.BLACK,20,width=SCREEN_WIDTH,align="center")
    arcade.draw_text("0e1",(SCREEN_WIDTH/5),((SCREEN_HEIGHT/100)*73),arcade.color.BLACK,20,width=SCREEN_WIDTH,align="center")

if __name__ == '__main__':
    class Win(Window):
        def __init__(self):
            super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        def setup(self):
            self.background_color = (0, 0, 0)

        def on_draw(self):
            self.clear()
            # arcade.start_render()
            view_graph()
            view_circle()
            view_player()
            text()
            # arcade.finish_render()
            


    def main():
        window = Win()
        window.setup()
        
        arcade.run()


    main()
