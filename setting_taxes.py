import math
import matplotlib.pyplot as plt
import os
import time

def revenue(tax):
    """Taxes Formula"""
    return(100 * (math.log(tax + 1) - (tax -0.2)**2 + 0.04))

def revenue_derivative(tax):
    """revenue derivative """
    return(100 * (1/(tax + 1) - 2 * (tax - 0.2) ) )

def search_maxima(current_rate):
    """Algorithm no search maximun performance to revenue taxes """
    threshold = 0.0001
    maximum_iterations = 100000
    keep_going = True
    iterations = 0
    step_size = 0.001

    os.system('clear')
    while(keep_going):
        rate_change = step_size * revenue_derivative(current_rate)
        current_rate = current_rate + rate_change

        if abs(rate_change) < threshold or iterations >= maximum_iterations:
            keep_going = False

        iterations += 1

        print(f"Current Rate:\t{current_rate}\nRevenue:\t{revenue(current_rate)}")
        time.sleep(0.1)
        os.system('clear')        

    print(f"Current Rate:\t{current_rate}\nRevenue:\t{revenue(current_rate)}")
    return current_rate


if __name__ == "__main__":
    xs = [x/1000 for x in range(1001)]
    ys = [revenue(x) for x in xs]
    current_rate = 0.9

    current_rate = search_maxima(current_rate)

    plt.plot(xs, ys)
    plt.plot(current_rate, revenue(current_rate), 'ro')
    plt.title('Tax Rates and Revenue')
    plt.xlabel('Tax Rate')
    plt.ylabel('Revenue')
    plt.show()
