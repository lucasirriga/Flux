from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QDoubleSpinBox, QPushButton, QMessageBox, QGroupBox
from PyQt5.QtCore import Qt

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        grupo_malha = QGroupBox("Configurações da Malha de Plantio")
        layout_malha = QVBoxLayout()
        
        # Orientação
        layout_ori = QHBoxLayout()
        lbl_ori = QLabel("Orientação:")
        self.cb_orientacao = QComboBox()
        self.cb_orientacao.addItems(["Leste-Oeste (Padrão)", "Norte-Sul", "Customizada (Graus)"])
        layout_ori.addWidget(lbl_ori)
        layout_ori.addWidget(self.cb_orientacao)
        layout_malha.addLayout(layout_ori)
        
        # Espaçamento
        layout_esp = QHBoxLayout()
        lbl_tipo = QLabel("Padrão de Plantio:")
        self.cb_padrao = QComboBox()
        self.cb_padrao.addItems(["Retangular", "Triângulo Equilátero", "Triângulo Não-Equilátero"])
        layout_esp.addWidget(lbl_tipo)
        layout_esp.addWidget(self.cb_padrao)
        layout_malha.addLayout(layout_esp)
        
        # Medidas
        layout_med = QHBoxLayout()
        lbl_p_linha = QLabel("Espaço Pontos(m):")
        self.spn_pontos = QDoubleSpinBox()
        self.spn_pontos.setValue(3.0)
        
        lbl_p_entr = QLabel("Espaço Linhas(m):")
        self.spn_linhas = QDoubleSpinBox()
        self.spn_linhas.setValue(5.0)
        
        layout_med.addWidget(lbl_p_linha)
        layout_med.addWidget(self.spn_pontos)
        layout_med.addSpacing(10)
        layout_med.addWidget(lbl_p_entr)
        layout_med.addWidget(self.spn_linhas)
        layout_malha.addLayout(layout_med)
        
        grupo_malha.setLayout(layout_malha)
        layout.addWidget(grupo_malha)
        
        # Botoes Requisitação a Geoprocessing
        btn_gerar = QPushButton("Gerar Malha na Área e Adicionar na Cena")
        btn_gerar.clicked.connect(self.on_gerar_malha)
        layout.addWidget(btn_gerar)
        
        layout.addStretch()

    def on_gerar_malha(self):
        try:
            from ..core.geoprocessing import gerar_malha_plantio_retangular
            # Exemplo de mock para gerar pontos sem estressar QGIS enquanto o GeoPandas n processa:
            QMessageBox.information(self, "Geoprocessamento", "A malha de plantio seria gerada usando Geopandas / Shapely e apresentada no Canvas...")
            if self.projeto:
                # Store parametros
                self.projeto.definir_parametros_passo(2, {
                    'padrao': self.cb_padrao.currentText(),
                    'esp_pontos': self.spn_pontos.value(),
                    'esp_linhas': self.spn_linhas.value()
                })
        except Exception as e:
            QMessageBox.critical(self, "Erro Execução", str(e))
    
    def validar(self):
        return True
