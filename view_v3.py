import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
plt.ion()

class GraphAnimation(animation.FuncAnimation):
	
	def set_x(xn):
		self.x = xn
		print("set")
	
	def get_x(self):
		print("get")
		return self.x
		
	def updateGraphs(self, new_y):

		#self.x = self.get_x()
		self.x += 5
		#y = np.random.random_integers(0, 100)
		y = new_y
		
		print(self.x, y)
		
		self.xdata_g1.append(self.x)
		self.ydata_g1.append(y)
		self.xdata_g2.append(self.x)
		self.ydata_g2.append(y)
		self.xdata_g3.append(self.x)
		self.ydata_g3.append(y)
		self.xdata_g4.append(self.x)
		self.ydata_g4.append(y)
		
		xmin_g1, xmax_g1 = self.g1.get_xlim()
		xmin_g2, xmax_g2 = self.g2.get_xlim()
		xmin_g3, xmax_g3 = self.g3.get_xlim()
		xmin_g4, xmax_g4 = self.g4.get_xlim()
		
		if self.x >= xmax_g1:
			self.g1.set_xlim(xmax_g1, 2*xmax_g1)
			self.g1.figure.canvas.draw()
			self.line_g1.set_data(self.xdata_g1, self.ydata_g1)
		elif self.x >= xmax_g2:
			self.g2.set_xlim(xmax_g2/2, 2*xmax_g2)
			self.g2.figure.canvas.draw()
		elif self.x >= xmax_g3:
			self.g3.set_xlim(xmin_g3, 2*xmax_g3)
			self.g3.figure.canvas.draw()
		elif self.x >= xmax_g4:
			self.g4.set_xlim(xmin_g4, 2*xmax_g4)
			self.g4.figure.canvas.draw()
			

		#self.line_g1.set_data(self.x, y)
		#self.line_g1.set_xdata(np.append(self.line_g1.get_xdata(), new_data))
    

		self.line_g1.set_data(self.x, y)
		#self.line_g1.set_data(y)

		self.line_g2.set_data(self.x, y)
		self.line_g3.set_data(self.x, y)
		self.line_g4.set_data(self.x, y)
		
		#rescale plot
		#self.g1.relim() 
		#self.g1.autoscale_view()
		
		#self.g1.figure.canvas.draw()
		#plt.draw()
		plt.show()
		#self.fig.canvas.flush_events()
		plt.pause(1)
		

	def __init__(self):
		self.fig = plt.figure()
		self.g1 = self.fig.add_subplot(2,2,1)
		self.g2 = self.fig.add_subplot(2,2,2)
		self.g3 = self.fig.add_subplot(2,2,3)
		self.g4 = self.fig.add_subplot(2,2,4)
		
		self.xdata_g1, self.ydata_g1 = [], []
		self.xdata_g2, self.ydata_g2 = [], []
		self.xdata_g3, self.ydata_g3 = [], []
		self.xdata_g4, self.ydata_g4 = [], []
		 
		self.line_g1, = self.g1.plot([], [])
		#self.line_g1 = plt.plot([],[])
		self.g1.set_xlim(0, 60)
		self.g1.set_ylim(0, 120)
		self.g1.grid()
        
		self.line_g2, = self.g2.plot([], [], color='black')
		self.g2.set_xlim(0,60)
		self.g2.set_ylim(0,120)
		self.g2.grid()
		
		self.line_g3, = self.g3.plot([], [], color='red')
		self.g3.set_xlim(0,60)
		self.g3.set_ylim(0,120)
		self.g3.grid()
		
		self.line_g4, = self.g4.plot([], [], color='green')
		self.g4.set_xlim(0,60)
		self.g4.set_ylim(0,120)
		self.g4.grid()
		
		self.x = 1
		
		
	#def draw(self):
	#	ani = animation.FuncAnimation(self.fig, self.data_update, 60, blit=False, interval=10, repeat=False)
	#	plt.show()

	
		
