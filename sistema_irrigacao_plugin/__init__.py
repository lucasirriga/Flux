def classFactory(iface):
    from .sistema_irrigacao import SistemaIrrigacaoPlugin
    return SistemaIrrigacaoPlugin(iface)
