import math
import matplotlib.pyplot as plt

def revenue(tax):
    """Taxes Formula"""
    return(100 * (math.log(tax + 1) - (tax -0.2)**2 + 0.04))

def revenue_derivative(tax):
    """revenue derivative """
    return(100 * (1/(tax + 1) - 2 * (tax - 0.2) ) )

if __name__ == "__main__":
    xs = [x/1000 for x in range(1001)]
    ys = [revenue(x) for x in xs]
    step_size = 0.001
    current_rate = 0.7
    for _ in range(0, 15):
        current_rate = current_rate + step_size * revenue_derivative(current_rate)

    print(current_rate,  revenue(current_rate))
    plt.plot(xs, ys)
    plt.plot(current_rate, revenue(current_rate), 'ro')
    plt.title('Tax Rates and Revenue')
    plt.xlabel('Tax Rate')
    plt.ylabel('Revenue')
    plt.show()
