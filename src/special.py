'''This Special Simulton is called Catcher. It is derived from the Prey class, thus it can be eaten by instances of
the Black Hole class. The Catcher moves just like a Ball simulton. The Catcher is purple, has a radius of 8 pixels 
(width = 16 pixels and height = 16 pixels), and has a set speed of 2 pixels/update. 

The Catcher's unique ability is to "catch" Balls and Floater simultons if they are within 30 pixels from the Catcher. 
If "caught", they are unable to leave the 30 pixel radius (from Catcher).
Any attempts to leave this "gravity field" are drawn back into the Catcher: the simulton's angle changes to a direction that keeps 
simulton within the Catcher's "gravity field." When a Ball or Floater is "caught," it is bound to that specific Catcher
and hence is unable to enter other gravity fields, preventing field overlap and buggy behavior. This allows Catcher
simultons to move through each other on the canvas, along with their "caught" balls and floaters.
'''

import model
from prey import Prey
from math import atan2, pi
from floater import Floater
from ball import Ball
from random import random


class Special(Prey):
    # repel_field = 100
    gravity_field = 30
    radius = 8
    total_caught = set()
    list_of_caught_sets = []
    
    def __init__(self, x, y):
        Prey.__init__(self,x,y,16,16,0,2)
        self.randomize_angle()
        self.caught_set = set()
        self.list_of_caught_sets.append(self.caught_set)

    
    def update(self, model):
        def in_radius(s):
            return (self.distance(s.get_location()) <= Special.gravity_field) and isinstance(s, (Floater, Ball))
        # def is_Special(s):
        #     return isinstance(s, Special)
        x,y = self.get_location()

        #check if any items in the caught set are deleted or eaten from the canvas
        for sim in self.caught_set.copy():
            if sim not in model.sims:
                self.caught_set.remove(sim)
                Special.total_caught.remove(sim)
        #adds all balls and floaters to the caught set that are in the gravity field of the Catcher
        for sim in model.find(in_radius):
            if sim not in self.caught_set and sim not in Special.total_caught: #prevents balls/floaters from being in multiple caught sets
                self.caught_set.add(sim)
                Special.total_caught.add(sim)
        #prevents caught balls and floaters from being freed from the gravity field 
        for sim in self.caught_set:
            if not in_radius(sim):
                sx, sy = sim.get_location()
                nucleic_path = atan2(y-sy, x-sx)
                sim.set_angle(nucleic_path+random()*pi/2)
        #checks all caught balls and floaters if they are in at least one of the caught sets of Catcher simultons
        for sim in Special.total_caught:
            if not any(False if sim not in s else True for s in Special.list_of_caught_sets):
                Special.total_caught.remove(sim)
        self.move() 

        # for spec in model.find(is_Special):
        #     if spec is not self:
        #         spec_x, spec_y = spec.get_location()
        #         self_angle = atan2(x-spec_x, y-spec_y)+random()*pi/2

        #         if self.distance((spec_x, spec_y)) <= Special.repel_field:
        #             self.set_angle(self_angle)
            

    def display(self, canvas):
        x,y = self.get_location()
        canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius, fill = 'purple') 

    def contains(self, xy):
        return self.distance(xy) < self.radius
    
