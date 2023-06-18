import math
import matplotlib.pyplot as plt


def income(edu_yrs):
    """Income function"""
    return math.sin((edu_yrs - 10.6) * (2 * math.pi / 4)) + ((edu_yrs - 11) / 2)


if __name__ == "__main__":
    xs = [11 + x / 100 for x in list(range(901))]
    ys = [income(x) for x in xs]
    plt.plot(xs, ys)
    current_edu = 12.5
    plt.plot(current_edu, income(current_edu), 'ro')
    plt.title('Education and Income')
    plt.xlabel('Years of Education')
    plt.ylabel('Lifetime Income')
    plt.show()
