import view_v3
import numpy as np

gui = view_v3.GraphAnimation()

new_y = 0
while True:
	new_y = np.random.random_integers(0, 100)
	gui.updateGraphs(new_y)
	
	
#gui.draw()


