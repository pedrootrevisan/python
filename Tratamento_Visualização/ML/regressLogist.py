#adptação da regressão lienar para problemas para atender uma distribuição de bernoulli/binomial
# ou seja resultados de 0 ou 1/ Verdadeiro ou falso

import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
from sklearn.linear_model import LogisticRegression
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv('Eleicao.csv', sep = ';')
base.shape
base.head()
plt.scatter(base.DESPESAS,base.SITUACAO)
base.describe()

#visualizado coeficiente de corr
np.corrcoef(base.DESPESAS,base.SITUACAO)
#criando as variaveis x e y (independente e dependente)
#transformando x em matriz newaxis
x = base.iloc[:,2].values
x=x[:,np.newaxis]
y = base.iloc[:,1].values

modelo = LogisticRegression()
modelo.fit(x,y)
modelo.coef_
modelo.intercept_

plt.scatter(x,y)
#gerando novos dados para func sigmoide
X_teste = np.linspace(10,3000,100)
#func sigmoid
def model(x):
    return 1/(1+ np.exp(-x))
#gerando previsões
r = model(X_teste*modelo.coef_ +modelo.intercept_).ravel()
plt.plot(X_teste,r,color = 'red')

