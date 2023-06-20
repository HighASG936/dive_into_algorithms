import math
import matplotlib.pyplot as plt
import time
import os
from random import  randint


def income(edu_yrs):
    """Income function"""
    return math.sin((edu_yrs - 10.6) * (2 * math.pi / 4)) + ((edu_yrs - 11) / 2)

def income_derivative(edu_yrs):
    """Derivative of income function"""
    return(math.cos( (edu_yrs - 10.6) * (2 * math.pi/4) ) + 1/2 )

def find_local_maxima(current_education):
    """Seek maxima of function by gradient ascent"""
    threshold = 0.0001
    maximum_iterations = 100000
    step_size = 0.001

    keep_going = True
    iterations = 0

    while(keep_going):
        education_change = step_size * income_derivative(current_education)
        current_education = current_education + education_change
        if abs(education_change) < threshold or iterations >= maximum_iterations:
            keep_going = False                
        iterations += 1
        print(f"Current Education:\t{current_education}\nIncome:\t{income(current_education)}")
        os.system('clear')   

    print(f"Current Education:\t{current_education}\nIncome:\t{income(current_education)}")
    return current_education    

def find_global_maxima(random_edu_yrs):
    """ """
    max_income = 0

    for yr in random_edu_yrs:
        current_education = yr
        current_education = find_local_maxima(current_education)
        current_max_income = income(current_education)

        if current_max_income > max_income:
            maxima = current_education
            max_income = current_max_income
    return maxima

def randomnize_edu_yrs(random_edu_yrs):
    """Generate random array of ages"""
    for _ in range(0, 10):
        random_edu_yrs.append(randint(11, 20))
    random_edu_yrs = list(set(random_edu_yrs))
    print(random_edu_yrs)
    time.sleep(2)    

def plot_function(xs, ys):
    """Plot function"""
    plt.plot(xs, ys)
    plt.title('Education and Income')
    plt.xlabel('Years of Education')
    plt.ylabel('Lifetime Income')

def plot_current_education(current_education):
    """Plot current education using a red 'o' """
    plt.plot(current_education, income(current_education), 'ro')

if __name__ == "__main__":
    xs = [11 + x / 100 for x in list(range(901))]
    ys = [income(x) for x in xs]
    random_edu_yrs = []

    #Plot function
    plot_function(xs, ys)

    #Looking for solution
    randomnize_edu_yrs(random_edu_yrs)
    solution = find_global_maxima(random_edu_yrs)
    
    #Plot solution
    plot_current_education(solution)
    
    plt.show()

