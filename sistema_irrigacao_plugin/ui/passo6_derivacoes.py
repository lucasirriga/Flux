from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 6: Derivações e Laterais</h2>"
                     "<p>Sinta-se livre para acoplar suas linhas de platilhas base e as válvulas.</p>"
                     "<p>O processo irá gerar as linhas de derivação de forma perpendicular às linhas mestras da plantação.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        btn_gerar = QPushButton("Gerar Linhas de Derivação e Recortar Laterais")
        btn_gerar.clicked.connect(self.on_gerar)
        layout.addWidget(btn_gerar)
        
        layout.addStretch()

    def on_gerar(self):
        QMessageBox.information(self, "Geoprocessamento", "Serão processados e salvos: 'derivacoes.shp' e 'laterais.shp'")
        
    def validar(self):
        return True
