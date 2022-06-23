# Simulton
ICS 33 project where different "simultons" with unique properties are put onto a GUI canvas to move around. Canvas is continuously updated, adjusting simultons accordingly, to simulate animation. 

Run script.py and click the control panel to play!



Simulton Types (types are differentiated using inheritance):

ball (blue) - set speed and angle

floater (red) - set speed and randomized angle every few canvas updates

black hole (black) - can't move but eats ball, floater, and special

hunter (black) - chases nearest ball, floater, or special in a certain range

special (purple) - captures ball and floaters that enter in its radius (like an atom electron cloud)
