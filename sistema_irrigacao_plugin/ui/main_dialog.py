from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QStackedWidget, QSplitter, QPushButton, QMessageBox, QWidget, QLabel
from PyQt5.QtCore import Qt

class MainDialog(QDialog):
    def __init__(self, iface, parent=None):
        super().__init__(parent)
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.projeto = None # Placeholder para instanciação via interface ou open project
        
        self.setWindowTitle('Sistema de Dimensionamento de Irrigação')
        self.resize(800, 600)
        
        self.setup_ui()
        self.conectar_sinais()
        
    def setup_ui(self):
        layout_principal = QVBoxLayout(self)
        
        # Painel central splitter
        splitter = QSplitter(Qt.Horizontal)
        
        self.tree_passos = QTreeWidget()
        self.tree_passos.setHeaderHidden(True)
        self._criar_arvore_passos()
        
        self.stack_passos = QStackedWidget()
        
        # Carrega passos dinamicamente ou placeholder para os não implementados
        for i in range(1, 19):
            widget_passo = self._criar_widget_passo(i)
            self.stack_passos.addWidget(widget_passo)
            
        splitter.addWidget(self.tree_passos)
        splitter.addWidget(self.stack_passos)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 3)
        layout_principal.addWidget(splitter)
        
        # Botoes na barra inferior
        layout_inferior = QHBoxLayout()
        self.btn_voltar = QPushButton("Voltar")
        self.btn_salvar = QPushButton("Salvar Projeto")
        self.btn_proximo = QPushButton("Próximo")
        
        layout_inferior.addWidget(self.btn_voltar)
        layout_inferior.addStretch()
        layout_inferior.addWidget(self.btn_salvar)
        layout_inferior.addWidget(self.btn_proximo)
        
        layout_principal.addLayout(layout_inferior)
        
    def _criar_arvore_passos(self):
        passos = [
            ("1", "Imagem + Área"),
            ("2A", "Malha de Plantio"),
            ("2B", "Malha de Irrigação"),
            ("3", "Setorização Prévia"),
            ("4", "Malha de Agrupamento"),
            ("5", "Setores + Válvulas"),
            ("6", "Derivações + Laterais"),
            ("7", "Ajuste + Recorte"),
            ("8", "Validação de Laterais"),
            ("9", "Principais + Fonte"),
            ("10", "Cálculo de Diâmetros"),
            ("11", "Pontos de Redução"),
            ("12", "Pontos Interconexão"),
            ("13", "Especif. de Peças"),
            ("14", "Bloco de Comando"),
            ("15", "Tubo de Comando"),
            ("16", "Emissores"),
            ("17", "Tubulação"),
            ("18", "Orçamento Final")
        ]
        
        for numero, descricao in passos:
            item = QTreeWidgetItem([f"[{numero}] {descricao}"])
            item.setData(0, Qt.UserRole, numero)
            self.tree_passos.addTopLevelItem(item)
            
    def _criar_widget_passo(self, numero: int) -> QWidget:
        nome_modulos = {
            1: "passo1_imagem",
            2: "passo2a_plantio",
            3: "passo2b_irrigacao", 
            4: "passo3_setorizacao",
            # Ajuste de numerção: No UI loop os indices da árvore são os step ID, mas 2A, 2B contam como items.
            # O mapeamento do array passos será alinhado pelo array e Index.
        }
        
        # Mapeamento do numero visual com base no arvore
        passos = ["1", "2A", "2B", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]
        passo_code = passos[numero - 1]
        mod_name = passo_code.replace("A", "a").replace("B", "b").lower()
        if "a" in mod_name or "b" in mod_name:
            if "2a" in mod_name: arquivo = "passo2a_plantio"
            if "2b" in mod_name: arquivo = "passo2b_irrigacao"
        else:
            n_val = int(passo_code)
            arquivo = f"passo{n_val}" # Ex. "passo3" ... para lidar de forma generica depois. Dependerá da nossa nomeclatura

        try:
            modulo = __import__(f'sistema_irrigacao_plugin.ui.{arquivo}', fromlist=['PassoWidget'])
            return modulo.PassoWidget(self.projeto)
        except ImportError:
            w = QWidget()
            l = QVBoxLayout(w)
            l.addWidget(QLabel(f"<h2>Passo {passo_code}</h2><p>Pendente de implementação (Fase de Mock).</p>"))
            l.addStretch()
            return w
        
    def conectar_sinais(self):
        self.tree_passos.itemClicked.connect(self.on_passo_selecionado)
        self.btn_proximo.clicked.connect(self.on_proximo_passo)
        self.btn_voltar.clicked.connect(self.on_voltar_passo)
        self.btn_salvar.clicked.connect(self.on_salvar_projeto)
        
    def on_passo_selecionado(self, item: QTreeWidgetItem, column: int):
        numero_str = item.data(0, Qt.UserRole)
        # 2A e 2B serao mapeados numericamente conforme index, temporario:
        idx = self.tree_passos.indexOfTopLevelItem(item)
        self.stack_passos.setCurrentIndex(idx)
        
    def on_proximo_passo(self):
        idx = self.stack_passos.currentIndex()
        if idx < self.stack_passos.count() - 1:
            self.stack_passos.setCurrentIndex(idx + 1)
            item = self.tree_passos.topLevelItem(idx + 1)
            self.tree_passos.setCurrentItem(item)
            
    def on_voltar_passo(self):
        idx = self.stack_passos.currentIndex()
        if idx > 0:
            self.stack_passos.setCurrentIndex(idx - 1)
            item = self.tree_passos.topLevelItem(idx - 1)
            self.tree_passos.setCurrentItem(item)
            
    def on_salvar_projeto(self):
        if self.projeto:
            self.projeto.salvar_projeto()
            QMessageBox.information(self, "Sucesso", "Projeto salvo.")
        else:
             QMessageBox.warning(self, "Aviso", "Nenhum projeto aberto.")
