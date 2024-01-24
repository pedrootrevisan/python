#histograma
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

base = pd.read_csv('tree.csv')
base.shape
#dados
base.head()
#criação do hist, considerando apenas o segundo atributo da bs[ase de dados e com duas divisões
#a variavel 'h' armazena as faixas de valores de Height
h=np.histogram(base.iloc[:,1], bins=6)
h
#visualização
plt.hist(base.iloc[:,1], bins=6)
plt.title('Árvores')
plt.ylabel('Frequencia')
plt.xlabel('Altura')

#usando seaborn
sb.histplot(base.iloc[:,1],kde=False , bins=6, color = 'blue').set(title = 'Arvores')
#Linha de densidade, metodo kdeplot para densidade
sb.histplot(base.iloc[:,1], bins=6, color = 'blue')

#densidade e histograma
sb.histplot(base.iloc[:,1],kde=True , bins=6, color = 'blue').set(title = 'Arvores')





