import view_v3
import numpy as np

gui = view_v3.GraphAnimation()

while True:
	gui.drawG1(np.random.random_integers(0, 100))
	gui.drawG2(np.random.random_integers(0, 100))
	gui.drawG3(np.random.random_integers(0, 100))
	gui.drawG4(np.random.random_integers(0, 100))
