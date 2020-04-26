import matplotlib.pyplot as plt
import csv
import numpy as np

bins = 20
ystep = 100.0/bins  # max y is 100
xstep = 1000.0/bins # max x is 1000

fig,(ax1, ax2, ax3) = plt.subplots(1,3, figsize=(13, 6))

density = np.zeros((bins+1, bins+1))
with open("airbnb-2020-mar-london.csv", encoding="utf-8") as f:
        rdr = csv.reader(f, delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
        next(rdr)
        for cols in rdr:
                if cols[82] == '':
                        x = 0
                else:
                        x = int(float(cols[82]) / xstep) # number of reviews
                if cols[86] == '':
                        y = 0
                else:
                        y = int(float(cols[86])/ ystep) # review score of rating
                density[y][x] += 1   # frequency 

ylabels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
xlabels = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

org = density.copy()
for i in range(bins+1):
        for j in range(bins+1):
                if density[i][j] >= 1 and density[i][j] < 10:  #  from 1 to 9
                        continue
                density[i][j] = np.nan  # zero is displayed as blank

heatmap1 = ax1.pcolor(density, cmap=plt.cm.viridis)
ax1.set_yticks(np.arange(0, bins+1, 2))
ax1.set_yticklabels(ylabels)
ax1.set_xticks(np.arange(0, bins+1, 2))
ax1.set_xticklabels(xlabels, rotation=45)
ax1.xaxis.tick_top()
fig.colorbar(heatmap1, ax=ax1, orientation="horizontal")

density = org.copy()
for i in range(bins+1):
        for j in range(bins+1):
                if density[i][j] >= 10 and density[i][j] < 100:  # from 10 to 99
                        continue
                density[i][j] = np.nan

heatmap2 = ax2.pcolor(density, cmap=plt.cm.plasma)
ax2.set_yticks(np.arange(0, bins+1, 2))
ax2.set_yticklabels(ylabels)
ax2.set_xticks(np.arange(0, bins+1, 2))
ax2.set_xticklabels(xlabels, rotation=45)
ax2.xaxis.tick_top()
fig.colorbar(heatmap2, ax=ax2, orientation="horizontal")

density = org.copy()
for i in range(bins+1):
        for j in range(bins+1):
                if density[i][j] >= 100 and density[i][j] < 100000:  # from 100 
                        continue
                density[i][j] = np.nan

heatmap3 = ax3.pcolor(density, cmap=plt.cm.cividis)
ax3.set_yticks(np.arange(0, bins+1, 2))
ax3.set_yticklabels(ylabels)
ax3.set_xticks(np.arange(0, bins+1, 2))
ax3.set_xticklabels(xlabels, rotation=45)
ax3.xaxis.tick_top()
fig.colorbar(heatmap3, ax=ax3, orientation="horizontal")


plt.show()

