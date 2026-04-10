from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QPushButton, QMessageBox, QGroupBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        grupo_origem = QGroupBox("Base da Malha")
        layout_origem = QVBoxLayout()
        
        self.bg_origem = QButtonGroup()
        self.rb_assumir = QRadioButton("Assumir malha de plantio existente")
        self.rb_criar = QRadioButton("Criar nova malha exclusiva")
        self.rb_assumir.setChecked(True)
        
        self.bg_origem.addButton(self.rb_assumir, 1)
        self.bg_origem.addButton(self.rb_criar, 2)
        
        layout_origem.addWidget(self.rb_assumir)
        layout_origem.addWidget(self.rb_criar)
        grupo_origem.setLayout(layout_origem)
        layout.addWidget(grupo_origem)
        
        grupo_emissor = QGroupBox("Configuração do Emissor (Aspersor)")
        layout_emissor = QHBoxLayout()
        
        lbl_raio = QLabel("Raio de Alcance (m):")
        self.spn_raio = QDoubleSpinBox()
        self.spn_raio.setValue(12.0)
        self.spn_raio.setRange(0.5, 100.0)
        
        layout_emissor.addWidget(lbl_raio)
        layout_emissor.addWidget(self.spn_raio)
        
        grupo_emissor.setLayout(layout_emissor)
        layout.addWidget(grupo_emissor)
        
        btn_gerar = QPushButton("Gerar Zonas de Irrigação (Buffers)")
        btn_gerar.clicked.connect(self.on_gerar_zonas)
        layout.addWidget(btn_gerar)
        
        layout.addStretch()

    def on_gerar_zonas(self):
        try:
            from ..core.geoprocessing import criar_zonas_irrigacao_buffer
            QMessageBox.information(self, "Geoprocessamento", f"Gerando buffers de raio {self.spn_raio.value()}m para cada ponto...")
            if self.projeto:
                self.projeto.definir_parametros_passo(3, {
                    'raio_emissor': self.spn_raio.value()
                })
        except Exception as e:
            QMessageBox.critical(self, "Erro Execução", str(e))
            
    def validar(self):
        return True
