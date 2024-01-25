import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

base = pd.read_csv('tree.csv')
base.shape
#dados
base.head()
#gerando boxplot
#showfliers = outliers
plt.boxplot(base.Volume, showfliers= True, patch_artist= True)

#gerando um para cada info
plt.boxplot(base.Volume)
plt.boxplot(base.Girth)
plt.boxplot(base.Height)
plt.title('Arvores')


sb.boxplot(data=base.Volume, orient='v').set_title('Arvore')
sb.boxplot(data=base) #mostra mais de um



