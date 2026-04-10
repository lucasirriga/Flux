from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QPushButton, QMessageBox, QGroupBox, QComboBox, QCheckBox
from PyQt5.QtCore import Qt

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        grupo_mat = QGroupBox("Metodologia de Dimensionamento por Linha")
        l_mat = QVBoxLayout()
        
        l_fixo = QHBoxLayout()
        self.chk_mangueira_fixa = QCheckBox("Forçar diâmetro nas Laterais (Sem Hazen-W)")
        self.cb_dn_fixo = QComboBox()
        from ..core.constants import DIAM_COMERCIAIS_MM
        self.cb_dn_fixo.addItems([str(d) for d in DIAM_COMERCIAIS_MM])
        self.cb_dn_fixo.setEnabled(False)
        self.chk_mangueira_fixa.toggled.connect(self.cb_dn_fixo.setEnabled)
        
        l_fixo.addWidget(self.chk_mangueira_fixa)
        l_fixo.addWidget(self.cb_dn_fixo)
        l_mat.addLayout(l_fixo)
        
        # Parametros base Derivações/Principais
        l_hazen = QHBoxLayout()
        l_hazen.addWidget(QLabel("Material HW (C):"))
        self.cb_mat = QComboBox()
        self.cb_mat.addItems(['PVC', 'PEAD', 'Ferro', 'Cimento', 'Galvanizado'])
        l_hazen.addWidget(self.cb_mat)
        
        l_hazen.addWidget(QLabel("Pressão de Serviço e Limite (%):"))
        self.spn_pressao = QDoubleSpinBox()
        self.spn_pressao.setValue(35.0) # MCA
        self.spn_pressao.setSuffix(" mca")
        self.spn_limite = QDoubleSpinBox()
        self.spn_limite.setValue(10.0)
        self.spn_limite.setSuffix(" %")
        l_hazen.addWidget(self.spn_pressao)
        l_hazen.addWidget(self.spn_limite)
        
        l_mat.addLayout(l_hazen)
        grupo_mat.setLayout(l_mat)
        layout.addWidget(grupo_mat)
        
        btn_calc = QPushButton("Calcular Vazões Acumuladas e Diâmetros Ideais")
        btn_calc.clicked.connect(self.on_calcular)
        layout.addWidget(btn_calc)
        
        layout.addStretch()

    def on_calcular(self):
        try:
            from ..core.calculo_hidraulico import selecionar_diametro_comercial, COEFICIENTES_HW
            q_teste = 25.5
            mat = self.cb_mat.currentText()
            coef = COEFICIENTES_HW.get(mat, 150)
            res = selecionar_diametro_comercial(q_teste, 100.0, coef, self.spn_pressao.value(), self.spn_limite.value())
            QMessageBox.information(self, "Auditoria Hidráulica", "Cálculos rodariam no background! Exemplo pra fluxo 25m3/h numa dist de 100m gerou DN " + str(res.get('dn_mm')) + " e Velocidade : " + str(res.get('velocidade_ms')))
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))
            
    def validar(self):
        return True
