# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from mobilesimulton import Mobile_Simulton
from prey import Prey


class Ball(Prey): 

    radius = 5
    

    def __init__(self,x,y):
        super(Prey, self).__init__(x,y,10,10,0,5)
        self.randomize_angle()
    
    def update(self, model):
        self.move()

    def display(self, canvas):
        x,y = self.get_location()
        canvas.create_oval(x-Ball.radius, y-Ball.radius, x+Ball.radius, y+Ball.radius, fill = 'blue')
        

