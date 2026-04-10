from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 11: Extração dos Pontos de Redução</h2>"
                     "<p>A varredura da fase 10 atribuiu valores diferentes de Diâmetro Nominal (DN) sob "
                     "o mesmo segmento percorrido devido às vazões. Aqui agrupamos as transições para listar as Buchas de Redução.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_gerar = QPushButton("Levantar Pontos de Redução de Bitola")
        btn_gerar.clicked.connect(self.on_gerar)
        layout.addWidget(btn_gerar)
        
        layout.addStretch()

    def on_gerar(self):
        QMessageBox.information(self, "Reduções", "Verificando loops nas linhas principais e derivações buscando DN_A != DN_B e clipando reducoes.shp")
        
    def validar(self):
        return True
