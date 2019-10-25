# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:49:24 2019

@author: Gebruiker
"""

import matplotlib.pyplot as plt

def open_data(filename):
    with open(filename, "r") as txt_file:
        results = txt_file.read().split('\n')

        if len(results) % 2 == 0:
            results.pop(-1)

        for i in range(len(results)):
            results[i] = results[i].strip("[").strip("]")
            results[i] = results[i].split(",")

            for j in range(len(results[i])):
                results[i][j] = float(results[i][j].strip())

    return results

def simple_data(filename):
    with open(filename, "r") as txt_file:
        results = txt_file.read().split('\n')

        if len(results) % 2 == 1:
            results.pop(-1)
        
        for i in range(len(results)):
            results[i] = float(results[i])
    
    return results

def line_plot(best, average):
    
    plt.figure()
    plt.plot(best)
    plt.plot(average)
    plt.title("Fitness scores for replace mutation")
    plt.xlabel("generation")
    plt.ylabel("fitness")
    plt.legend(["best result", "average result"])
    plt.show()
    
def boxplot(replace,alter):
    
    plt.figure()
    box1 = plt.boxplot(replace,positions=[0.75],patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box1[element], color='red')
    for patch in box1['boxes']:
        patch.set(facecolor='white')
        
    box2 = plt.boxplot(alter,positions=[1.25],patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box2[element], color='green')
    for patch in box2['boxes']:
        patch.set(facecolor='white')
    plt.xticks([0.75,1.25],["replace mutation", "alter mutation"])
    plt.xlim([0.5,1.5])
    plt.ylabel("fitness")
    plt.title("average fitness over all 8 levels for the best solution per run")
    plt.show()
    

def averages(data):
    print(data)
    
    average = []
    
    for i in range(len(data[0])):
        print(i)
        current = 0
        
        for row in range(len(data)):
            #print(data)
            current += data[row][i]
            
        average.append(current/len(data))
        
    return average

maxdata = []

for i in range(10):
    maxdata.append(simple_data("replaceresults/maxfit" + str(i) + ".txt")[0:15])
    
meandata = []

for i in range(10):
    meandata.append(simple_data("replaceresults/meanfit" + str(i) + ".txt")[0:15])

maxdata = averages(maxdata)
meandata = averages(meandata)

line_plot(maxdata, meandata)
        
endbox = [[] for i in range(8)]

for i in range(10):
    runs = open_data("replaceresults/bestrunfitness" + str(i) + ".txt")
    runs = averages(runs)
    
    for j in range(8):
        endbox[j].append(runs[j])
    
endbox = averages(endbox)
boxplot(endbox,endbox)