from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 7: Ajuste de Derivações e Recorte Final</h2>"
                     "<p>Após mover as válvulas e as derivações para suas valas ideias usando o QGIS, clique abaixo "
                     "para atualizar e fatiar fisicamente as intersecções de tubulações na sua geometria atual.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_atualizar = QPushButton("Processar Intersecções e Recortes")
        btn_atualizar.clicked.connect(self.on_atualizar)
        layout.addWidget(btn_atualizar)
        
        layout.addStretch()

    def on_atualizar(self):
        QMessageBox.information(self, "Recorte Shapely", "O sistema recalculará usando divide nas intersecções das derivações mantendo os pipes menores no layer lateral!")
        
    def validar(self):
        return True
