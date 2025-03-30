
"""
Autor: Pedro Trevisan
"""

# =============================================================================
# 1. CRIAÇÃO DE FUNÇÕES DE CÁLCULO
# =============================================================================

def calcular_calagem(V_atual: float, V_desejado: float, CTC: float, PRNT: float) -> float:
    """
    Cálculo simplificado da necessidade de calcário (NC) com base na saturação por bases.
    Fórmula genérica (inspirada na 5ª Aproximação - MG):
    NC (t/ha) = [CTC * (V_desejado - V_atual) / 100] * (100 / PRNT)
    """
    if V_atual >= V_desejado:
        return 0.0
    necessidade_calcario = (CTC * (V_desejado - V_atual) / 100) * (100 / PRNT)
    return necessidade_calcario

def calcular_gessagem(Al_subsuperficie: float, Ca_subsuperficie: float) -> float:
    """
    Cálculo simplificado da necessidade de gesso.
    Se Al_subsuperficie > 0.5 e Ca_subsuperficie < 0.5 => 1 t/ha (valor simbólico).
    """
    if Al_subsuperficie > 0.5 and Ca_subsuperficie < 0.5:
        return 1.0
    else:
        return 0.0

def calcular_adubacao_formacao(P: float, K: float) -> dict:
    """
    Cálculo simplificado da adubação de formação (antes ou no plantio),
    com foco em fósforo (P2O5) e potássio (K2O), seguindo faixas didáticas.
    """
    # Fósforo
    if P < 10:
        p2o5 = 80
    elif 10 <= P < 20:
        p2o5 = 60
    else:
        p2o5 = 40
    
    # Potássio
    if K < 0.2:
        k2o = 60
    elif 0.2 <= K < 0.4:
        k2o = 40
    else:
        k2o = 20
    
    return {
        "P2O5_kg_ha": p2o5,
        "K2O_kg_ha": k2o
    }

def calcular_adubacao_cobertura(N_recomendado: float, K_recomendado: float, parcelas: int = 1) -> dict:
    """
    Cálculo simplificado da adubação de cobertura.
    'parcelas' indica em quantas aplicações (parcelas) será dividido.
    Retorna o total e o valor por parcela.
    """
    if parcelas < 1:
        parcelas = 1  # evitar divisão por zero
    
    n_por_parcela = N_recomendado / parcelas
    k_por_parcela = K_recomendado / parcelas
    
    return {
        "N_total_kg_ha": N_recomendado,
        "K2O_total_kg_ha": K_recomendado,
        "parcelas": parcelas,
        "N_por_parcela": n_por_parcela,
        "K2O_por_parcela": k_por_parcela
    }

def calcular_adubacao_foliar(lista_micronutrientes: list) -> dict:
    """
    Cálculo simplificado da adubação foliar.
    Cada micronutriente tem uma dose padrão simbólica (ex.: B=0.5 kg/ha, Zn=1.0 kg/ha, etc.)
    """
    # Doses fictícias de exemplo (por aplicação):
    doses_padrao = {
        "B": 0.3,   # kg/ha (via ácido bórico, por exemplo)
        "Zn": 1.0,  # kg/ha (via sulfato de zinco)
        "Fe": 2.0,  # kg/ha (via quelato ou sulfato)
        "Mn": 1.0,
        "Cu": 0.5,
        "Mo": 0.1
        # etc.
    }
    recomendacoes = {}
    
    for nutriente in lista_micronutrientes:
        nutriente_up = nutriente.strip().capitalize()  # Padroniza, e.g. 'zn' -> 'Zn'
        if nutriente_up in doses_padrao:
            recomendacoes[nutriente_up] = doses_padrao[nutriente_up]
        else:
            recomendacoes[nutriente_up] = 0.0  # Se não está no dicionário, retorna 0.0
    
    return recomendacoes


# =============================================================================
# 2. FUNÇÕES AUXILIARES (VALIDAÇÃO E INTERFACE)
# =============================================================================

def input_float(mensagem: str, permitir_zero_neg=False) -> float:
    """
    Lê uma string do usuário, substitui vírgula por ponto, e converte para float.
    Se permitir_zero_neg=False, não permite valores negativos (e zero) retornando erro.
    """
    while True:
        entrada = input(mensagem).replace(',', '.')
        try:
            valor = float(entrada)
            if not permitir_zero_neg and valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite um número válido, usando '.' ou ','. Tente novamente.")


