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
            #we are gonna use this temporaty content list, to draw the balls from. without touchng the original contents
            self.temp_lst = copy.deepcopy(self.contents)
            #shuffle the hat's contents
            random.shuffle(self.temp_lst)
            #remove random element from the contents list for the amouts of balls to draw.
            #need a way to keep track of the balls drawn (result) for each expirement
            self.result = []
            for item in range(balls):
                self.temp_lst.pop(random.randint(0,len(self.temp_lst)-1))
                
                #print(self.result)
                #print(self.contents)
                
                
            
    #represent the object's dictionary when printing the object         
    def __repr__(self):
        output= ""
        for color,amount in self.dictionary.items():
            output = output + f"{color} : {amount}\n"
        return output
        
    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
    for experiment in range(num_experiments):
        #probability = (hat.dictionary["red"]+hat.dictionary["green"]) / len(hat.contents)
        hat.draw(num_balls_drawn)
        if len(hat.contents) < 1: break
        print(probability)
    
    
hat1 = Hat(black=6, red=4, green=3)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

#probability = experiment(hat=hat1,
                  #expected_balls={"red":2,"green":1},
                  #num_balls_drawn=5,
                  #num_experiments=10)
hat1.draw(0)
print(hat1.contents)
print(hat1.temp_lst)


