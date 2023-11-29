import csv
import matplotlib.pyplot as plt
import numpy as np

# Maximum Strategy

maxFile = open("max_group.csv", "r")
maxData = list(csv.reader(maxFile, delimiter=","))
maxFile.close()

maxClicks = []
maxImpressions = []
maxEarnings = []
maxPurchase = []


for i in range(1, len(maxData)):
    if maxData[i][1] != "-":
        maxImpressions.append(int(maxData[i][0]))
        maxClicks.append(int(maxData[i][1]))
        maxPurchase.append(int(maxData[i][2]))
        maxEarnings.append(int(maxData[i][3]))

for i in range(len(maxClicks)):
    print("Clicks: " + str(maxClicks[i]) + " Earnings: " + str(maxEarnings[i]))


x = np.array(maxImpressions)
y = np.array(maxEarnings)
x.sort()
y.sort()
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
plt.xlabel('Impressions', fontweight='bold', color='Black', fontsize='10', horizontalalignment='center')
plt.ylabel('Earnings', fontweight='bold', color='Black', fontsize='10', horizontalalignment='center')
plt.title("Impressions to Earnings MAX")

# Show the graph
plt.show()

print("")
print("")
# Maximum Strategy

# -----------------------------------------------------------------------------------------

# Average Strategy

avgFile = open("avg_group.csv", "r")
avgData = list(csv.reader(avgFile, delimiter=","))
avgFile.close()


avgClicks = []
avgImpressions = []
avgEarnings = []
avgPurchase = []


for i in range(1, len(avgData)):
    if avgData[i][1] != "-":
        avgImpressions.append(int(avgData[i][0]))
        avgClicks.append(int(avgData[i][1]))
        avgPurchase.append(int(avgData[i][2]))
        avgEarnings.append(int(avgData[i][3]))

for i in range(len(avgClicks)):
    print("Clicks: " + str(avgClicks[i]) + " Earnings: " + str(avgEarnings[i]))

avgX = np.array(avgImpressions)
avgY = np.array(avgEarnings)
avgX.sort()
avgY.sort()
fig, ax = plt.subplots()

ax.plot(avgX, avgY, linewidth=2.0)
plt.xlabel('Impressions', fontweight='bold', color='Black', fontsize='10', horizontalalignment='center')
plt.ylabel('Earnings', fontweight='bold', color='Black', fontsize='10', horizontalalignment='center')
plt.title("Impressions to Earnings AVERAGE")

# Show the Graph
plt.show()

fig, ax = plt.subplots()

ax.plot(avgX, avgY, linewidth=2.0, label="Average")
ax.plot(x, y, linewidth=2.0, label="Maximum")
plt.xlabel('Impressions', fontweight='bold', color='Black', fontsize='10', horizontalalignment='center')
plt.ylabel('Earnings', fontweight='bold', color='Black', fontsize='10', horizontalalignment='center')
plt.title("Impressions to Earnings")


plt.legend()
plt.show()
