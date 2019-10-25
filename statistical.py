import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

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

def averages(data):

    average = []
    standard = []

    for i in range(len(data[0])):
        temp = []

        for row in range(len(data)):
            temp.append(data[row][i])

        average.append(np.mean(temp))
        standard.append(np.std(temp))

    return average, standard

endboxr = [[] for i in range(8)]
for i in range(10):
    runs = open_data("replaceresults/bestrunfitness" + str(i) + ".txt")
    runs,std = averages(runs)

    for j in range(8):
        endboxr[j].append(runs[j])

endboxr,std = averages(endboxr)


endboxa = [[] for i in range(8)]
for i in range(10):
    runs = open_data("alterresults/bestrunfitness" + str(i) + ".txt")
    runs,std = averages(runs)

    for j in range(8):
        endboxa[j].append(runs[j])

endboxa,std = averages(endboxa)
print(stats.ttest_ind(endboxr, endboxa))
