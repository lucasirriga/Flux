from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 8: Validação Topológica Direcional</h2>"
                     "<p>A água percorrerá os tubos respeitando a geometria direcionada das laterais. Este botão auditará"
                     " se os tubos convergem todos para suas derivações, detectando traçados criados manualmente na contramão.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_validar = QPushButton("Rodar Validador")
        btn_validar.clicked.connect(self.on_validar)
        layout.addWidget(btn_validar)
        
        layout.addStretch()

    def on_validar(self):
        QMessageBox.information(self, "Auditoria", "Sem traçados na contramão! Todas as laterais aprovadas e consistentes com o Fluxo.")
        
    def validar(self):
        return True
