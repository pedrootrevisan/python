# Análise de Solo - Ferramenta de Cálculo de Adubação e Correção

## 📝 Descrição
Este é um projeto, modelo, que visa auxiliar profissionais da área agrícola no cálculo de recomendações de adubação e correção de solo. A ferramenta desenvolvida para simplificar os cálculos complexos envolvidos na análise de solo, fornecendo recomendações baseadas em parâmetros básicos do solo.



## 🛠️ Funcionalidades
- Cálculo de necessidade de calagem
- Cálculo de necessidade de gessagem
- Recomendação de adubação de formação
- Recomendação de adubação de cobertura
- Recomendação de adubação foliar com micronutrientes
- Ajustes baseados na textura do solo
- Recomendações específicas por região

## 📋 Pré-requisitos
- Python 3.x
- Não são necessárias bibliotecas externas

## 🔧 Instalação
1. Clone este repositório
2. Navegue até a pasta do projeto
3. Execute o arquivo `solo_analisys.py`

## 💻 Como Usar
1. Execute o programa
2. Escolha a opção 1 para inserir dados e gerar recomendações
3. Siga as instruções na tela para inserir os parâmetros do solo
4. Receba as recomendações detalhadas


## 📚 Documentação das Funções
### Funções Principais
- `calcular_calagem()`: Calcula a necessidade de calcário
- `calcular_gessagem()`: Calcula a necessidade de gesso
- `calcular_adubacao_formacao()`: Calcula recomendações de adubação de formação
- `calcular_adubacao_cobertura()`: Calcula recomendações de adubação de cobertura
- `calcular_adubacao_foliar()`: Calcula recomendações de micronutrientes

### Funções Auxiliares
- `input_float()`: Validação de entrada numérica
- `input_int()`: Validação de entrada inteira
- `escolher_regiao()`: Seleção de recomendações por região
- `ajustar_adubacao_por_textura()`: Ajuste de doses por textura do solo

## Observações
- As recomendações são baseadas em modelos simplificados
- Consulte manuais oficiais da sua região para ajustes finais
- O projeto está em constante desenvolvimento e pode receber atualizações
- Atente-se para as unidades de medida de cada calculo, caso necessario realize conversão prévia

