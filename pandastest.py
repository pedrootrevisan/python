import pandas as pd

dados = pd.read_csv("Credit.csv")
dados.shape

# resumo estatistico das colunas
dados.describe()
dados.head()
dados.tail(2)

#filtro por nome da coluna
dados[["duration"]]
#filtrar linhas por indice
dados[1:3]
#linhas 1 e 3
dados[[1,3]]

#filtro
dados.loc[dados['porpuse'] == "radio/tv"]
#outro filtro
resultados = dados.loc[dados['credit_amount'] > 10000]
print(resultados)

#definimos somente algumas colunas
credito3 = dados[['checking_status','duration']].loc[dados['credit_amount'] > 10000]
#Series, unica coluna
#pode ser criada a partiir de listas e arrays do numpy ou colunas de data frame
s1 = pd.Series([1,2,3,416,2,33])
print(s1)
#por dataframe
s2 = dados['porpouse']
#excluir coluna
dados.drop('checking_status',axis=1,inplace=True)
#verificar dados nulos
dados.isnull()
dados.isnull().sum()
#retirar colunas com Nan
dados.dropna()