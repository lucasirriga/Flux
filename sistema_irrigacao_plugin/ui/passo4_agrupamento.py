from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passos 4 e 5: Malha de Agrupamento de Setores</h2>"
                     "<p>Utiliza a quantidade de emissores dividida pela quantidade de setores teóricos (ex. 1/10) "
                     "para gerar polígonos que facilitam o dissolve manual de setores na cena.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_gerar = QPushButton("Gerar Rede 1/10 de Agrupamento")
        btn_gerar.clicked.connect(self.on_gerar)
        layout.addWidget(btn_gerar)
        
        btn_val_dissolve = QPushButton("Validar Setores após Agrupamento (Dissolve Manual QGIS)")
        btn_val_dissolve.clicked.connect(self.on_validar)
        layout.addWidget(btn_val_dissolve)
        
        layout.addStretch()
        
    def on_gerar(self):
        QMessageBox.information(self, "Zonas 1/10", "A Malha de Grade regular para auxílio ao usuário será gerada aqui.")
        
    def on_validar(self):
        QMessageBox.information(self, "Sucesso", "O sistema irá verificar a variação (em %) da quantidade de pontos dentro de cada setor desenhado. Em caso de discrepância as válvulas não ficariam balanceadas e um alerta será soado.")
        
    def validar(self):
        return True
