#Distruibuição T student, usada com caracteristicas especificas como pequenas amostras
from scipy.stats import t
#exemplo media de salarios é 75 reais/h, Amostra com 9 funcionarios e Desvio padrão = 10
#probabilidade de um funcionario receeber menos de 80
t.cdf(1.5,8) #1.5 tabelado com 8 graus de liberdade ( 9 - 1), cdf a esquerda da distribuição
#probabilidade de um funcionario receeber maior de 80
t.sf(1.5,8)

x = t.cdf(1.5,8) + t.sf(1.5,8)


