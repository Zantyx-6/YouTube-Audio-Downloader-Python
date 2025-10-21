#!/usr/bin/env python3
"""
Punto de entrada principal de la aplicación.
Inicia la interfaz gráfica del Descargador de Audio de YouTube.
"""

import tkinter as tk
from src.gui.app import YouTubeDownloaderApp
from src.utils.dependency_checker import check_dependencies

def main():
    """Función principal que inicia la aplicación."""
    # Verificar dependencias antes de iniciar
    if not check_dependencies():
        return
    
    # Crear ventana principal
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    
    # Iniciar loop principal
    root.mainloop()

if __name__ == "__main__":
    main()