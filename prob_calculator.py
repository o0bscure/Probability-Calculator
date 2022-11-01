import copy
import random

class Hat:
    
    #with each object created(hat), create a dictionary that has the ball color as key, and the number of balls with that particular color as value
    def __init__(self,**kwargs):
        self.contents = dict()
        for k,v in kwargs.items():
            self.contents[k] = v
            
    #represent the object's dictionary when printing the object         
    def __repr__(self):
        return f"{self.contents}"
        
    
    

    def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        pass
    
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1)
print(hat2)
print(hat3)
