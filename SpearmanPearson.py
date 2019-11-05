import matplotlib.pyplot as plt
import pandas as pd 
from datetime import datetime 
from scipy.stats import spearmanr,pearsonr,gaussian_kde
import numpy as np
#inputs
pairsIndices = [[10,18],[10,21],[10,27], [7,57]] #, [41,21], [23, 29], [12,40], [11, 22], [37, 49]]
rows,columns = 2,2
#end inputs

pairs = []
#rename pairs as column names
for pair in pairsIndices:
    pairs.append(['answer_' + str(pair[0]) + '_N', 'answer_' + str(pair[1]) + '_N'])

file = r'data/2019-07-09-SPSS.xls'
df = pd.read_excel(file)

fig, axs = plt.subplots(rows,columns)
axs = axs.ravel()

index = 0
for pair in pairs:
    #use alpha coloring to see the density of points
    axs[index].scatter(df[pair[0]], df[pair[1]], s=80, alpha=0.02) 
    axs[index].set_xlabel(pairsIndices[index][0], fontsize = 8)
    axs[index].set_ylabel(pairsIndices[index][1], fontsize = 8)
    scorr, p_value = spearmanr(df[pair[0]], df[pair[1]])
    pcorr, p_value = pearsonr(df[pair[0]], df[pair[1]])
    axs[index].set_title("Spear " + str(round(scorr**2, 3)) + " Pear " +str(round(pcorr**2, 3)), fontsize = 8)
    
    #set ticks on x and y axes
    axs[index].xaxis.set_major_locator(plt.MaxNLocator(len(df[pair[0]].unique())))
    axs[index].yaxis.set_major_locator(plt.MaxNLocator(len(df[pair[1]].unique())))
    index = index + 1

plt.tight_layout()
filename = datetime.now().strftime("%Y-%m-%d %H_%M_%S") +  "_SpearPearCorrScatter.png"
figPath = "Figs\\" + filename
plt.savefig(figPath)
plt.show()