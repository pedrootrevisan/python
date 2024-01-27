#amostragem simples
import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
base
base.shape
#mudança de seed
np.random.seed(250)
#150 amostras de 0 ou 1 com reposição, probabilidade equivalentes
amostra = np.random.choice(a=[0,1], size=150, replace=True, p =[0.7,0.3])
#verificar tamanho amostra
len(amostra)
len(amostra[amostra==1])
len(amostra[amostra==0])
base_final = base.loc(amostra==0)
base_final.shape()

base_final2 = base.loc(amostra==1)
base_final2.shape()