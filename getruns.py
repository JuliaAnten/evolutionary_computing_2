# imports framework
import sys,os
sys.path.insert(0, 'evoman')
from environment import Environment
from demo_controller import player_controller

# imports other libs
import numpy as np

experiment_name = 'controller_generalist_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# Update the number of neurons for this specific example
n_hidden_neurons = 10

# initializes environment for multi objetive mode (generalist)  with static enemy and ai player
env = Environment(experiment_name=experiment_name,
				  playermode="ai",
				  player_controller=player_controller(n_hidden_neurons),
		  		  speed="fastest",
				  enemymode="static",
				  level=2)

sol = np.loadtxt('alterresults/bestrun0.txt')
print('\n LOADING SAVED GENERALIST SOLUTION FOR ALL ENEMIES \n')

results = []

for i in range(5):
    results.append([])
    # tests saved demo solutions for each enemy
    for en in range(1, 9):
    	
    	#Update the enemy
        env.update_parameter('enemies',[en])
        
        env.play(sol)
        results[-1].append(env.fitness_single())

with open("bestrunfitness0.txt", "w") as txt_file:

    for row in results:
        txt_file.write(str(row)+"\n")

