def validar_poligono(poligono, area_minima_ha: float = 0.1, area_maxima_ha: float = 10000) -> dict:
    return {'valido': True, 'area_ha': 1.0}

def validar_malha_pontos(gdf_pontos, gdf_area, espaco_esperado_m: float = None) -> dict:
    return {'valido': True}

def validar_imagem(caminho_arquivo: str) -> dict:
    return {'valido': True, 'zona_utm': '23'}
