################################
# EvoMan FrameWork - V1.0 2016 #
# Author: Karine Miras         #
# karine.smiras@gmail.com      #
################################

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
print(elements)

# initializes environment with ai player using random controller, playing against static enemy

for i in range(20):
    env = Environment(experiment_name=experiment_name,
                      player_controller=player_controller(n_hidden_neurons),
                      speed='fastest')
    controller = np.random.normal(loc = 0, scale=1, size=(elements))
    # for i, el in enumerate(controller):
    #     if np.random.random() > 0.01:
    #         controller[i] = 0
    env.play(controller)
