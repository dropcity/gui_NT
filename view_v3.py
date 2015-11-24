import matplotlib.pyplot as plt
plt.ion()

class GraphAnimation():

	def __init__(self):
		self.fig = plt.figure()
		self.x_g1 = 0
		self.g1 = self.fig.add_subplot(2,2,1)
 		self.x_g2 = 0
		self.g2 = self.fig.add_subplot(2,2,2)
		self.x_g3 = 0
		self.g3 = self.fig.add_subplot(2,2,3)
		self.x_g4 = 0
		self.g4 = self.fig.add_subplot(2,2,4)

		self.xdata_g1, self.ydata_g1 = [], []
		self.xdata_g2, self.ydata_g2 = [], []
		self.xdata_g3, self.ydata_g3 = [], []
		self.xdata_g4, self.ydata_g4 = [], []

		self.line_g1, = self.g1.plot([], [])
		self.g1.set_xlim(0, 120)
		self.g1.set_ylim(0, 100)
		self.g1.grid()

		self.line_g2, = self.g2.plot([], [])
		self.g2.set_xlim(0,120)
		self.g2.set_ylim(0,100)
		self.g2.grid()

		self.line_g3, = self.g3.plot([], [])
		self.g3.set_xlim(0,120)
		self.g3.set_ylim(0,100)
		self.g3.grid()

		self.line_g4, = self.g4.plot([], [])
		self.g4.set_xlim(0,120)
		self.g4.set_ylim(0,100)
		self.g4.grid()

	def drawG1(self, new_y):
		self.x_g1 += 5
		self.xdata_g1.append(self.x_g1)
		self.ydata_g1.append(new_y)

		xmin_g1, xmax_g1 = self.g1.get_xlim()

		if self.x_g1 >= xmax_g1:
			self.g1.set_xlim(xmax_g1, xmax_g1+120)

		self.line_g1.set_data(self.x_g1, new_y)

		#rescale plot
		self.g1.relim()
		self.g1.autoscale_view()

		self.g1.plot(self.xdata_g1, self.ydata_g1, '-k')
		plt.show()
		plt.pause(0.1)

	def drawG2(self, new_y):
		self.x_g2 += 5

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
		self.x_g3 += 5

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
		self.x_g4 += 5

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
