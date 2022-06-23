# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    def __init__(self, x,y):
        super(Prey, self).__init__(x,y,10,10, 0, 5)
        self.randomize_angle()

    def update(self, model):
        rand = int(random()*10)+1
        if rand <= 3:
            self.set_angle(self.get_angle() + random()-.5)
            self.set_speed(self.get_speed() + random()-.5)
            if self.get_speed() < 3: self.set_speed(3)
            if self.get_speed() > 7: self.set_speed(7)
        self.move()

    def display(self, canvas):
        x,y = self.get_location()
        canvas.create_oval(x-Floater.radius, y-Floater.radius, x+Floater.radius, y+Floater.radius, fill = 'red')
