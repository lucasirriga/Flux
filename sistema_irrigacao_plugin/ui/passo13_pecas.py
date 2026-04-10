from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 13: Especificação de Peças Físicas</h2>"
                     "<p>Baseado nos layers de redução e interconexão, selecione as peças catálogo do mercado que casam com a tubulação.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        self.table = QTableWidget(2, 3)
        self.table.setHorizontalHeaderLabels(['Tipo Transição', 'Dimensoes (DN A -> B)', 'Sua Peça Física'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.table.setItem(0, 0, QTableWidgetItem("Redução Derivação"))
        self.table.setItem(0, 1, QTableWidgetItem("75mm -> 50mm"))
        self.table.setItem(0, 2, QTableWidgetItem("Bucha Redução Curta PVC 75x50"))
        
        self.table.setItem(1, 0, QTableWidgetItem("Interconexão Lat/Der"))
        self.table.setItem(1, 1, QTableWidgetItem("50mm -> 32mm"))
        self.table.setItem(1, 2, QTableWidgetItem("Colar de Tomada + Adaptador (32mm)"))
        
        layout.addWidget(self.table)
        
        btn_save = QPushButton("Validar Lista de Peças Transicionais")
        btn_save.clicked.connect(self.on_save)
        layout.addWidget(btn_save)

    def on_save(self):
        QMessageBox.information(self, "Tabela", "Especificações mapeadas para a futura lista do orçamento.")
        
    def validar(self):
        return True
