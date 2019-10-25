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

def line_plot(bestr, averager,besta,averagea):
    
    plt.figure()
    plt.plot(bestr)
    plt.plot(averager)
    plt.plot(besta)
    plt.plot(averagea)
    plt.title("Fitness scores with both types of mutations")
    plt.xlabel("generation")
    plt.ylabel("fitness")
    plt.legend(["best result with replace", "average result with replace", "best result with alter", "average result with alter"])
    plt.show()
    
def enemy_plot(bestr, averager,besta,averagea):
    
    plt.figure()
    plt.plot(bestr)
    plt.plot(averager)
    plt.plot(besta)
    plt.plot(averagea)
    plt.title("Enemy life for both types of mutations")
    plt.xlabel("generation")
    plt.ylabel("life points")
    plt.legend(["best result with replace", "average result with replace", "best result with alter", "average result with alter"])
    plt.show()
    
def player_plot(bestr, averager,besta,averagea):
    
    plt.figure()
    plt.plot(bestr)
    plt.plot(averager)
    plt.plot(besta)
    plt.plot(averagea)
    plt.title("Player life for both types of mutations")
    plt.xlabel("generation")
    plt.ylabel("life points")
    plt.legend(["best result with replace", "average result with replace", "best result with alter", "average result with alter"])
    plt.show()
    
def boxplot(replace,alter):
    
    plt.figure()
    box1 = plt.boxplot(replace,positions=[0.75],patch_artist = True)
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box1[element], color='red')
    for patch in box1['boxes']:
        patch.set(facecolor='white')
        
    box2 = plt.boxplot(alter,positions=[1.25],patch_artist = True)
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
    
    average = []
    
    for i in range(len(data[0])):
        current = 0
        
        for row in range(len(data)):
            current += data[row][i]
            
        average.append(current/len(data))
        
    return average

maxdatar = []
for i in range(10):
    maxdatar.append(simple_data("replaceresults/maxfit" + str(i) + ".txt")[0:15])
    
meandatar = []
for i in range(10):
    meandatar.append(simple_data("replaceresults/meanfit" + str(i) + ".txt")[0:15])
    
maxdataa = []
for i in range(10):
    maxdataa.append(simple_data("alterresults/maxfit" + str(i) + ".txt")[0:15])
    
meandataa = []
for i in range(10):
    meandataa.append(simple_data("alterresults/meanfit" + str(i) + ".txt")[0:15])
maxdatar = averages(maxdatar)
meandatar = averages(meandatar)
maxdataa = averages(maxdataa)
meandataa = averages(meandataa)
line_plot(maxdatar, meandatar, maxdataa, meandataa)

maxdatar = []
for i in range(10):
    maxdatar.append(simple_data("replaceresults/playermax" + str(i) + ".txt")[0:15])
    
meandatar = []
for i in range(10):
    meandatar.append(simple_data("replaceresults/playerav" + str(i) + ".txt")[0:15])
    
maxdataa = []
for i in range(10):
    maxdataa.append(simple_data("alterresults/playermax" + str(i) + ".txt")[0:15])
    
meandataa = []
for i in range(10):
    meandataa.append(simple_data("alterresults/playerav" + str(i) + ".txt")[0:15])
maxdatar = averages(maxdatar)
meandatar = averages(meandatar)
maxdataa = averages(maxdataa)
meandataa = averages(meandataa)
player_plot(maxdatar, meandatar, maxdataa, meandataa)

maxdatar = []
for i in range(10):
    maxdatar.append(simple_data("replaceresults/enemymax" + str(i) + ".txt")[0:15])
    
meandatar = []
for i in range(10):
    meandatar.append(simple_data("replaceresults/enemyav" + str(i) + ".txt")[0:15])
    
maxdataa = []
for i in range(10):
    maxdataa.append(simple_data("alterresults/enemymax" + str(i) + ".txt")[0:15])
    
meandataa = []
for i in range(10):
    meandataa.append(simple_data("alterresults/enemyav" + str(i) + ".txt")[0:15])
maxdatar = averages(maxdatar)
meandatar = averages(meandatar)
maxdataa = averages(maxdataa)
meandataa = averages(meandataa)
enemy_plot(maxdatar, meandatar, maxdataa, meandataa)
        
endboxr = [[] for i in range(8)]
for i in range(10):
    runs = open_data("replaceresults/bestrunfitness" + str(i) + ".txt")
    runs = averages(runs)
    
    for j in range(8):
        endboxr[j].append(runs[j])
    
endboxr = averages(endboxr)

endboxa = [[] for i in range(8)]
for i in range(10):
    runs = open_data("alterresults/bestrunfitness" + str(i) + ".txt")
    runs = averages(runs)
    
    for j in range(8):
        endboxa[j].append(runs[j])
    
endboxa = averages(endboxa)
boxplot(endboxr,endboxa)