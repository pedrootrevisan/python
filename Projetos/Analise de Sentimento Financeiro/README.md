# Análise de Sentimento Financeiro

Este projeto realiza análise de sentimento em textos financeiros utilizando técnicas de Processamento de Linguagem Natural (NLP). O objetivo é classificar textos financeiros em três categorias: positivo, negativo e neutro, utilizando diferentes métodos de análise de sentimento.nForam implementados dois métodos principais de análise de sentimento: Naive Bayes e TextBlob.

## Objetivo

- Classificar textos financeiros em três categorias de sentimento
- Comparar o desempenho entre diferentes métodos de análise de sentimento
- Fornecer insights sobre o sentimento em textos financeiros

## Dados

- **Fonte**: Arquivo CSV (`data.csv`)
- **Tamanho**: 5.842 amostras
- **Estrutura**:
  - Coluna "texto": contém os textos financeiros
  - Coluna "sentimento": classificação do sentimento (positivo, negativo, neutro)

## Processamento dos Dados

### 1. Pré-processamento
- Carregamento dos dados usando pandas
- Renomeação das colunas para "texto" e "sentimento"
- Análise exploratória dos dados
- Visualização da distribuição dos sentimentos

### 2. Codificação dos Rótulos
- Utilização do LabelEncoder para converter as classes de sentimento em valores numéricos:
  - 2 = positivo
  - 1 = neutro
  - 0 = negativo

### 3. Divisão dos Dados
- Separação em conjuntos de treino e teste
- Proporção: 80% treino, 20% teste
- Vetorização do texto usando Bag of Words (CountVectorizer)

## Métodos de Análise

### 1. Naive Bayes
O Naive Bayes é um algoritmo de classificação probabilístico baseado no teorema de Bayes.

**Princípios**:
- Assume independência entre as palavras (hipótese "naive")
- Calcula a probabilidade de cada classe dado o texto
- Classifica o texto na classe com maior probabilidade

**Vantagens**:
- Simples e eficiente
- Funciona bem com dados textuais
- Requer menos dados de treinamento

**Desvantagens**:
- Assume independência entre palavras
- Pode não capturar bem o contexto

### 2. TextBlob
O TextBlob é uma biblioteca Python para processamento de linguagem natural.

**Funcionamento**:
- Analisa a polaridade do texto (-1 a 1)
- Considera palavras positivas e negativas
- Calcula a subjetividade do texto

**Classificação**:
- Polaridade > 0: Sentimento positivo
- Polaridade = 0: Sentimento neutro
- Polaridade < 0: Sentimento negativo

## Resultados

### Comparação de Desempenho
- **Naive Bayes**: 71% de acurácia
- **TextBlob**: 44% de acurácia

### Métricas Detalhadas (Naive Bayes)
```
              precision    recall  f1-score   support
           0       0.45      0.31      0.37       175
           1       0.74      0.86      0.79       622
           2       0.74      0.65      0.70       372
```

## Conclusão

O modelo Naive Bayes apresentou melhor desempenho na classificação dos sentimentos, com uma acurácia de 71%. O TextBlob, embora mais simples de implementar, teve um desempenho inferior (44% de acurácia). Isso sugere que para este conjunto específico de dados financeiros, o modelo treinado (Naive Bayes) é mais eficaz que a análise de sentimento baseada em regras (TextBlob).

## Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- TextBlob
- Matplotlib
- Seaborn

## Requisitos

Para executar o projeto, são necessárias as seguintes bibliotecas:

```python
numpy
pandas
seaborn
matplotlib
scikit-learn
textblob
```

