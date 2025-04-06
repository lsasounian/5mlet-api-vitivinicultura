import json

def exportacao_abc(json_data):
    """
    Classifica países conforme curva ABC baseada no valor em US$.
    
    Args:
        json_data: Dados no formato JSON contendo uma lista de dicionários com:
                  - "Países"
                  - "Quantidade (Kg)"
                  - "Valor (US$)"
    
    Returns:
        Lista classificada com o campo adicional "classificação"
    """
    # Carrega os dados se for uma string JSON, senão assume que já é um dicionário
    if isinstance(json_data, str):
        try:
            dados = json.loads(json_data)
        except json.JSONDecodeError:
            raise ValueError("Formato JSON inválido")
    else:
        dados = json_data
    
    # Extrai a lista de dados se estiver em um dicionário com chave "dados"
    if isinstance(dados, dict) and "dados" in dados:
        dados = dados["dados"]
    elif not isinstance(dados, list):
        raise ValueError("Os dados devem ser uma lista ou dicionário com chave 'dados'")
    
    # Pré-processamento: converte valores e filtra registros válidos
    paises_processados = []
    for item in dados:
        if not isinstance(item, dict):
            continue
        
        pais = {
            "Países": item.get("Países", "Desconhecido"),
            "Quantidade (Kg)": item.get("Quantidade (Kg)", "-"),
            "Valor (US$)": item.get("Valor (US$)", "-")
        }
        
        # Converte valor para float quando possível
        valor_str = pais["Valor (US$)"]
        if valor_str != "-":
            try:
                # Remove pontos de milhar e converte vírgula decimal para ponto
                valor_float = float(valor_str.replace(".", "").replace(",", "."))
                pais["Valor_float"] = valor_float
                paises_processados.append(pais)
            except (ValueError, AttributeError):
                pass
    
    # Ordena por valor decrescente
    paises_ordenados = sorted(
        paises_processados,
        key=lambda x: x["Valor_float"],
        reverse=True
    )
    
    # Calcula totais para classificação ABC
    valor_total = sum(p["Valor_float"] for p in paises_ordenados)
    classificacao = []
    acumulado = 0.0
    
    # Classificação ABC
    for i, pais in enumerate(paises_ordenados):
        valor_pais = pais["Valor_float"]
        proporcao_acumulada = (acumulado + valor_pais) / valor_total
        
        # Regras de classificação
        if proporcao_acumulada <= 0.70 or i < 5:  # Classe A (top 5 ou 70%)
            classe = "A"
        elif proporcao_acumulada <= 0.95 or i < 20:  # Classe B (próximos 15 ou 25%)
            classe = "B"
        else:  # Classe C (restante)
            classe = "C"
        
        # Adiciona à classificação final
        classificacao.append({
            "Países": pais["Países"],
            "Quantidade (Kg)": pais["Quantidade (Kg)"],
            "Valor (US$)": pais["Valor (US$)"],
            "classificação": classe,
            "participação": f"{(valor_pais/valor_total)*100:.2f}%",
            "acumulado": f"{proporcao_acumulada*100:.2f}%"
        })
        
        acumulado += valor_pais
    
    # Adiciona países sem dados
    for item in dados:
        if isinstance(item, dict) and item.get("Valor (US$)", "-") == "-":
            classificacao.append({
                "Países": item.get("Países", "Desconhecido"),
                "Quantidade (Kg)": item.get("Quantidade (Kg)", "-"),
                "Valor (US$)": "-",
                "classificação": "Sem dados",
                "participação": "0%",
                "acumulado": "-"
            })
    
    return classificacao