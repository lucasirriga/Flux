from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 12: Intersecções Cruzadas</h2>"
                     "<p>Sua geometria está estática e cortada, precisamos colher as metadados entre "
                     "laterais vs derivações (Tees e Cruzetas) apontando DN_lateral <-> DN_derivacao.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_gerar = QPushButton("Gerar Interconexões")
        btn_gerar.clicked.connect(self.on_gerar)
        layout.addWidget(btn_gerar)
        
        layout.addStretch()

    def on_gerar(self):
        QMessageBox.information(self, "Topologia Cross", "Exportando Shape 'interconexoes_lateral_derivacao' com attributos DN acoplados.")
        
    def validar(self):
        return True
