import random
from Population import Population
from Individual import Individual


def brute_force_solution(target):
    number = 0
    not_found = True
    while not_found:
        number += 1
        tryy = ""
        for i in range(len(target)):
            letter = random.randint(97, 122)
            tryy += chr(letter)
        print(tryy)
        if tryy == target:
            not_found = False
            print("Found it! in " + str(number))


voc = [x for x in range(97, 123)]
voc.append(32)
# print(voc)

target = "to be"

# brute_force_solution(target)

pop = Population(50, target)
print(pop)

pop.calculate_fitnnes()

p = sorted(pop.pop, key=lambda x: x.fitnnes)
maxx = p[len(p)-1]
print(maxx)
print(target)
print(maxx.fitnnes)
#
# # inf = Individual(10)
# # print(inf)
