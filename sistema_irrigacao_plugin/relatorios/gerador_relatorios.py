class GeradorRelatorios:
    def __init__(self, projeto):
        self.projeto = projeto

    def gerar_orcamento_final(self, servico: float):
        # Aqui seriam agregados os materiais de projeto.shapefiles / projeto.parametros
        # renderizados usando WeasyPrint ou outra api se estivermos num sub OS do QGIS puro
        print(f"Mock Log: Gerando o Orçamento final agregando Servicos: {servico}")
        return True
