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

def main(index, pop_size, mutation_rate, nr_generations, initial_parent="sparse", enemy = [1], mutation = "replace"):

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
    enemyav = []
    enemymax = []
    playerav = []
    playermax = []

    maxfitness = 0
    for i in range(nr_generations):
        print(i)
        
        thisfitness = 0

        fitnesslist = []
        enemylist = []
        playerlist = []
        
        if i < nr_generations / 2:
            # check for the entire population the fitness
            for theindex, individual in enumerate(population):
                env0.play(np.array(individual))
                #env1.play(np.array(individual))
                fitnesslist.append(env0.fitness_single())
                enemylist.append(env0.get_enemylife())
                playerlist.append(env0.get_playerlife())
                if fitnesslist[-1] > maxfitness:
                    maxfitness = fitnesslist[-1]
                    with open("bestrun" + str(index) + ".txt", "w") as txt_file:
                        for el in individual:
                            txt_file.write(str(el)+ "\n")
                            
                if fitnesslist[-1] > thisfitness:
                    thisfitness = fitnesslist[-1]
                    with open("lastrun" + str(index) + ".txt", "w") as txt_file:
                        for el in individual:
                            txt_file.write(str(el)+ "\n")
                            
        else:
            # check for the entire population the fitness
            for theindex, individual in enumerate(population):
                #env0.play(np.array(individual))
                env1.play(np.array(individual))
                fitnesslist.append(env1.fitness_single())
                enemylist.append(env0.get_enemylife())
                playerlist.append(env0.get_playerlife())
                if fitnesslist[-1] > maxfitness:
                    maxfitness = fitnesslist[-1]
                    with open("bestrun" + str(index) + ".txt", "w") as txt_file:
                        for el in individual:
                            txt_file.write(str(el)+ "\n")
                            
                if fitnesslist[-1] > thisfitness:
                    thisfitness = fitnesslist[-1]
                    with open("lastrun" + str(index) + ".txt", "w") as txt_file:
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
        enemyav.append(np.mean(enemylist))
        enemymax.append(np.max(enemylist))
        playerav.append(np.mean(playerlist))
        playermax.append(np.max(playerlist))
        
    save_data(meanlist,index,"meanfit")
    save_data(maxlist,index,"maxfit")
    save_data(enemyav,index,"enemyav")
    save_data(enemymax,index,"enemymax")
    save_data(playerav,index,"playerav")
    save_data(playermax,index,"playermax")
    print(maxfitness)
    plt.plot(meanlist)
    plt.plot(maxlist)

    plt.show()
    
def save_data(data, index, title):

    with open(title + str(index) +".txt", "w") as txt_file:

        for row in data:
            txt_file.write(str(row)+"\n")

# Run the algorithm
if __name__ == '__main__':

    # Parameters for experiment
    selection = "full" # sparse or full
    # m_rate = 0.01??
    level = 1
    mutate_type = "alter" # alter or replace
    
    for i in range(10):

        main(index = i, pop_size=64, mutation_rate=20/elements, nr_generations=30, initial_parent=selection, enemy = [7,4], mutation = mutate_type)
