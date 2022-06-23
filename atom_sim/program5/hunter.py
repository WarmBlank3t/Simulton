# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    
    hunt_dist = 200

    def __init__(self, x, y):
        super(Hunter, self).__init__(x, y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)
        self.randomize_angle()
    
    def update(self, model):
        Pulsator.update(self, model)
        def if_prey(s):
            return isinstance(s, Prey)
        hunt_list = [(self.distance(sim.get_location()),sim) for sim in model.find(if_prey) if self.distance(sim.get_location()) <= 200]

        if hunt_list:
            hunted = min(hunt_list)[1]
            hx, hy = hunted.get_location()
            x,y = self.get_location()
            self.set_angle(atan2(hy-y, hx-x))
        self.move()
        




    

