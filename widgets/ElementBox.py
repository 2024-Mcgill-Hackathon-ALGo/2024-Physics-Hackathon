import arcade

class ElementBox:
    
    category_colors = {
        "diatomic nonmetal": arcade.color.BRIGHT_GREEN,
        "noble gas": arcade.color.LIGHT_BLUE,
        "alkali metal": arcade.color.DEEP_PINK,
        "alkaline earth metal": arcade.color.LIME_GREEN,
        "metalloid": arcade.color.ORANGE,
        "polyatomic nonmetal": arcade.color.YELLOW,
        "post-transition metal": arcade.color.GRAY,
        "transition metal": arcade.color.SILVER,
        "lanthanide": arcade.color.LIGHT_GOLDENROD_YELLOW,
        "actinide": arcade.color.MEDIUM_PURPLE,
        "unknown": arcade.color.DAFFODIL,
    }
    
    def __init__(self, element, x, y, size):
        self.element = element # element object 
        
        self.x = x  
        self.y = y  
        
        self.width =  size # Width and height of each element box
        self.height = size  
        self.element_category = element.element_category
        
        if self.element_category not in self.category_colors:
            self.element_category = "unknown"
        
    def __repr__(self):
        # java toString equivalent
        return f"Element({self.symbol}, {self.name}, {self.atomic_number}, {self.atomic_weight}, {self.category})"

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.category_colors[self.element_category])
        arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.BLACK, 2)
        arcade.draw_text(self.element.symbol, self.x - 15, self.y - 5, arcade.color.BLACK, 14, bold=True)
        arcade.draw_text(self.element.name, self.x - 15, self.y + 10, arcade.color.BLACK, 9, anchor_x="left")


    def is_clicked(self, x, y):
        # just to check if the place that is clicked is within the box
        return self.x - self.width / 2 < x < self.x + self.width / 2 and self.y - self.height / 2 < y < self.y + self.height / 2


