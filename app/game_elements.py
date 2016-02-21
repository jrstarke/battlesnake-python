MY_SNAKE_ID = "f0a3b076-268e-44f2-9371-d80185843178"
my_snake_health = 0

class GameElement(object):
    value = 0

class Food(GameElement):
    display = "o"
    
    def __str__(self):
        return self.display
    
class SnakeElement(GameElement):
    def __init__(self,snake):
        if snake.id == MY_SNAKE_ID:
            self.display = self.display.upper()
    
class SnakeHead(SnakeElement):
    display = "h"
    
    def __init__(self,snake):
        super(SnakeHead,self).__init__(snake)
        if snake.id == MY_SNAKE_ID:
            my_snake_health = snake['health']

class SnakeBody(GameElement):
    display = "s"
    
class Grid(object):
    spaces = None
    
    def __init__(self, height, width):
        self.spaces = [[None for j in range(width)] for row in range (height)]
    
    def add_food(self, food_list):
        for x,y in food_list:
            self.spaces[y][x] = Food()
            
    def add_snakes(self, snake_list):
        for snake in snake_list:
            self.add_snake(snake)
        
    def add_snake(self,snake):
        for index, (x,y) in enumerate(snake['coords']):
            
            body_type = SnakeBody
            if index == 0:
                body_type = SnakeHead
            
            self.spaces[y][x] = body_type(snake)
        
    def __str__(self):
        return "\n".join([",".join([str(element) if element else " " for element in row]) for row in self.spaces])
    