import arcade
import arcade.gui

from views import MainMenu

class SettingsMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.background = None
        self.v_box = arcade.gui.UIBoxLayout()

        # Available resolutions
        self.resolutions = [
            (800, 600),
            (1024, 768),
            (1280, 720),
            (1920, 1080),
        ]
        self.selected_resolution = (800, 600)  # Default resolution

        # Creating resolution buttons
        self.resolution_button_800x600 = arcade.gui.UIFlatButton(text="800 x 600", width=200)
        self.resolution_button_800x600.on_click = self.change_resolution(self.resolutions[0])
        self.v_box.add(self.resolution_button_800x600.with_space_around(bottom=10))

        self.resolution_button_1024x768 = arcade.gui.UIFlatButton(text="1024 x 768", width=200)
        self.resolution_button_1024x768.on_click = self.change_resolution(self.resolutions[1])
        self.v_box.add(self.resolution_button_1024x768.with_space_around(bottom=10))

        self.resolution_button_1280x720 = arcade.gui.UIFlatButton(text="1280 x 720", width=200)
        self.resolution_button_1280x720.on_click = self.change_resolution(self.resolutions[2])
        self.v_box.add(self.resolution_button_1280x720.with_space_around(bottom=10))

        self.resolution_button_1920x1080 = arcade.gui.UIFlatButton(text="1920 x 1080", width=200)
        self.resolution_button_1920x1080.on_click = self.change_resolution(self.resolutions[3])
        self.v_box.add(self.resolution_button_1920x1080.with_space_around(bottom=10))

        # Apply and Cancel buttons
        apply_button = arcade.gui.UIFlatButton(text="Apply", width=200)
        cancel_button = arcade.gui.UIFlatButton(text="Done", width=200)
        self.v_box.add(apply_button.with_space_around(bottom=20))
        self.v_box.add(cancel_button)

        # Button events
        apply_button.on_click = self.apply_changes
        cancel_button.on_click = self.done_modifying

    def setup(self):
        self.manager.enable()

        # Add layout to the UI
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.v_box,
            )
        )

        # Try loading background image
        try:
            self.background = arcade.load_texture(
                r"./ressources/MainMenu/images/Atom-Desktop-Wallpaper-1183943868.jpeg")
        except FileNotFoundError:
            print("Background image not found. Ensure the path is correct.")
            self.background = None

    def on_draw(self):
        self.clear()
        arcade.start_render()

        # Get the current window size
        width, height = self.window.get_size()

        # Draw background image, scaled to fit the window size
        if self.background:
            arcade.draw_lrwh_rectangle_textured(
                0, 0, width, height, self.background
            )

        # Draw UI elements
        self.manager.draw()

        # Title text centered at the top of the window
        arcade.draw_text(
            "Settings Menu",
            width / 2,
            height - 50,
            arcade.color.BLACK,
            font_size=30,
            font_name="Kenney High Square",
            anchor_x="center",
            anchor_y="center"
        )

    def change_resolution(self, resolution):
        def _change(event):
            self.selected_resolution = resolution
            print(f"Selected resolution: {self.selected_resolution[0]} x {self.selected_resolution[1]}")
        return _change

    def apply_changes(self, event):
        width, height = self.selected_resolution
        arcade.get_window().set_viewport(0, width, 0, height)
        arcade.get_window().set_size(width, height)
        arcade.get_window().set_viewport(0, width, 0, height)
        print(f"Resolution changed to: {width} x {height}")
        
        # Ensure that the layout is adjusted after the resolution change
        self.setup()

    def done_modifying(self, event):
        print("end of settings view.")
        self.manager.disable()
        main_menu = MainMenu.MainMenuView()
        main_menu.setup()
        self.window.show_view(main_menu)

    def on_resize(self, width, height):
        print(f"Window resized to: {width} x {height}")

        # Recalculate the layout after resize and draw the UI
        self.manager.on_resize(width, height)

        self.clear()
        self.on_draw()
