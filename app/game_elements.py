class GameElement(object):
    value = 0

class Food(GameElement):
    def __str__(self):
        return "o"

class Grid(object):
    spaces = None
    
    def __init__(self, height, width):
        self.spaces = [[None for j in range(width)] for row in range (height)]
    
    def add_food(self, food_list):
        for x,y in food_list:
            self.spaces[y][x] = Food()
        
    def __str__(self):
        return "\n".join([",".join([str(element) if element else " " for element in row]) for row in self.spaces])
    