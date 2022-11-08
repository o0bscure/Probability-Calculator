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
            #create a copy of the original hat's content
            self.original=copy.deepcopy(self.contents)
            #shuffle the hat's contents
            random.shuffle(self.contents)
            #remove random element from the contents list for the amouts of balls to draw.
            #need a way to keep track of the balls drawn (result) for each expirement
            self.result = []
            for i in range(balls):
                #pick a randome index to remove an item from the hat
                random_index = random.randint(0,len(self.contents)-1)
                #add that item to the results list
                self.result.append(self.contents[random_index])
                #remove that item from the hat
                self.contents.pop(random_index)
            if self.balls > len(self.contents):
                self.contents = self.original
            return self.result
                
    #represent the object's dictionary when printing the object         
    def __repr__(self):
        output= ""
        for color,amount in self.dictionary.items():
            output = output + f"{color} : {amount}\n"
        return output
        
    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #need to check if the desired balls exist in the results after each draw(), keep track of how many times you got the desired result(M?) 
    m = 0
    probability = 0
    #run expirements
    for experiment in range(num_experiments):
        #place holder list to store succesful experiment
        place_holder = []
        #draw balls
        hat.draw(num_balls_drawn)
        #check if the result of the draw has the required outcome (the keys with its correspondent values)
        for key,value in expected_balls.items():
            if hat.result.count(key) >= value:
                place_holder.append((key,value))
        if len(place_holder) == len(expected_balls):
            print(place_holder)
            m = m + 1
    #expermintal probability equation
    probability = m/num_experiments
    return probability
    
hat1 = Hat(black=6, red=4, green=3)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

probability = experiment(hat=hat1,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)


