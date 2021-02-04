class tags:
    __version__ = "1.1.2"
    __author__ = "Kreusada"
    __contributors__ = ["Kreusada",]

    def version_info():
        return __version__

    def author_info():
        return __author__

    def contributors():
        return __contributors__

    def kreusada_info():
        return [__version__, __author__, sorted(__contributors__)]