from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, QDoubleSpinBox
from PyQt5.QtCore import Qt

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("<h2>Passo 18: Orçamento Final (Resumo Cotação)</h2>"
                     "<p>O projeto compila os itens dos passos 13 a 17, acopla Valores Base para emitir "
                     "o prospecto em um layout PDF ou HTML para o seu cliente.</p>")
        lbl.setWordWrap(True)
        layout.addWidget(lbl)
        
        l_h = QHBoxLayout()
        l_h.addWidget(QLabel("Valor do Serviço Humano R$: "))
        self.spn_servico = QDoubleSpinBox()
        self.spn_servico.setRange(0, 9999999)
        self.spn_servico.setValue(5000)
        l_h.addWidget(self.spn_servico)
        layout.addLayout(l_h)
        
        btn_pdf = QPushButton("Gerar Relatório Resumo da Fazenda")
        btn_pdf.clicked.connect(self.on_pdf)
        layout.addWidget(btn_pdf)
        
        layout.addStretch()

    def on_pdf(self):
        try:
            from ..relatorios.gerador_relatorios import GeradorRelatorios
            rel = GeradorRelatorios(self.projeto)
            rel.gerar_orcamento_final(self.spn_servico.value())
            QMessageBox.information(self, "PDF", "O sistema finalizou o Pipeline e seu sumario estaria no root de sua pasta ou em /relatorios!")
        except Exception as e:
            QMessageBox.critical(self, "PDF Generator Erro", "Ao gerar: " + str(e))
        
    def validar(self):
        return True
