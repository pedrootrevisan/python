#Distribuição de Poisson
#mede a probabilidade da ocorrência de eventos e intervalo de tempo, ao inves de numeros de experimentos,
# eventos na poisson estão associados a intervalos de tempo, porem eventos são independentes

from scipy.stats import poisson

#média de acidentes de carrosé 2 por dia
#qual a probabilidade de ocorrer 3 em um dia?

poisson.pmf(3,2)         #calc probabilidade pontua
poisson.cdf(3,2)         #calc probabilidade de 3 ou menos acidentes/ inclui 3 acidentes
poisson.sf(3,2)          #probabilidade de ocorrer mais de x acidentes
