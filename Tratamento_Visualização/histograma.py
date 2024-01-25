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

#caso 2
base2 = pd.read_csv('chicken.csv')
base2.head()
#criando novo data frame agrupando o atributo 'feed'
agrupado = base.groupby(['feed'])['weight'].sum()
agrupado
#novo data frame para testar os filtros
teste = base2.loc[base2['feed']== 'horsebean']
teste
#impressao em grafico 2x3
plt.figure()
plt.subplot(3,2,1)
sb.histplot(base2.loc[base2['feed']== 'horsebean'].weight, kde=True).set(title='horsebean')
plt.subplot(3,2,2)
sb.histplot(base2.loc[base2['feed']== 'casein'].weight, kde=True).set(title='casein')
plt.subplot(3,2,3)
sb.histplot(base2.loc[base2['feed']== 'linseed'].weight, kde=True).set(title='linseed')
plt.subplot(3,2,4)
sb.histplot(base2.loc[base2['feed']== 'meatmeal'].weight, kde=True).set(title='meatmeal')
plt.subplot(3,2,5)
sb.histplot(base2.loc[base2['feed']== 'soybean'].weight, kde=True).set(title='soybean')
plt.subplot(3,2,1)
sb.histplot(base2.loc[base2['feed']== 'sunflower'].weight, kde=True).set(title='sunflower')
#ajusta layout para nao haver sobreposição
plt.tight_layout()






