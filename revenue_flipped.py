import matplotlib.pyplot as plt
import math

def revenue(tax):
    """Taxes Formula"""
    return(100 * (math.log(tax + 1) - (tax -0.2)**2 + 0.04))

def revenue_derivative(tax):
    """revenue derivative """
    return(100 * (1/(tax + 1) - 2 * (tax - 0.2) ) )

def revenue_flipped(tax):
    """flipped function """
    return -revenue(tax)

def revenue_derivative_flipped(tax):
    """flipped derivative function """
    return -revenue_derivative(tax)

def search_minima(current_rate):
    """Algorithm no search minima performance to revenue taxes """
    threshold = 0.0001
    maximum_iterations = 100000
    step_size = 0.001
    keep_going = True
    iterations = 0

    while(keep_going):
        rate_change = step_size * revenue_derivative_flipped(current_rate)
        current_rate -= rate_change
        if abs(rate_change) < threshold or iterations >= maximum_iterations:
            keep_going = False
        iterations += 1
    return current_rate



if __name__ == '__main__':
    xs = [x/1000 for x in range(1001)]
    ys = [revenue_flipped(x) for x in xs]

    current_rate = 0.3
    current_rate = search_minima(current_rate)

    plt.plot(xs, ys)
    plt.plot(current_rate, revenue_flipped(current_rate), 'ro')
    plt.title('The Tax/Revenue Curve - Flipped')
    plt.xlabel('Current Tax Rate')
    plt.ylabel('Revenue - Flipped')
    plt.show()

