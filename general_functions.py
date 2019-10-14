###################################
# EvoMan FrameWork - 2020         #
# Authors: Julia Anten,           #
# Jasper den Duijf, Romy Meester, #
# Nathalie van Sterkenburg        #
###################################


# imports framework
import random
import numpy as np

def initial_population(pop_size=32, type="Full", loc = 0, scale = 1, size = 265, sparse = 0.99):
    if type.lower() not in ["full", "sparse"]:
        raise NameError("Check carefully how you want to initiate the first population!")

    population = list()
    for i in range(pop_size):
        controller = np.random.normal(loc = loc, scale = scale, size=(size))
        for i, el in enumerate(controller):
            if np.random.random() > sparse and type.lower() == "sparse":
                controller[i] = 0
        population.append(controller)

    return population


def parent_selection(player_number, fitnesses):
    #tournament
    #to do: maak clonen onmogelijk

    parent1 = 0
    parent2 = 0

    a = random.randint(0,player_number-1)
    b = random.randint(0,player_number-1)

    if fitnesses[a] > fitnesses[b]:
        parent1 = a
    else:
        parent1 = b

    while True:

        a = random.randint(0,player_number-1)
        b = random.randint(0,player_number-1)

        if fitnesses[a] > fitnesses[b]:
            parent2 = a
        else:
            parent2 = b

        if parent1 == parent2:
            break

    return parent1,parent2

def cross_breeding(parent1, parent2):
    # coinflip
    # Rekening houden met welke waardes bias is!

    child1 = []
    child2 = []

    for i in range(len(parent1)):

        if random.random() > 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])

        else:
            child1.append(parent2[i])
            child2.append(parent1[i])

    return child1, child2

def mutate(player, mutation_rate):
    # 1 waarde vervangen (uit normaal distribution)

    if random.random() < mutation_rate:
        
        for i in range(5):
            player[random.randint(0,len(player)-1)] = np.random.normal(loc = 0, scale=1)
