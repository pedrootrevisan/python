import pandas as pd
import seaborn as sb
import statistics as est

#importar dados
dataset=pd.read_csv("X", sep=";")
#visualizar
dataset.head()
#tamanho
dataset.shape
#Problema inicial é dar nome as colunas
dataset.columns = ["Id","Score","genero","idade","estado","Salario"]
#esplorar dados categoricos
#estado
agrupado = dataset.groupby(['estado']).size()
agrupado
agrupado.plot.bar(color = 'gray')
#explorar colunas numericas
#Score
dataset['Score'].describe()
sb.boxplot(dataset['Score']).set_title('Score')
sb.distplot(dataset['Score']).set_title('Score')
#idade
dataset['idade'].describe()
sb.boxplot(dataset['idade']).set_title('idade')
sb.distplot(dataset['idade']).set_title('idade')
#contar casos NAN
dataset.isnull().sum()
#Salarios
#remover nas e substituir por mediana
dataset['Salario'].describe()
mediana= est.median(dataset['salario'])
mediana
#substituir
dataset['Salario'].fillna(mediana,inplace=True)
dataset['Salario'].isnull().sum()
#Tratar Genero
agrupado = dataset.groupby(['Genero']).size()
agrupado
dataset.loc[dataset['Genero']== 'M', 'Genero'] ="Masculino"
dataset.loc[dataset['Genero'].isin(['fem','F']), 'Genero'] ="Feminino"
agrupado = dataset.groupby(['Genero']).size()
agrupado




