import random
voc = [x for x in range(97, 123)]
voc.append(32)

class Individual:
    def __init__(self, ind_len):
        self.length = ind_len
        self.fitnnes = -1
        self.DNA = ""
        # for i in range(ind_len):
        #     letter = random.randint(97, 122)
        #     self.DNA += chr(letter)
        for i in range(ind_len):
            letter = random.randint(0, len(voc)-1)
            self.DNA += chr(voc[letter])

    def __str__(self):
        return self.DNA

    def __repr__(self):
        return self.DNA

    # fitnnes function
    def calc(self, target):
        score = 0
        for i in range(len(self.DNA)):
            if self.DNA[i] == target[i]:
                score += 1

        self.fitnnes = score

    # not finished!
    def crossover(self, parentB):
        new_individual = Individual(self.length)

        return new_individual