import matplotlib.pyplot as plt
import numpy as np
import math as m

def ask():
	global speed
	global angle
	speed = float(input("What is the speed of this trajectory?: "))
	angle = float(input("What is the angle of this trajectory?: "))
	angle = m.radians(angle)
	if type(angle) != float: 
		print("You typed the angle wrong")
		ask()
	else:
		pass
	set_axis()

def set_axis():
	global x_axis
	global y_axis
	x_axis = [x for x in range(0, 1000)]
	#y_axis = [((x * m.tan(angle)) - ((9.8 * x ** 2) / ((2 * speed ** 2) * m.cos(angle) ** 2))) for x in x_axis]
	y_axis = [(x*m.tan(angle)) - (9.8 * x ** 2) * ((1 + m.tan(angle) ** 2) / (2 * speed ** 2)) for x in x_axis]
	for y in y_axis:
		if y < 0:
			index = y_axis.index(y)
			y_axis.pop(index)
			x_axis.pop(index)
		else:
			pass
	plot()

def plot():
	x_points = np.array(x_axis)
	y_points = np.array(y_axis)

	plt.plot(x_points, y_points, "b")
	plt.show()

ask()
