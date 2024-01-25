import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

base = pd.read_csv('tree.csv')
base.shape
#dados
base.head()
#grafico dispersao considerando volume e dispersão
plt.scatter(x=base.Girth, y = base.Volume, color = 'blue', facecolors = 'none', marker='.')
plt.title('Árvores')
plt.ylabel('Circunferencia')
plt.xlabel('Volume')

#grafico de linha
plt.plot(base.Girth,base.Volume)
plt.ylabel('Circunferencia')
plt.xlabel('Volume')
#grafico de dispersão com afastamento de dados (jitter)
#fit_reg (linha de tendencia)
sb.regplot(x=base.Girth, y = base.Volume, data=base, x_jitter=0.3,fit_reg=False )




