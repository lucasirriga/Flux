import os
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
import inspect

class SistemaIrrigacaoPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(inspect.getfile(self.__class__))

    def initGui(self):
        icon_path = os.path.join(self.plugin_dir, 'icons', 'plugin_icon.png')
        self.action = QAction(QIcon(icon_path), 'Sistema de Irrigação', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        
        # Add to Menu and Toolbar
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu('&Sistema de Irrigação', self.action)

    def unload(self):
        self.iface.removePluginMenu('&Sistema de Irrigação', self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        from .ui.main_dialog import MainDialog
        self.dialog = MainDialog(self.iface)
        self.dialog.show()
