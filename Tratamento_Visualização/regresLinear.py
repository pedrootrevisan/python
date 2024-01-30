#Regressão linear mostra a  orrelação entre duas variaveis
import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv('cars.csv')
base.shape
base.head()
base.drop(['Unnamed: 0'], axis= 1)
base.head()
#definindo variaveis x e y, X distancia e a variavel independente e y distancia é a variavel dependente
x = base.iloc[:,1].values
y = base.iloc[:,0].values
x

#calculo correlação
corr = np.corrcoef(x,y)
corr

#forma de matriz com uma coluna a mais
x = x.reshape(-1,1)
#criando modelo e treino (fit indica que o modelo deve ser executado)
modelo = LinearRegression()
modelo.fit(x,y)
         
modelo.intercept_    #coeficientes
modelo.coef_         #inclinação

#visualização
plt.scatter(x,y)
plt.plot(x, modelo.predict(x), color = 'Blue')
# previsão de ponto
modelo.intercept_+modelo.coef_*22
#usando sklearn
modelo.predict([[22]])
#grafco residual
visualizador = ResidualsPlot(modelo)
visualizador.fit(x,y)
visualizador.poof()