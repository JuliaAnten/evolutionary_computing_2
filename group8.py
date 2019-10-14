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

def main(pop_size, mutation_rate, nr_generations, initial_parent="sparse", enemy = 1):

    # Create the population
    # population = initial_population(pop_size, initial_parent)

    # check for the entire population the fitness
    # for index, data in enumerate(population):
    #     fitness = fitnesscheck(data, enemy = [enemy])


    # initializes environment with ai player using random controller, playing against static enemy
    env = Environment(experiment_name=experiment_name,
                      player_controller=player_controller(n_hidden_neurons),
                      speed='fastest')
    controller = np.random.normal(loc = 0, scale=1, size=(elements))
    # for i, el in enumerate(controller):
    #     if np.random.random() > 0.01:
    #         controller[i] = 0
    env.play(controller)

# Run the algorithm
if __name__ == '__main__':

    # Parameters for experiment
    selection = "sparse" #or full
    # m_rate = 0.01??
    level = 1

    main(pop_size=10, mutation_rate=0.01, nr_generations=5, initial_parent=selection, enemy = level)
