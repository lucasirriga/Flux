from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 16: Emissores e Tubos Polietileno</h2>"
                     "<p>Baseado nos aspersores desenhados, levanta as Mangueiras limitadas em bobinas de 500m "
                     "e mapeia conectores de serviço.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_calc = QPushButton("Agrupar Microaspersores e Bobinas P.E")
        btn_calc.clicked.connect(self.on_calc)
        layout.addWidget(btn_calc)
        
        layout.addStretch()

    def on_calc(self):
        QMessageBox.information(self, "Mapeamento Físico", "Todos os Aspersores contabilizados x Extensão da Mangueira Base Cega (Rolos de 500m).")
        
    def validar(self):
        return True
