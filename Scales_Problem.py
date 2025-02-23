import random as rd
import copy as cp


class Scales:
    def __init__(self, data):
        self.data = data
        # Create a random solution (list of 0s and 1s)
        self.solution = [rd.randint(0, 1) for _ in range(len(data))]
        self.fitness = 0.00
        self.calculate_fitness()  # Calculate fitness based on the current solution

    def print_solution(self):
        for i in self.solution:
            print(i, end=" ")
        print("\tFitness:", self.fitness)

    # Calculate the fitness as the absolute difference between the two pans.
    def calculate_fitness(self):
        left = 0
        right = 0
        # For each weight, add it to left or right based on the binary value.
        for i, bit in enumerate(self.solution):
            if bit == 0:
                left += self.data[i]
            else:
                right += self.data[i]
        self.fitness = abs(left - right)

    # Copy the solution from another Scales object.
    def copy_solution(self, another_scales):
        self.solution = cp.deepcopy(another_scales.solution)
        self.calculate_fitness()
