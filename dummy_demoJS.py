################################
# EvoMan FrameWork - V1.0 2016 #
# Author: Karine Miras         #
# karine.smiras@gmail.com      #
################################

# imports framework
import  sys, os
import numpy as np
import matplotlib.pyplot as plt
from demo_controller import player_controller
sys.path.insert(0, 'evoman')
from environment import Environment

experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# initializes environment with ai player using random controller, playing against static enemy
np.random.seed(123)
# sdarray= np.linspace(0.01, 1, 100)
# ss = 1
# alltimemax = 0
# maxarray = []
# sumarray = []
# for sd in sdarray:
#     sum = 0
#     max = 0
#     for i in range(ss):
controller = np.random.normal(loc = 0, scale=sd, size=(265))

#print(controller)
env = Environment(experiment_name=experiment_name, player_controller=player_controller(), speed="fastest")
env.play(controller)

        # if env.fitness_single() > max:
        #     max = env.fitness_single()
        # if env.fitness_single() > alltimemax:
        #     alltimemax = env.fitness_single()
        #     with open("alltimemax.txt", "w") as txt_file:
        #         for el in controller:
        #             txt_file.write(str(el)+ "\n")
        # sum += env.fitness_single()
# 
#     maxarray.append(max)
#     sumarray.append(sum/ss)
#
# plt.plot(sdarray, maxarray, label = 'max')
# plt.plot(sdarray, sumarray, label = 'sum')
# plt.legend()
# plt.show()
