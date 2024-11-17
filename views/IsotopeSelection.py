import arcade
from services import IsotopeGetter
from views.GameView import GameView
from widgets.IsotopeBox import IsotopeBox
from model.DecayingElement import DecayingElement
from services.ElementMapper import mapper
from views import PeriodicTable
import arcade.gui

class IsotopeSelectionView(arcade.View):
    def __init__(self, selected_element):
        super().__init__()
        
        self.selected_element = selected_element
        try:
            self.isotopes = IsotopeGetter.returnIsotopes(selected_element.element.symbol)
        except:
            self.isotopes = []
        self.isotopeBoxes = []
        self.isotopeChosen = None

        # UI Manager
        self.manager = arcade.gui.UIManager()
        self.v_box = arcade.gui.UIBoxLayout()

        # Back button
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=200)
        self.back_button.on_click = self.on_back_button_click
        self.v_box.add(self.back_button.with_space_around(bottom=10))

    def setup(self):
        self.manager.enable()

        # Add layout to the UI
        self.manager.add(arcade.gui.UIAnchorWidget(child=self.v_box, anchor_x="center", anchor_y="bottom"))

    def on_draw(self):
        self.clear()
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

        if self.selected_element and self.selected_element.element:
            arcade.draw_text(
                f"Selected Element: {self.selected_element.element.name} ({self.selected_element.element.symbol})",
                100, 100, arcade.color.BLACK, 18
            )
        else:
            arcade.draw_text("No element selected", 100, 100, arcade.color.BLACK, 18)

        self.draw_isotopes()
        self.manager.draw()

    def draw_isotopes(self):
        max_isotopes_to_display = 14
        window_width, window_height = self.window.get_size()
        padding = 10  # Space between boxes
        box_width = window_width / 8  
        box_height = 40
        start_y = window_height - 150 

        # Adjust the starting position to ensure boxes don't go out of bounds on the left
        # the logic for how to place the boxes came from chatGPT so, yes, its confusing but it works
        # i commented it as much as possible to make it easier to understand
        x_start_pos = padding + box_width / 2

        # Create a box for each isotope
        for i, isotope in enumerate(self.isotopes[:max_isotopes_to_display]):
            text = str(isotope) if isotope else "Unknown Isotope"

            # Calculate the x position based on the number of boxes per row
            x_pos = (i % 6) * (box_width + padding) + x_start_pos

            # Ensure the last box fits on the screen
            if x_pos + box_width > window_width - padding:
                # If the box exceeds window width, wrap to the next row
                x_pos = x_start_pos

            y_pos = start_y - (i // 6) * (box_height + padding)

            self.isotopeBoxes.append(IsotopeBox(text, x_pos, y_pos, box_width, box_height))

        if not self.isotopes:
            arcade.draw_text("No unstable isotopes found", window_width / 2 , window_height / 2, arcade.color.BLACK, 18, anchor_x="center", bold=True)
        else:
            for isotopeBox in self.isotopeBoxes:
                isotopeBox.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for isotopeBox in self.isotopeBoxes:
            if isotopeBox.is_clicked(x, y):
                print(f"Isotope clicked: {isotopeBox.text}")
                isotope_chosen = mapper.toDecayingElement(isotopeBox.text)
                view = GameView(isotope_chosen)
                view.setup()
                self.window.show_view(view)
                self.manager.disable()
                break

    def on_back_button_click(self, event):
        # print("Back button pressed")
        periodic_table_view = PeriodicTable.PeriodicTableView()
        arcade.get_window().show_view(periodic_table_view)
        self.manager.disable()

