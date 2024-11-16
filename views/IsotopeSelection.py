import arcade
from services import IsotopeGetter

class IsotopeSelectionView(arcade.View):
    def __init__(self, selected_element):
        super().__init__()
        
        self.selected_element = selected_element
        self.isotopes = IsotopeGetter.returnIsotopes(selected_element.element.symbol)

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
        
        max_isotopes_to_display = 15
        window_width, window_height = self.window.get_size()
        start_y = window_height - 150 
        
        for i, isotope in enumerate(self.isotopes[:max_isotopes_to_display]):
            text = str(isotope) if isotope else "Unknown Isotope"
            arcade.draw_text(text, 100, start_y - 20 * i, arcade.color.WHITE, 14)

