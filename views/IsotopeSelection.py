import arcade
from services import IsotopeGetter
from widgets.IsotopeBox import IsotopeBox
from model.DecayingElement import DecayingElement
from services.ElementMapper import mapper

class IsotopeSelectionView(arcade.View):
    def __init__(self, selected_element):
        super().__init__()
        
        self.selected_element = selected_element
        self.isotopes = IsotopeGetter.returnIsotopes(selected_element.element.symbol)
        self.isotopeBoxes = []
        
        self.isotopeChosen = None
        
       

    def on_draw(self):
        self.clear()
        arcade.start_render()

        if self.selected_element and self.selected_element.element:
            arcade.draw_text(
                f"Selected Element: {self.selected_element.element.name} ({self.selected_element.element.symbol})",
                100, 100, arcade.color.WHITE, 14
            )
        else:
            arcade.draw_text("No element selected", 100, 100, arcade.color.WHITE, 14)

        
        self.draw_isotopes()
        #show 15 first isotopes
        
    def draw_isotopes(self):
        
        max_isotopes_to_display = 7
        window_width, window_height = self.window.get_size()
        start_y = window_height - 150 

        
        for i, isotope in enumerate(self.isotopes[:max_isotopes_to_display]):
            text = str(isotope) if isotope else "Unknown Isotope"
            self.isotopeBoxes.append(IsotopeBox(text, 100*i + 100, 500, window_height / 15))

            
        for isotopeBox in self.isotopeBoxes:
            isotopeBox.draw()


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # check if is in isotope isotopebox has isotope.is_clicked(x,y)
        for isotopeBox in self.isotopeBoxes:
            if isotopeBox.is_clicked(x, y):
                print(f"Isotope clicked: {isotopeBox.text}")
                self.isotopeChosen = mapper.toDecayingElement(isotopeBox.text)
                print(self.isotopeChosen.possible_decays)
                break
            