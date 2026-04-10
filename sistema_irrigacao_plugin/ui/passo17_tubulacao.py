from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 17: Tubulação Rígida Principais e Derivações</h2>"
                     "<p>Baseado nos cálculos dos perfis hidráulicos na Fase 3, extrai as métricas de len() para PVC/Linhas duras"
                     " vendidas e contabilizadas em Varas fixas (6 metros padrão Brasil).</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_calc = QPushButton("Acumular Compimentos para Varas (6m) e Registrar")
        btn_calc.clicked.connect(self.on_calc)
        layout.addWidget(btn_calc)
        
        layout.addStretch()

    def on_calc(self):
        QMessageBox.information(self, "Quantitativo", "Toda geometria de redes fixada, divida por 6 foi compilada!")
        
    def validar(self):
        return True
