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
    xs2 = [0.1, 2]
    ys2 = [ball_trajectory(0.1), 0]
    xs3 = [0.2, 2]
    ys3 = [ball_trajectory(0.2), 0]
    xs4 = [0.3, 2]
    ys4 = [ball_trajectory(0.3), 0]
    xs5 = [0.3,0.3]
    ys5 = [0, ball_trajectory(0.3)]
    xs6 = [0.3, 2]
    ys6 = [0, 0]

    plt.text(0.31, ball_trajectory(0.3)/2, 'A', fontsize=16)
    plt.text((0.3+2)/2, 0.05, 'B', fontsize=16)
    plt.plot(xs, ys, xs2, ys2, xs3, ys3, xs4, ys4, xs5, ys5, xs6, ys6)
    plt.title("The trajectory of a Thrown Ball")
    plt.xlabel("Horizontal Position of Ball")
    plt.ylabel("Vertical Position of Ball")
    plt.axhline(y=0)
    plt.show()
    

if __name__ == '__main__':
    plot_trajectory()
    



