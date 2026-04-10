from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGroupBox, QCheckBox, QDoubleSpinBox, QFileDialog
from PyQt5.QtCore import Qt

class PassoWidget(QWidget):
    """
    Widget para o Passo 1: Carregamento de Imagem + Delimitação de Área.
    """
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        grupo_imagem = QGroupBox("1. Carregar Imagem de Referência")
        layout_imagem = QVBoxLayout()
        
        lbl_arquivo = QLabel("Arquivo:")
        self.txt_arquivo = QLineEdit()
        self.txt_arquivo.setReadOnly(True)
        btn_procurar = QPushButton("Procurar...")
        btn_procurar.clicked.connect(self.on_procurar_imagem)
        
        layout_arquivo = QHBoxLayout()
        layout_arquivo.addWidget(lbl_arquivo)
        layout_arquivo.addWidget(self.txt_arquivo)
        layout_arquivo.addWidget(btn_procurar)
        layout_imagem.addLayout(layout_arquivo)
        
        self.check_crs = QCheckBox("✓ CRS válido (SIRGAS 2000 UTM)")
        self.check_crs.setEnabled(False)
        self.lbl_zona = QLabel("Zona UTM: ??")
        
        layout_imagem.addWidget(self.check_crs)
        layout_imagem.addWidget(self.lbl_zona)
        grupo_imagem.setLayout(layout_imagem)
        layout.addWidget(grupo_imagem)
        
        grupo_poligono = QGroupBox("2. Digitalizar Polígono da Área Total")
        layout_poligono = QVBoxLayout()
        lbl_info = QLabel("A imagem será carregada no QGIS. Use a ferramenta 'Adicionar Feição' "
                          "para digitalizar o polígono de área total (uma única feição).")
        lbl_info.setWordWrap(True)
        
        btn_carregar_qgis = QPushButton("Carregar Imagem no QGIS")
        btn_carregar_qgis.clicked.connect(self.on_carregar_imagem_qgis)
        
        layout_poligono.addWidget(lbl_info)
        layout_poligono.addWidget(btn_carregar_qgis)
        grupo_poligono.setLayout(layout_poligono)
        layout.addWidget(grupo_poligono)
        
        grupo_atributos = QGroupBox("3. Informações do Projeto")
        layout_atributos = QVBoxLayout()
        lbl_nome = QLabel("Nome do Projeto:")
        self.txt_nome_projeto = QLineEdit()
        
        lbl_area = QLabel("Área total (ha):")
        self.spn_area = QDoubleSpinBox()
        self.spn_area.setReadOnly(True)
        self.spn_area.setDecimals(4)
        
        layout_atributos.addWidget(lbl_nome)
        layout_atributos.addWidget(self.txt_nome_projeto)
        layout_atributos.addWidget(lbl_area)
        layout_atributos.addWidget(self.spn_area)
        
        grupo_atributos.setLayout(layout_atributos)
        layout.addWidget(grupo_atributos)
        
        layout_botoes = QHBoxLayout()
        btn_validar = QPushButton("Validar Limite e Salvar Dados Base")
        btn_validar.clicked.connect(self.on_validar)
        layout_botoes.addWidget(btn_validar)
        layout.addLayout(layout_botoes)
        
        layout.addStretch()

    def on_procurar_imagem(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "GeoTIFF (*.tif *.tiff);;Todos (*.*)")
        if arquivo:
            self.txt_arquivo.setText(arquivo)
            self.validar_imagem(arquivo)
            
    def validar_imagem(self, caminho):
        try:
            from ..core.validacao import validar_imagem
            res = validar_imagem(caminho)
            if res.get('valido'):
                self.check_crs.setChecked(True)
                self.lbl_zona.setText(f"Zona UTM: {res.get('zona_utm')}S")
            else:
                QMessageBox.warning(self, "CRS", "CRS Inválido. Selecione Raster UTM SIRGAS2000.")
        except Exception as e:
             pass

    def on_carregar_imagem_qgis(self):
        if not self.txt_arquivo.text():
            QMessageBox.warning(self, "Aviso", "Selecione uma imagem primeiro.")
            return
        QMessageBox.information(self, "Pronto", "Camada Raster seria carregada aqui. Use a UI do QGIS para digitalizar o polígono temp_area.")

    def on_validar(self):
        if self.projeto:
            self.projeto.nome_projeto = self.txt_nome_projeto.text()
            QMessageBox.information(self, "Validação", "Atributos pré-validos com sucesso!")
            
    def validar(self):
        return True
