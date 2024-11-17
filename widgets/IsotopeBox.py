import arcade

class IsotopeBox:
    def __init__(self, text, x, y, size):
        self.text = text
        
        self.x = x  
        self.y = y  
        
        self.width =  size * 2 # Width and height of each element box
        self.height = size * 2
       
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.WHITE)
        arcade.draw_text(self.text, self.x - 15, self.y - 10, arcade.color.BLACK, 14)

    def is_clicked(self, x, y):
        # just to check if the place that is clicked is within the box
        return self.x - self.width / 2 < x < self.x + self.width / 2 and self.y - self.height / 2 < y < self.y + self.height / 2


