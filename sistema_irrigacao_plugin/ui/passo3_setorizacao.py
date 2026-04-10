from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QSpinBox, QPushButton, QMessageBox, QGroupBox, QGridLayout
from PyQt5.QtCore import Qt

class PassoWidget(QWidget):
    def __init__(self, projeto):
        super().__init__()
        self.projeto = projeto
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        grupo_params = QGroupBox("Parâmetros de Operação")
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Vazão por Emissor (m³/h):"), 0, 0)
        self.spn_vazao = QDoubleSpinBox()
        self.spn_vazao.setValue(0.5)
        self.spn_vazao.setDecimals(3)
        grid.addWidget(self.spn_vazao, 0, 1)
        
        grid.addWidget(QLabel("Tempo por Setor (horas):"), 1, 0)
        self.spn_tempo = QDoubleSpinBox()
        self.spn_tempo.setValue(4.0)
        grid.addWidget(self.spn_tempo, 1, 1)
        
        grid.addWidget(QLabel("Tempo Disp. Diário (h):"), 2, 0)
        self.spn_diario = QDoubleSpinBox()
        self.spn_diario.setValue(16.0)
        grid.addWidget(self.spn_diario, 2, 1)
        
        grid.addWidget(QLabel("Setores operando simultâneamente:"), 3, 0)
        self.spn_simultaneo = QSpinBox()
        self.spn_simultaneo.setValue(1)
        self.spn_simultaneo.setMinimum(1)
        grid.addWidget(self.spn_simultaneo, 3, 1)
        
        grupo_params.setLayout(grid)
        layout.addWidget(grupo_params)
        
        self.lbl_resultados = QLabel("Setores mínimos necessários: --\nVazão de Projeto Necessária Estimada: --")
        layout.addWidget(self.lbl_resultados)
        
        btn_calc = QPushButton("Calcular Equilíbrio")
        btn_calc.clicked.connect(self.on_calcular)
        layout.addWidget(btn_calc)
        
        layout.addStretch()

    def on_calcular(self):
        tempo_setor = self.spn_tempo.value()
        tempo_diario = self.spn_diario.value()
        vazao_emissor = self.spn_vazao.value()
        simultan = self.spn_simultaneo.value()
        
        if tempo_setor <= 0: return
        turnos = tempo_diario / tempo_setor
        setores = turnos * simultan
        
        self.lbl_resultados.setText(f"Setores Atendíveis (Max): {int(setores)}\n"
                                    f"Turnos por dia: {turnos:.1f}")
        if self.projeto:
            self.projeto.definir_parametros_passo(4, {
                'vazao_emissor': vazao_emissor,
                'tempo_setor': tempo_setor,
                'setores': int(setores)
            })

    def validar(self):
        return True
