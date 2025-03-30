# Simulação de Monte Carlo para Preços de Ativos

Este projeto implementa uma simulação de Monte Carlo para prever possíveis trajetórias futuras do preço de um ativo (ex: ações), utilizando retornos logarítmicos. Também inclui análise de risco por meio da distribuição dos preços simulados e cálculo do Value at Risk (VaR).

---

## ⚙️ Funcionalidades

- Simulação de preços futuros com base em retorno lognormal
- Visualização de múltiplas trajetórias (caminhos simulados)
- Distribuição estatística dos preços ao final do horizonte de simulação
- Estimativa de risco via **Value at Risk (VaR)**

---

## Modelos Estatísticos Envolvidos

### 🔹 Retornos Lognormais 
Retornos logarítmicos são normalmente distribuídos.
    
- Preços seguem uma distribuição lognormal.
    
- Fórmula de simulação:
    
    St=S0⋅exp⁡[(μ−(σ^2/2))t+σ⋅Z] 
    
    onde Z ∼ N(0,1)

### 🔹 Simulação de Monte Carlo
- Gera **vários caminhos possíveis** para o preço com base na distribuição estatística dos retornos.
- Utiliza números aleatórios com distribuição normal (via `norm.ppf(np.random.rand())`).

### 🔹 Value at Risk (VaR)
- Estima a **perda máxima esperada** para um nível de confiança.    
- Simplesmente, usamos os percentis da distribuição de preços simulados:
    
    VaR95%=Patual − Ppercentil 5%
---

