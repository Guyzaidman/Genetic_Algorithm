from Individual import Individual


class Population:
    def __init__(self, pop_size, individual_length):
        self.pop = []
        for i in range(pop_size):
            ind = Individual(individual_length)
            self.pop.append(ind)
