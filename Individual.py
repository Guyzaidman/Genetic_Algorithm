import random


class Individual:
    def __init__(self, ind_len):
        self.DNA = []
        for i in range(ind_len):
            letter = random.randint(97, 122)  # 123?
            self.DNA.append(chr(letter))

    def __str__(self):
        return str(self.DNA)