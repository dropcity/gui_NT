import matplotlib.pyplot as plt
plt.ion()

class GraphAnimation():

	def __init__(self, name, illness, age):
		#create figure and subplots with position 1,2, 3 and 4
		self.fig = plt.figure()
		self.x_g1 = 0
		self.g1 = self.fig.add_subplot(2,2,1)
 		self.x_g2 = 0
		self.g2 = self.fig.add_subplot(2,2,2)
		self.x_g3 = 0
		self.g3 = self.fig.add_subplot(2,2,3)
		self.x_g4 = 0
		self.g4 = self.fig.add_subplot(2,2,4)

		#sets name for window
		self.fig.canvas.set_window_title('Muscle Activity')
		#Name, ilness and age of patien
		#TODO fix placing
		plt.figtext(0.05, 0.95, name)
		plt.figtext(0.20, 0.95, illness)
		plt.figtext(0.35, 0.95, age)

		#lists for x and y values
		self.xdata_g1, self.ydata_g1 = [], []
		self.xdata_g2, self.ydata_g2 = [], []
		self.xdata_g3, self.ydata_g3 = [], []
		self.xdata_g4, self.ydata_g4 = [], []

		#plot for axes g1
		self.line_g1, = self.g1.plot([], [])
		#x and y limit of axes
		self.g1.set_xlim(0, 60)
		self.g1.set_ylim(0, 120)
		#grid for graph
		self.g1.grid()

		self.line_g2, = self.g2.plot([], [])
		self.g2.set_xlim(0,60)
		self.g2.set_ylim(0,120)
		self.g2.grid()

		self.line_g3, = self.g3.plot([], [])
		self.g3.set_xlim(0,60)
		self.g3.set_ylim(0,120)
		self.g3.grid()

		self.line_g4, = self.g4.plot([], [])
		self.g4.set_xlim(0,60)
		self.g4.set_ylim(0,120)
		self.g4.grid()

	def drawG1(self, new_y):
		#draws every second
		self.x_g1 += 1
		# append new values to x ynd y lists
		self.xdata_g1.append(self.x_g1)
		self.ydata_g1.append(new_y)

		#check if drawn lines exceed x axes,
		#if so, change x axes range
		xmin_g1, xmax_g1 = self.g1.get_xlim()
		if self.x_g1 >= xmax_g1:
			self.g1.set_xlim(xmax_g1, xmax_g1+120)
		#sets the x and y value for line in axes g1
		self.line_g1.set_data(self.x_g1, new_y)

		#rescale plot
		self.g1.relim()
		self.g1.autoscale_view()
		#plot and show line g1 and pause for 1 millisec
		self.g1.plot(self.xdata_g1, self.ydata_g1, '-k')
		plt.show()
		plt.pause(0.1)

	def drawG2(self, new_y):
		self.x_g2 += 1

		self.xdata_g2.append(self.x_g2)
		self.ydata_g2.append(new_y)

		xmin_g2, xmax_g2 = self.g2.get_xlim()

		if self.x_g2 >= xmax_g2:
			self.g2.set_xlim(xmax_g2, xmax_g2+120)

		self.line_g2.set_data(self.x_g2, new_y)

		#rescale plot
		self.g2.relim()
		self.g2.autoscale_view()

		self.g2.plot(self.xdata_g2, self.ydata_g2, '-b')
		plt.show()
		plt.pause(0.1)

	def drawG3(self, new_y):
		self.x_g3 += 1

		self.xdata_g3.append(self.x_g3)
		self.ydata_g3.append(new_y)

		xmin_g3, xmax_g3 = self.g3.get_xlim()

		if self.x_g3 >= xmax_g3:
			self.g3.set_xlim(xmax_g3, xmax_g3+120)

		self.line_g3.set_data(self.x_g3, new_y)

		#rescale plot
		self.g3.relim()
		self.g3.autoscale_view()

		self.g3.plot(self.xdata_g3, self.ydata_g3, '-g')
		plt.show()
		plt.pause(0.1)

	def drawG4(self, new_y):
		self.x_g4 += 1

		self.xdata_g4.append(self.x_g4)
		self.ydata_g4.append(new_y)

		xmin_g4, xmax_g4 = self.g4.get_xlim()

		if self.x_g4 >= xmax_g4:
			self.g4.set_xlim(xmax_g4, xmax_g4+120)

		self.line_g4.set_data(self.x_g4, new_y)

		#rescale plot
		self.g4.relim()
		self.g4.autoscale_view()

		self.g4.plot(self.xdata_g4, self.ydata_g4, '-r')
		plt.show()
		plt.pause(0.1)
