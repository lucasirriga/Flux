import os
import json

class Projeto:
    def __init__(self, diretorio_projeto: str, nome_projeto: str):
        self.diretorio_projeto = diretorio_projeto
        self.nome_projeto = nome_projeto
        self.passo_atual = 1
        self.metadata = {}
        self.shapefiles = {}
        self.parametros = {}
        self.relatorios = {}
        
        self.dir_shapefiles = os.path.join(diretorio_projeto, "shapefiles")
        self.dir_relatorios = os.path.join(diretorio_projeto, "relatorios")
        self.dir_temp = os.path.join(diretorio_projeto, ".temp")
        self.arquivo_metadata = os.path.join(diretorio_projeto, "metadata.json")
        
        self._criar_estrutura_diretorios()
    
    def _criar_estrutura_diretorios(self):
        os.makedirs(self.dir_shapefiles, exist_ok=True)
        os.makedirs(self.dir_relatorios, exist_ok=True)
        os.makedirs(self.dir_temp, exist_ok=True)
    
    def salvar_projeto(self):
        data = {
            "nome_projeto": self.nome_projeto,
            "passo_atual": self.passo_atual,
            "metadata": self.metadata,
            "parametros": self.parametros
        }
        with open(self.arquivo_metadata, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
    def carregar_projeto(self):
        if os.path.exists(self.arquivo_metadata):
            with open(self.arquivo_metadata, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.nome_projeto = data.get("nome_projeto", self.nome_projeto)
                self.passo_atual = data.get("passo_atual", 1)
                self.metadata = data.get("metadata", {})
                self.parametros = data.get("parametros", {})
                
    def adicionar_shapefile(self, nome: str, gdf, tipo: str = 'output'):
        self.shapefiles[nome] = {'gdf': gdf, 'tipo': tipo}
        
    def obter_shapefile(self, nome: str):
        return self.shapefiles.get(nome, {}).get('gdf', None)
        
    def definir_parametros_passo(self, passo: int, parametros: dict):
        self.parametros[str(passo)] = parametros
        
    def obter_parametros_passo(self, passo: int) -> dict:
        return self.parametros.get(str(passo), {})
        
    def validar_passo_anterior(self, passo: int) -> bool:
        return True # Mock: Implement proper validation later
        
    def ir_proximo_passo(self):
        self.passo_atual += 1
        self.salvar_projeto()
        
    def ir_passo_anterior(self):
        if self.passo_atual > 1:
            self.passo_atual -= 1
            self.salvar_projeto()
