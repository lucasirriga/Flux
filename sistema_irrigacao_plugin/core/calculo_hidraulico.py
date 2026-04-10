# core/calculo_hidraulico.py
import math
from .constants import COEFICIENTES_HW, DIAM_COMERCIAIS_MM

def calcular_perda_carga_hazen_williams(vazao_m3h: float, diametro_m: float, comprimento_m: float, coeficiente_c: float) -> float:
    """
    Calcula perda de carga (hf) em MCA usando a fórmula de Hazen-Williams.
    hf = 10.643 × Q^1.852 / (C^1.852 × D^4.87) × L
    """
    if vazao_m3h <= 0 or diametro_m <= 0 or coeficiente_c <= 0:
        return 0.0

    Q = vazao_m3h
    C = coeficiente_c
    D = diametro_m
    L = comprimento_m
    
    hf = 10.643 * (Q ** 1.852) / ((C ** 1.852) * (D ** 4.87)) * L
    return hf

def calcular_velocidade(vazao_m3h: float, diametro_m: float) -> float:
    """
    Retorna velocidade do fluxo (v = Q / (3.6 × A)) -> v = Q / (3.6 * D^2 * pi / 4).
    Aproximação: Q / (2.827 * D^2).
    Usaremos a forma Q / (3.6 * D^2) informada no prompt pra padronizar.
    """
    if diametro_m <= 0: return 0.0
    return vazao_m3h / (3.6 * (diametro_m ** 2))

def selecionar_diametro_comercial(vazao_m3h: float, comprimento_m: float, coeficiente_c: float, pressao_servico_mca: float, perda_maxima_pct: float = 10.0) -> dict:
    perda_limite = pressao_servico_mca * (perda_maxima_pct / 100.0)
    
    for dn_mm in sorted(DIAM_COMERCIAIS_MM):
        dn_m = dn_mm / 1000.0
        
        hf = calcular_perda_carga_hazen_williams(vazao_m3h, dn_m, comprimento_m, coeficiente_c)
        vel = calcular_velocidade(vazao_m3h, dn_m)
        
        # Conhecimentos padrão sugerem:
        # Menor diámetro que passe a velocidade segura (e.g. 0.5 a 2.0) e não quebre a perda de carga
        if 0.5 <= vel <= 2.0 and hf <= perda_limite:
            di_mm = dn_mm - 3  # Simplificado conforme especificação
            return {
                'dn_mm': dn_mm,
                'di_mm': di_mm,
                'hf_mca': hf,
                'velocidade_ms': vel,
                'valido': True
            }
            
    dn_final = DIAM_COMERCIAIS_MM[-1]
    return {
        'dn_mm': dn_final,
        'di_mm': dn_final - 3,
        'hf_mca': calcular_perda_carga_hazen_williams(vazao_m3h, dn_final/1000.0, comprimento_m, coeficiente_c),
        'velocidade_ms': calcular_velocidade(vazao_m3h, dn_final/1000.0),
        'valido': False,
        'aviso': 'Nenhum DN atende os critérios. Usado o maior diâmetro disponível do catálogo.'
    }
