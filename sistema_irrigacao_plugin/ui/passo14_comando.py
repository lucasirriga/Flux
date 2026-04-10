from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 14: Bloco de Comando e Linhas</h2>"
                     "<p>Demarque o local onde os solenoides ou quadros elétricos ficarão. O plugin traçará "
                     "linhas de cabo espelhadas às mestras até suas válvulas dos setores.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_comando = QPushButton("Posicionar Bloco de Comando no Mapa")
        btn_comando.clicked.connect(self.on_comando)
        layout.addWidget(btn_comando)
        
        layout.addStretch()

    def on_comando(self):
        QMessageBox.information(self, "Topologia Elétrica", "As 'linhas_comando.shp' seguem o pipe e são criadas baseadas pela válvula de distribuição central do Passo 5.")
        
    def validar(self):
        return True
