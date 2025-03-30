# Análise de Localização de Lojas

Este projeto realiza a análise e visualização de dados de localização de lojas, utilizando Python para processamento de dados e geração de mapas de calor (heatmaps).

## 📋 Descrição

O projeto consiste em uma análise de dados de localização de lojas, incluindo:
- Processamento de dados de planilhas Excel
- Geração de mapas de calor para visualização de distribuição de lojas
- Integração com APIs do Google para geocodificação

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Google Maps API
- Folium (para geração de heatmaps)
- Jupyter Notebook

## 📁 Estrutura do Projeto

```
.
├── googleE.ipynb              # Notebook principal com o código
├── heatmap_Youcom.html        # Mapa de calor gerado para Youcom
├── heatmap_renner.html        # Mapa de calor gerado para Renner
├── Planilhas e Fundamentos .xlsx  # Dados fonte

```

## 📊 Funcionalidades

### Processamento de Dados
- Leitura de dados de planilhas Excel
- Processamento de informações de localização
- Geocodificação de endereços

### Visualização
- Geração de mapas de calor para diferentes redes de lojas
- Visualização interativa da distribuição geográfica
- Análise de concentração de lojas por região

## 📝 Como Usar

1. Abra o arquivo `googleE.ipynb` no Jupyter Notebook
2. Execute as células em sequência
3. Os mapas de calor serão gerados automaticamente

## 📈 Resultados

O projeto gera dois tipos principais de visualizações:
- Heatmap com a localização das lojas da rede Youcom
- Heatmap com a localização das lojas da rede Renner
- Dessa forma podemos observar a destribuição das lojas de cada rede,avaliando assim a estrategia de crescimento de  cada uma, publico alvo e etc

