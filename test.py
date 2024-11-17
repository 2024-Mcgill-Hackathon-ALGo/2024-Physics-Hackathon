from transformers import pipeline
import arcade

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHAT_WIDTH = 800
SCREEN_TITLE = "Chatbot with Game Window"

class ChatbotWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)

        # Initialize Hugging Face pipeline
        self.chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
        
        # Chatbot attributes
        self.chat_history = []
        self.current_input = ""

        # Input box properties
        self.input_active = False
        self.input_box_x = SCREEN_WIDTH - CHAT_WIDTH + 10
        self.input_box_y = 10
        self.input_box_width = CHAT_WIDTH - 20
        self.input_box_height = 30

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()

        arcade.draw_text("Game Area", SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2,
                         arcade.color.BLACK, 24)

        # Draw chatbot sidebar
        arcade.draw_rectangle_filled(
            SCREEN_WIDTH - CHAT_WIDTH // 2, SCREEN_HEIGHT // 2,
            CHAT_WIDTH, SCREEN_HEIGHT, arcade.color.DARK_BLUE
        )
        arcade.draw_text("Chatbot", SCREEN_WIDTH - CHAT_WIDTH // 2, SCREEN_HEIGHT - 40,
                         arcade.color.WHITE, 18)

        # Draw chat history
        y_offset = SCREEN_HEIGHT - 80
        for message in self.chat_history[-10:]:
            arcade.draw_text(message, SCREEN_WIDTH - CHAT_WIDTH + 10, y_offset,
                             arcade.color.WHITE, 12, width=CHAT_WIDTH - 20)
            y_offset -= 40

        # Draw input box
        arcade.draw_rectangle_outline(
            self.input_box_x + self.input_box_width // 2,
            self.input_box_y + self.input_box_height // 2,
            self.input_box_width, self.input_box_height,
            arcade.color.WHITE, 2
        )
        arcade.draw_text(
            self.current_input, self.input_box_x + 5,
            self.input_box_y + 5, arcade.color.WHITE, 12, width=self.input_box_width - 10
        )

    def on_key_press(self, key, modifiers):
        """Handle key presses."""
        if key == arcade.key.ENTER:
            self.process_input()
        elif key == arcade.key.BACKSPACE:
            self.current_input = self.current_input[:-1]

    def process_input(self):
        """Process the input text."""
        user_message = self.current_input.strip()
        self.chat_history.append(f"You: {self.current_input}")
        self.current_input = ""

        # Get response from the ML model
        response = self.get_ml_response(user_message)
        self.chat_history.append(f"Bot: {response}")

        # Quit application if input is 'quit'
        if user_message.lower() == "quit":
            arcade.close_window()

    def get_ml_response(self, user_message):
        """Use a machine learning model to generate a response."""
        response = self.chatbot(user_message, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse clicks."""
        if (self.input_box_x <= x <= self.input_box_x + self.input_box_width and
                self.input_box_y <= y <= self.input_box_y + self.input_box_height):
            self.input_active = True
        else:
            self.input_active = False

    def on_text(self, text):
        """Handle text input."""
        if self.input_active and len(self.current_input) < 50:
            self.current_input += text


def main():
    """Main function."""
    window = ChatbotWindow()
    arcade.run()


if __name__ == "__main__":
    main()
