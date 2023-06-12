import matplotlib.pyplot as plt

def ball_trajectory(x):
    """Describe a trayectory of a thrown ball using Galileo's equations"""
    a = -9.81 # m/s^2
    vx = 0.99   # m/s
    vy = 9.9   # m/s
    location = (vy/vx)*x + (a/(2*vx**2))*x**2
    return location

def plot_trajectory():
    """Plot trjectory of the ball"""
    xs = [x/100 for x in list(range(201))]
    ys = [ball_trajectory(x) for x in xs]
    plt.plot(xs, ys)
    plt.title("The trajectory of a Thrown Ball")
    plt.xlabel("Horizontal Position of Ball")
    plt.ylabel("Vertical Position of Ball")
    plt.axhline(y=0)
    print(xs[0])
    plt.show()
    

if __name__ == '__main__':
    plot_trajectory()
    



