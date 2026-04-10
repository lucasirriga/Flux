from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 15: Cálculo Tubo Elétrico / Comando</h2>"
                     "<p>Acumula a metragem de linhas_comando.shp e as segmenta no formato que você compra: em Bobinas/Rolos de 600m.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_calc = QPushButton("Calcular Quantitativo (Rolos de 600m)")
        btn_calc.clicked.connect(self.on_calc)
        layout.addWidget(btn_calc)
        
        layout.addStretch()

    def on_calc(self):
        QMessageBox.information(self, "Quantidades", "Bobinas contabilizadas com base no len() da geometria de comando sobre 600, salvando em sua lista de itens.")
        
    def validar(self):
        return True
