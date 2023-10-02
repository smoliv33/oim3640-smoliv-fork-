# Create function(s) that execute a simulation 10 times. Within each simulation, roll 100 dice (🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲...) and display the resulting sum.

"""
I will create 2 functions

Function 1: one simulation, roll 100 dice
Rolling 100 dice means generating 100 random numbers and sum up 

Pseudocode:
1. create a variable to store the sum
2. repeat the following 100 times:
    1. generate a random integer between 1 and 6
    2. add the random integer to the sum variable
3. print the sum


Function 2: repeat function 1 (simulation) 10 times
1. Repeat the following 10 times
    - call function 1

"""
import random


def one_simulation(n=100, sides=6):
    """
    roll n (default 100) dice, return the sum
    """
    # print('We found the sum!') # Fake it till make it
    total = 0
    for i in range(n):
        random_number = random.randint(1, sides)
        total += random_number
    # print(total)
    return total


def repeat_simulation(n=10):
    """repeat the simulation 10 times"""
    for i in range(n):
        result = one_simulation(n=1000000)
        print(f'Simulation {i+1}: sum = {result}')


# repeat_simulation(20)

# Write a function to simulate rolling 100 dice and count how many simulations it takes to reach to a sum of 600

def count_simulations(n=400):
    """count how many simulations it takes to reach to a sum of n"""
    counter = 0
    
    while True:
        total = one_simulation(n=100)
        print(total)
        counter += 1
        if total >= n:
            break
        
    print(counter)


count_simulations()