def input_int(mensagem: str, minimo=1, maximo=None) -> int:
    """
    Lê um inteiro do usuário, validando a faixa [minimo, maximo].
    Se maximo=None, não há limite superior.
    """
    while True:
        entrada = input(mensagem)
        try:
            valor = int(entrada)
            if valor < minimo:
                print(f"O valor deve ser maior ou igual a {minimo}.")
                continue
            if maximo and valor > maximo:
                print(f"O valor deve ser menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def escolher_regiao() -> dict:
    """
    Permite selecionar recomendações de regiões fictícias (ex.: MG ou SP) para saturação por bases,
    ou retorna valores padrão se a região não for reconhecida.
    """
    regioes = {
        "MG": {
            "nome": "Minas Gerais",
            # Exemplo: meta de saturação por bases = 50%
            "V_desejado": 50.0
        },
        "SP": {
            "nome": "São Paulo",
            # Exemplo: meta de saturação por bases = 60%
            "V_desejado": 60.0
        }
    }
    
    print("\nEscolha a região para seguir recomendações padrões (ex.: MG ou SP).")
    regiao_escolhida = input("Digite a sigla da região (MG/SP) ou pressione Enter para padrão (MG): ").strip().upper()
    
    if regiao_escolhida not in regioes:
        print("Região não reconhecida. Usando MG como padrão.\n")
        regiao_escolhida = "MG"
    
    return regioes[regiao_escolhida]


def ajustar_adubacao_por_textura(adub_form: dict, textura_solo: str) -> dict:
    """
    Ajusta as doses de adubação de formação de acordo com a textura do solo (muito simplificado).
    Exemplo fictício:
      - Solos arenosos: +10% de P2O5 e K2O
      - Solos argilosos: -10% de P2O5 e K2O
      - Franco: mantém igual
    """
    fator = 1.0
    if textura_solo == "arenoso":
        fator = 1.1
    elif textura_solo == "argiloso":
        fator = 0.9
    
    ajustado = {
        "P2O5_kg_ha": adub_form["P2O5_kg_ha"] * fator,
        "K2O_kg_ha": adub_form["K2O_kg_ha"] * fator
    }
    return ajustado


# =============================================================================
# 3. FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    print("="*60)
    print("Bem-vindo ao Programa Simplificado de Cálculo de Adubação e Correção de Solo".center(60))
    print("="*60)
    
    while True:
        print("\n[1] Inserir dados e gerar recomendações")
        print("[2] Sair")
        
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            print("\n Vamos comecar")
            regiao_info = escolher_regiao()
            V_desejado_regiao = regiao_info["V_desejado"]
            
            
            print("\n--- Insira os parâmetros básicos do solo ---")
            pH = input_float("pH do solo (0-14): ", permitir_zero_neg=True)
            V_atual = input_float("Saturação por bases atual (V_atual) [%]: ", permitir_zero_neg=True)
            CTC = input_float("Capacidade de troca de cátions (CTC) [cmolc/dm³]: ", permitir_zero_neg=True)
            PRNT = input_float("PRNT do calcário (%): ", permitir_zero_neg=True)
            
            # Subsuperfície
            Al_sub = input_float("Teor de Al³⁺ em subsuperfície (cmolc/dm³): ", permitir_zero_neg=True)
            Ca_sub = input_float("Teor de Ca²⁺ em subsuperfície (cmolc/dm³): ", permitir_zero_neg=True)
            
            # Macronutrientes
            P = input_float("Teor de Fósforo (P) [mg/dm³]: ", permitir_zero_neg=True)
            K = input_float("Teor de Potássio (K) [cmolc/dm³]: ", permitir_zero_neg=True)
            
            # Matéria orgânica (não usamos diretamente, mas coletamos)
            MO = input_float("Teor de Matéria Orgânica (MO) [%]: ", permitir_zero_neg=True)
            
            # Textura
            print("\nEscolha a textura do solo (influencia na dose de adubos):")
            print(" [1] Arenoso")
            print(" [2] Franco")
            print(" [3] Argiloso")
            opc_textura = input_int("Opção: ", 1, 3)
            if opc_textura == 1:
                textura_solo = "arenoso"
            elif opc_textura == 2:
                textura_solo = "franco"
            else:
                textura_solo = "argiloso"
            
            # Adubação de Cobertura
            print("\n--- Adubação de Cobertura ---")
            N_cobertura = input_float("Recomendação total de Nitrogênio (N) em cobertura (kg/ha): ", permitir_zero_neg=True)
            K_cobertura = input_float("Recomendação adicional de Potássio (K2O) em cobertura (kg/ha): ", permitir_zero_neg=True)
            parcelas_cobertura = input_int("Dividir a adubação de cobertura em quantas parcelas? (1-3): ", 1, 3)
            
            # Micronutrientes
            print("\n--- Micronutrientes ---")
            print("Caso haja deficiência, informe os elementos separados por vírgula (ex.: Zn, B, Fe)")
            print("Possíveis: B, Zn, Fe, Mn, Cu, Mo (padrão). Deixe vazio se não houver deficiência.")
            lista_def = input("Deficiências detectadas: ").strip()
            if lista_def:
                # Transformar em lista
                lista_micro = [x.strip() for x in lista_def.split(",")]
            else:
                lista_micro = []
            
            # ------------------------------
            # CÁLCULOS
            # ------------------------------
            
            # 1) Calagem
            # Se o usuário quiser usar a recomendação padrão da região, vamos substituí-la se V_desejado < V_atual
            # ou se preferir manter fixo, poderia perguntar. Aqui vamos usar a da região por padrão:
            V_desejado = V_desejado_regiao
            
            calcario = calcular_calagem(V_atual, V_desejado, CTC, PRNT)
            
            # 2) Gessagem
            gesso = calcular_gessagem(Al_sub, Ca_sub)
            
            # 3) Adubação de Formação
            adub_form = calcular_adubacao_formacao(P, K)
            # Ajuste pela textura
            adub_form_ajustado = ajustar_adubacao_por_textura(adub_form, textura_solo)
            
            # 4) Adubação de Cobertura
            adub_cob = calcular_adubacao_cobertura(N_cobertura, K_cobertura, parcelas_cobertura)
            
            # 5) Adubação Foliar (micronutrientes)
            adub_foliar = calcular_adubacao_foliar(lista_micro)
            
            # ------------------------------
            # RESULTADOS
            # ------------------------------
            print("\n" + "="*60)
            print("RESULTADOS DE RECOMENDAÇÃO".center(60))
            print("="*60)
            
            # -- Exibir dados básicos para referência
            print(f"\nRegião escolhida: {regiao_info['nome']}")
            print(f"pH do solo: {pH:.2f}")
            print(f"Saturação por bases atual: {V_atual:.2f}% / Desejada: {V_desejado:.2f}%")
            
            # Calagem e Gesso
            print("\n1) Correção de Solo:")
            print(f"   • Necessidade de calcário (t/ha): {calcario:.2f}")
            print(f"   • Necessidade de gesso (t/ha): {gesso:.2f}")
            
            # Adubação de Formação
            print("\n2) Adubação de Formação (antes ou no plantio):")
            print(f"   • P2O5: {adub_form_ajustado['P2O5_kg_ha']:.1f} kg/ha (após ajuste por textura)")
            print(f"   • K2O: {adub_form_ajustado['K2O_kg_ha']:.1f} kg/ha (após ajuste por textura)")
            
            # Adubação de Cobertura
            print("\n3) Adubação de Cobertura:")
            print(f"   • N total: {adub_cob['N_total_kg_ha']:.1f} kg/ha")
            print(f"     -> Em {adub_cob['parcelas']} parcelas de {adub_cob['N_por_parcela']:.1f} kg/ha cada")
            print(f"   • K2O total: {adub_cob['K2O_total_kg_ha']:.1f} kg/ha")
            print(f"     -> Em {adub_cob['parcelas']} parcelas de {adub_cob['K2O_por_parcela']:.1f} kg/ha cada")
            
            # Micronutrientes
            print("\n4) Adubação Foliar (Micronutrientes):")
            if len(adub_foliar) == 0:
                print("   • Sem deficiência aparente, sem recomendação especial de micronutrientes.")
            else:
                for mn, dose in adub_foliar.items():
                    if dose > 0:
                        print(f"   • {mn}: {dose} kg/ha (aplicação foliar)")
                    else:
                        print(f"   • {mn}: não padronizado ou não reconhecido.")
            
            print("\nObs.: Ajuste valores de acordo com manuais oficiais da região escolhida.")
            print("="*60)
            
        elif opcao == "2":
            print("\nSaindo do programa. Até logo, Vitor!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
