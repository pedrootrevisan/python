# Assistente Virtual com Groq API

Este projeto implementa um assistente virtual utilizando a API do Groq, que permite interações com um modelo de linguagem avançado (LLM) para responder perguntas e fornecer informações em diferentes contextos.

## Funcionalidades

- Integração com a API Groq
- Sistema de contexto para respostas personalizadas
- Interface interativa para perguntas e respostas
- Suporte a diferentes domínios de conhecimento

## Configuração

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave da API Groq:
     ```
     GROQ_API_KEY=sua_chave_aqui
     ```

## Uso

O projeto está organizado em notebooks Jupyter que demonstram diferentes usos da API Groq, incluindo:
- Respostas básicas
- Assistente especializado (ex: assistente de investimentos)
- Sistema de contexto para respostas mais precisas

## Estrutura do Projeto

```
.
├── src/                    # Código fonte
├── .env                    # Variáveis de ambiente
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
``` 