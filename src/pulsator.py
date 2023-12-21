# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    
    eat_counter = 30

    def __init__(self,x,y):
        super(Pulsator, self).__init__(x,y)
        self.counter = 0

    def update(self, model):
        self.counter += 1
        remove_set = Black_Hole.update(self,model)
        for _ in remove_set:
            self.counter = 0
            self.change_dimension(1,1)
            self.radius = self.get_dimension()[1]/2
        if self.counter == Pulsator.eat_counter:
            self.counter = 0
            self.change_dimension(-1,-1)
            self.radius = self.get_dimension()[1]/2
        if self.get_dimension() == (0,0):
            model.remove(self)
        




    
