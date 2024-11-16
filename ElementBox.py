import arcade

class ElementBox:
    def __init__(self, element, x, y):
        self.element = element # element object 
        
        self.x = x  
        self.y = y  
        
        self.width = 35  # Width and height of each element box
        self.height = 35  
        
    def __repr__(self):
        # java toString equivalent
        return f"Element({self.symbol}, {self.name}, {self.atomic_number}, {self.atomic_weight}, {self.category})"

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.WHITE)
        arcade.draw_text(self.element.symbol, self.x - 15, self.y - 10, arcade.color.BLACK, 14)
        arcade.draw_text(self.element.name, self.x - 15, self.y + 5, arcade.color.BLACK, 10)

    def is_clicked(self, x, y):
        # just to check if the place that is clicked is within the box
        return self.x - self.width / 2 < x < self.x + self.width / 2 and self.y - self.height / 2 < y < self.y + self.height / 2


