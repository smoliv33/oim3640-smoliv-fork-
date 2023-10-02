# Create function(s) that execute a simulation 10 times. Within each simulation, roll 100 dice (🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲...) and display the resulting sum.

"""
I will create two functions.

Function 1: one simulation, rolling 100 dice - generate 100 random integers between 1 and 6 and sum up
Pseudocode:
1. create a variable to store the sum, initialize to 0 
2. repeat the following step(s) 100 times:
    2.1. generate a random number between 1 and 6
    2.2. add the random number to the sum variable
3. print the sum
    

Function 2: repeat the simulation 10 times
Pseudocode:
- repeat the following step(s) 10 times:
    - call function 1
"""
import random


def one_simulation(n=100, sides=6):
    """one simulation, rolling n (by default 100) dice, return the sum"""
    # print('We found the sum!') # Fake it till make it
    total = 0
    for i in range(n):
        random_number = random.randint(1, sides)
        total += random_number
    return total


def repeat_simulations(n=10):
    """repeat the simulation 10 times, each simulation is rolling ? dice"""
    for i in range(n):
        result = one_simulation(n=1000, sides=20)
        print(f'Simulation {i+1}: sum = {result}')


# repeat_simulations(5)

# Write a function to simulate rolling 100 dice and count how many simulations it takes to reach to a sum of 400

def count_simulations():
    counter = 0
    while True:
        total = one_simulation()
        print(total)
        counter += 1
        if total >= 400:
            return counter, total

        

number_times, last_total = count_simulations()
print(f'It takes {number_times} to reach to 400. The last sum is {last_total}.')
