###################################
# EvoMan FrameWork - 2020         #
# Authors: Julia Anten,           #
# Jasper den Duijf, Romy Meester, #
# Nathalie van Sterkenburg        #
###################################

# imports framework
import sys, os
sys.path.insert(0, 'evoman')
from environment import Environment
from general_functions import *
import matplotlib.pyplot as plt

from demo_controller import player_controller
import numpy as np

experiment_name = 'controller_generalist_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# derived from dummy_demo and optimization_generlist_demo,
# and controller_generalist_demo
# you are required to use the neural network (demo_controller.py)
# available from (optimization_generalist_demo.py)

n_hidden_neurons = 10
input_sensor = 20
output_sensor = 5
elements = n_hidden_neurons * (input_sensor + output_sensor) + output_sensor + n_hidden_neurons

def main(pop_size, mutation_rate, nr_generations, initial_parent="sparse", enemy = [1], mutation = "replace"):

    # initializes environment with ai player using random controller, playing against static enemy
    env0 = Environment(experiment_name=experiment_name,
                      player_controller=player_controller(n_hidden_neurons),
                      speed='fastest',enemies=[enemy[0]])
    
    env1 = Environment(experiment_name=experiment_name,
                      player_controller=player_controller(n_hidden_neurons),
                      speed='fastest',enemies=[enemy[1]])

    # Create the population
    population = initial_population(pop_size, initial_parent)
    meanlist = []
    maxlist = []

    maxfitness = 0
    for i in range(nr_generations):
        print(i)

        fitnesslist = []
        # check for the entire population the fitness
        for index, individual in enumerate(population):
            env0.play(np.array(individual))
            env1.play(np.array(individual))
            fitnesslist.append(env0.fitness_single()+env1.fitness_single())
            if fitnesslist[-1] > maxfitness:
                maxfitness = fitnesslist[-1]
                with open("woohoo.txt", "w") as txt_file:
                    for el in individual:
                        txt_file.write(str(el)+ "\n")


        new_population = []
        for j in range(int(pop_size/2)):
            parent1, parent2 = parent_selection(len(fitnesslist), fitnesslist)
            child1, child2 = cross_breeding(population[parent1], population[parent2])
            
            if mutation == "replace":
                mutate_replace(child1, mutation_rate), mutate_replace(child2, mutation_rate)
            else:
                mutate_alter(child1, mutation_rate), mutate_alter(child2, mutation_rate)
            
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
        meanlist.append(np.mean(fitnesslist))
        maxlist.append(np.max(fitnesslist))
    print(maxfitness)
    plt.plot(meanlist)
    plt.plot(maxlist)

    plt.show()

# Run the algorithm
if __name__ == '__main__':

    # Parameters for experiment
    selection = "sparse" # sparse or full
    # m_rate = 0.01??
    level = 1
    mutate_type = "alter" # alter or replace

    main(pop_size=64, mutation_rate=1/elements, nr_generations=10, initial_parent=selection, enemy = [4,7], mutation = mutate_type)
