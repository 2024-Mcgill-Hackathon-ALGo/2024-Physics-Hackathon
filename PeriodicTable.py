import arcade
from ElementBox import ElementBox
from Element import Element 

class PeriodicTableWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.elements = []
        
        # var that will hold our selected element we can eventually pass this to the main game loop
        self.selected_element = None
        self.create_elements()

    def create_elements(self):
        self.elements = [
            # hand made elements for now (also for now im just hard coding in x and y values but eventually we should use the window width and height to calculate these)
            ElementBox(Element('H', 'Hydrogen', 1, 1.008), 20, 550),
            ElementBox(Element('He', 'Helium', 2, 4.0026), 780, 550),
            ElementBox(Element('Li', 'Lithium', 3, 6.94), 20, 513),
            ElementBox(Element('Be', 'Beryllium', 4, 9.0122), 57, 513),
        ]

    def on_draw(self):
        arcade.start_render()
        for element in self.elements:
            element.draw()

        if self.selected_element:
            arcade.draw_text(f"Selected Element: {self.selected_element.element.name} ({self.selected_element.element.symbol})", 10, 20, arcade.color.BLACK, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        for element in self.elements:
            if element.is_clicked(x, y):
                self.selected_element = element
                print(f"Element clicked: {self.selected_element.element.name} ({self.selected_element.element.symbol})") 
                break


# Run the game
window = PeriodicTableWindow(800, 600, "Periodic Table Clicker")
arcade.run()
