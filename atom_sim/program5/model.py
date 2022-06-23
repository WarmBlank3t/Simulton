import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from special    import  Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running = False
cycle_count = 0
sims = set()
button_name = ''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, sims
    running = False
    cycle_count = 0
    sims.clear()

#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, running
    if running:
        update_all()
        display_all()
        running = False
    else:
        running = True
        update_all()
        display_all()
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global button_name
    button_name = kind



#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if button_name == 'Remove':
        for s in sims.copy():
            if s.contains((x,y)):
                remove(s)
    elif button_name in {'Ball','Floater','Black_Hole','Pulsator','Hunter', 'Special'}:
        eval(f'add({button_name}({x},{y}))')
    

#add simulton s to the simulation
def add(s):
    sims.add(s)
    
    
    

# remove simulton s from the simulation    
def remove(s):
    sims.remove(s)

    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return {s for s in sims if p(s)}


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for s in sims.copy():
            s.update(model)

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for sim in controller.the_canvas.find_all():
        controller.the_canvas.delete(sim)
    for s in sims:
        s.display(controller.the_canvas)

    #might switch order of simultons and cycles
    controller.the_progress.config(text = f'{cycle_count} updates/{len(sims)} simultons')
