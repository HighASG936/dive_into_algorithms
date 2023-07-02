import matplotlib.pyplot as plt




if __name__ == '__main__':

	temperature = lambda t: 1/(t + 1)

	ts = list(range(0, 100))
	plt.plot(ts, [temperature(t) for t in ts])
	plt.title('The temperature function')
	plt.xlabel('Time')
	plt.ylabel('Temperature')
	plt.show()
	