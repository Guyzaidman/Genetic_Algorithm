import random
from Individual import Individual


class Population:
    def __init__(self, pop_size, target):
        self.size = pop_size
        self.target = target
        self.pop = []

        for i in range(pop_size):
            ind = Individual(len(target))
            self.pop.append(ind)

    def calculate_fitnnes(self):
        for i in range(len(self.pop)):
            self.pop[i].calc(self.target)

    # returns a random Individual! not done!!!
    def select_from_population(self):
        n = random.randint(0, len(self.size))
        return self.pop[n]

    def selection(self):
        new_pop = []
        for i in range(len(self.pop)):
            parentA = self.select_from_population()
            parentB = self.select_from_population()

            newind = parentA.crossover(parentB)
            newind.mutate()

            new_pop.append(newind)

    def __str__(self):
        return str(self.pop)