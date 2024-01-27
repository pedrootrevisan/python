#distribuição binomial eventos de mesma probabilidade, independentes de resultado "0 ou 1"

from scipy.stats import binom
#jogar moeda 5 vezes, qual a probabilidade de dar cara 3vezes?
prob = binom.pmf(3,5,0.5)
print(prob)

#passar por 4 sinais verdes 1,2,3,4 vezes
binom.pmf(4,4,0.25)
#concurso com 12 questoes, qual a prob de acertar 7
#cada questão tem 4  alternativa
binom.pmf(7,12,0.25)
#prob de acertar as 12
binom.pmf(12,12,0.25)