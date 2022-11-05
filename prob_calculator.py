import copy
import random

class Hat:
    
    #with each object created(hat), create a dictionary that has the ball color as key, and the number of balls with that particular color as value
    def __init__(self,**kwargs):
        #contents is list of items represent each ball in the hat
        self.contents = []
        #dictionary will represent the hats content in key, value pairs
        self.dictionary = dict()
        #for each color and its amount of balls
        for k,v in kwargs.items():
            #adds items to the dictionary (to be used later in the repr function)
            self.dictionary[k] = v
            for i in range(v):
                #adds each ball indiviually to the content list (by appending the key(color) for value(amount))
                self.contents.append(k)
                
    def draw(self,balls=int):
        self.balls = balls
        #return false if the required numberof balls to draw is greater than the number of the contents inthe hat
        if self.balls > len(self.contents):
            return False
        else:
            #shuffle the hat's contents
            random.shuffle(self.contents)
            #remove random element from the contents list for the amouts of balls to draw.
            for item in range(balls):
                self.contents.pop(random.randint(0,len(self.contents)-1))
            
    #represent the object's dictionary when printing the object         
    def __repr__(self):
        output= ""
        for color,amount in self.dictionary.items():
            output = output + f"{color} : {amount}\n"
        return output
        
    
    

    def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        pass
    
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.contents)
hat1.draw(5)
print(hat1.contents)

