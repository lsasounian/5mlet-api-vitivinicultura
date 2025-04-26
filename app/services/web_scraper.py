from bs4 import BeautifulSoup
from fastapi import HTTPException
import requests
import re

def scrape_table(url_pagina, ano=None, subopcao=None, categoria_filtro=None):
    if ano is not None:
        if int(ano) < 1970 or (
            url_pagina not in ["opt_05", "opt_06"] and int(ano) > 2023
        ) or (
            url_pagina in ["opt_05", "opt_06"] and int(ano) > 2024
        ):
            raise HTTPException(status_code=400, detail="Ano fora do intervalo permitido")

    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={url_pagina}"
    if subopcao:
        url += f"&subopcao={subopcao}"
    if ano:
        url += f"&ano={ano}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    subopcao_label = None
    if url_pagina in ["opt_03", "opt_05", "opt_06"]:
        buttons = soup.find_all("button", class_="btn_sopt")
        subopcoes_disponiveis = {btn.get("value"): btn.get_text(strip=True) for btn in buttons if btn.get("type") == "submit"}
        if subopcao:
            if subopcao not in subopcoes_disponiveis:
                raise HTTPException(status_code=400, detail="Subopcao inválida para esta página")
            subopcao_label = subopcoes_disponiveis[subopcao]

    header_text = soup.find("p", class_="text_center")
    header_content = header_text.get_text(strip=True) if header_text else None

    ano_extraido = None
    if header_content:
        match = re.search(r"\[(\d{4})\]", header_content)
        if match:
            ano_extraido = match.group(1)
            header_content = re.sub(r"\s*\[\d{4}\]\s*", "", header_content)

    if url_pagina in ["opt_05", "opt_06"]:
        tables = soup.find_all("table", class_="tb_base tb_dados")
    else:
        # FILTRA: pega só tabelas que têm th
        tables = [table for table in soup.find_all("table") if table.find("th")]

    site_data = []
    current_category = None
    grouped_data = {}
    category_totals = {}
    current_headers = []

    for table in tables:
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        if headers:
            current_headers = headers
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if not cells:
                continue

            td_class = cells[0].get("class", [])

            if "tb_item" in td_class:
                current_category = cells[0].get_text(strip=True)
                try:
                    total_str = cells[1].get_text(strip=True)
                    total_label = current_headers[1] if len(current_headers) > 1 else "total"
                    total = int(total_str.replace(".", "").replace(",", ""))
                except:
                    total = 0
                    total_label = "total"
                if current_category not in grouped_data:
                    grouped_data[current_category] = []
                    category_totals[current_category] = {"label": total_label, "value": total}
                continue

            if len(cells) == len(current_headers):
                values = [cell.get_text(strip=True) for cell in cells]
                item = dict(zip(current_headers, values))
                if current_category:
                    item["categoria"] = current_category
                    if categoria_filtro is None or item.get("categoria") == categoria_filtro:
                        grouped_data[current_category].append(item)
                else:
                    if categoria_filtro is None:
                        site_data.append(item)

    if grouped_data:
        site_data = []
        for cat, dados in grouped_data.items():
            total_info = category_totals.get(cat, {"label": "total", "value": 0})
            site_data.append({
                "categoria": cat,
                total_info["label"]: total_info["value"],
                "dados": dados
            })

    return {
        "header": header_content,
        "ano": ano_extraido,
        "subopcao": subopcao_label,
        "dados": site_data
    }