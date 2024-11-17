import arcade

class IsotopeBox:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x  
        self.y = y  
        self.width = width
        self.height = height
       
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.ASH_GREY)
        arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.BLACK, 2)
        arcade.draw_text(self.text, self.x, self.y, arcade.color.BLACK, 14, width=self.width, align="center", anchor_x="center", anchor_y="center")

    def is_clicked(self, x, y):
        return self.x - self.width / 2 < x < self.x + self.width / 2 and self.y - self.height / 2 < y < self.y + self.height / 2