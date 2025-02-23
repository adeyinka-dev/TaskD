import file
import Scales_Problem as sp
import random as rd


class Hill_Climbing:

    def __init__(self, data):
        # Create two solutions: one current and one for exploring small changes.
        self.solution1 = sp.Scales(data)
        self.solution2 = sp.Scales(data)
        self.solution2.copy_solution(self.solution1)

    # Performs a small change (perturbation) on solution2.
    def small_change(self):
        index = rd.randint(0, len(self.solution2.solution) - 1)
        # Flip the bit at the chosen index.
        self.solution2.solution[index] = 1 - self.solution2.solution[index]
        self.solution2.calculate_fitness()

    def run_hc(self, iter):
        results = []  # To record the iteration, fitness, and solution.
        print("Initial solution:")
        self.solution1.print_solution()

        for i in range(iter):
            row = []
            print("Iteration", i + 1)

            # Make a small change to explore a neighbor.
            self.small_change()
            print("New solution:")
            self.solution2.print_solution()

            print("Current solution:")
            self.solution1.print_solution()

            # If the new solution (solution2) is better, copy it to solution1.
            if self.solution2.fitness < self.solution1.fitness:
                self.solution1.copy_solution(self.solution2)
                print("Improved! Updated current solution:")
                self.solution1.print_solution()

            # Record the iteration number, current fitness, and current solution.
            row.append(i + 1)
            row.append(self.solution1.fitness)
            row.append(self.solution1.solution.copy())

            results.append(row)
            print()

        file.write_result(results)
