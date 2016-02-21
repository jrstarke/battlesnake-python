MY_SNAKE_ID = "f0a3b076-268e-44f2-9371-d80185843178"
my_snake_health = 0
my_snake_position = None

INVALID_ELEMENT_VALUE = -100
average_range = 2

class GameElement(object):
    value = 0

    def __str__(self):
        return self.display

class Food(GameElement):
    display = "o"
    
class SnakeElement(GameElement):
    value = -300 
    def __init__(self,snake):
        if snake['id'] == MY_SNAKE_ID:
            self.display = self.display.upper()
    
class SnakeHead(SnakeElement):
    display = "h"
    
    def __init__(self,snake):
        super(SnakeHead,self).__init__(snake)
        if snake['id'] == MY_SNAKE_ID:
            my_snake_health = snake['health']

class SnakeBody(SnakeElement):
    display = "s"
    
class Grid(object):
    spaces = None
    height = 0
    width = 0
    
    def get_move(self,x,y):
        directions = ['north','east','south','west']
        
        direction_values = [(direction, self.get_value_of_direction(x,y,direction)) for direction in directions]
        
        return sorted(direction_values,cmp=lambda direction, value: value, reversed=True)[0][0]
        
        
    
    def get_value_of_direction(self,x,y,direction):
        if direction == "north":
            y = y - 1
        if direction == 'south':
            y = y + 1
        if direction == 'east':
            x = x + 1
        if direction == 'west':
            x = x - 1
        
        return self.get_space_average_value(x, y) + self.get_space_value(x, y)
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
        self.spaces = [[None for j in range(width)] for row in range (height)]
        
    def get_space_value(self,x,y):
        if x < 0 or x > self.width or y < 0 or y > self.height:
            return INVALID_ELEMENT_VALUE
        
        element =  self.spaces[y][x]
        if not element:
            return element.value
        
    def get_space_average_value(self,x,y):
        area = (average_range * 2) + 1
        sum = 0
        
        for x_look in range(x-average_range, x+average_range+1):
            for y_look in range(y-average_range, y+average_range+1):
               sum += self.get_space_value(x_look,y_look)
               
        return sum/area 
    
    def add_food(self, food_list):
        for x,y in food_list:
            self.spaces[y][x] = Food()
            
    def add_snakes(self, snake_list):
        for snake in snake_list:
            self.add_snake(snake)
        
    def add_snake(self,snake):
        print snake['coords']
        for index, coordinate in enumerate(snake['coords']):
            x,y = coordinate
            if index == 0:
                body_element = SnakeHead(snake)
                if snake['id'] == MY_SNAKE_ID:
                    my_snake_position = coordinate
            else:
                body_element = SnakeBody(snake)
            
            self.spaces[y][x] = body_element
        
    def __str__(self):
        return "\n".join([",".join([str(element) if element else " " for element in row]) for row in self.spaces])
    