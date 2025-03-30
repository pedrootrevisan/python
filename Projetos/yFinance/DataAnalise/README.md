# Projeto de Análise Quantitativa de Dados Financeiros

## Visão Geral
Este projeto consiste em um sistema de análise quantitativa de dados financeiros, focado na análise de ações do mercado brasileiro. O projeto está estruturado em quatro notebooks principais que trabalham em conjunto para coletar, processar, analisar e visualizar dados financeiros.

## Estrutura do Projeto

### 1. Coleta de Dados (`coletaDados.ipynb`)
- **Objetivo**: Coleta dados históricos de preços de ações do mercado brasileiro
- **Funcionalidades**:
  - Utiliza a biblioteca `yfinance` para download de dados
  - Coleta dados de múltiplos ativos (15 ativos diferentes)
  - Período de análise: 2024
  - Dados coletados incluem:
    - Preço de fechamento
    - Preço máximo
    - Preço mínimo
    - Preço de abertura
    - Volume de negociação

### 2. Tratamento de Dados (`tratamento.ipynb`)
- **Objetivo**: Padronização e limpeza dos dados coletados
- **Funcionalidades**:
  - Padronização de nomes de colunas
  - Limpeza de dados nulos
  - Organização da estrutura dos dados
  - Geração de arquivos CSV limpos
  - Estrutura de diretórios:
    - `dados/brutos/`: Dados originais
    - `dados/limpos/`: Dados processados

### 3. Cálculo de Indicadores (`indicadores.ipynb`)
- **Objetivo**: Cálculo de indicadores técnicos
- **Indicadores Calculados**:
  - Diferença de preço
  - Retorno percentual
  - Ganhos e perdas
  - Médias móveis (5, 15, 30, 60 e 90 dias)
  - Médias de ganhos e perdas
- **Estrutura de Saída**:
  - Geração de arquivos CSV com indicadores
  - Armazenamento em `dados/indicadores/`

### 4. Visualização (`Graficos.ipynb`)
- **Objetivo**: Criação de visualizações dos dados e indicadores
- **Funcionalidades**:
  - Interface interativa para seleção de ativos
  - Visualização de múltiplos indicadores
  - Análise gráfica dos dados

## Fluxo de Dados
1. Coleta de dados brutos via `yfinance`
2. Tratamento e padronização dos dados
3. Cálculo de indicadores técnicos
4. Visualização e análise dos resultados

## Ativos Analisados
O projeto inclui análise de 15 ativos, incluindo:
- Índice Bovespa (^BVSP)
- Ações de grandes empresas brasileiras como:
  - Petrobras (PETR4)
  - Vale (VALE3)
  - Itaú (ITUB4)
  - Bradesco (BBDC4)
  - Ambev (ABEV3)
  - Entre outros

## Tecnologias Utilizadas
- Python
- Bibliotecas principais:
  - pandas: Manipulação de dados
  - numpy: Cálculos numéricos
  - yfinance: Coleta de dados financeiros
  - Jupyter Notebooks: Ambiente de desenvolvimento

## Estrutura de Arquivos
```
projeto/
├── dados/
│   ├── brutos/
│   ├── limpos/
│   └── indicadores/
├── coletaDados.ipynb
├── tratamento.ipynb
├── indicadores.ipynb
└── Graficos.ipynb
```

## Requisitos
Para executar o projeto, é necessário ter instalado:
- Python 3.x
- Jupyter Notebook
- Bibliotecas Python:
  - pandas
  - numpy
  - yfinance

`
## Uso
1. Execute os notebooks na seguinte ordem:
   - `coletaDados.ipynb`
   - `tratamento.ipynb`
   - `indicadores.ipynb`
   - `Graficos.ipynb`

2. Os dados serão processados automaticamente e salvos nas pastas correspondentes
3. Use o notebook `Graficos.ipynb` para visualizar e analisar os resultados
