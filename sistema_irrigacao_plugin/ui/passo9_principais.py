from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 9: Linha Mestra (Principais) e Fonte D'Água</h2>"
                     "<p>Conclua a arquitetura manual gráfica no QGIS desenhando de onde a bomba de sucção sai "
                     "e como suas linhas principais interligam todas as derivações validadas pelo passo anterior.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_concluir = QPushButton("Estou Pronto para Calcular Hidráulica (Avançar Fase)")
        btn_concluir.clicked.connect(self.on_concluir)
        layout.addWidget(btn_concluir)
        
        layout.addStretch()

    def on_concluir(self):
        QMessageBox.information(self, "Pre-flight Check", "A validade das linhas 'linha_principal.shp' e ponto da bomba 'fonte.shp' seria checada antes de liberar a matemática.")
        if self.projeto:
            self.projeto.passo_atual = 9
            self.projeto.salvar_projeto()
        
    def validar(self):
        return True
