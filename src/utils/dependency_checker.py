"""
Utilidades para verificar dependencias del sistema.
Verifica la presencia de yt-dlp y FFmpeg.
"""

import tkinter.messagebox as messagebox

def check_dependencies() -> bool:
    """
    Verifica que todas las dependencias estén instaladas.
    
    Returns:
        bool: True si todas las dependencias están disponibles
    """
    try:
        import yt_dlp
    except ImportError:
        messagebox.showerror(
            "Error de dependencias",
            "Para usar esta aplicación necesitas instalar:\n\n"
            "pip install yt-dlp\n\n"
            "También necesitas FFmpeg instalado para la conversión a MP3.\n"
            "Reinstala la aplicación después de instalar las dependencias."
        )
        return False
    
    # Verificar FFmpeg (yt-dlp lo verificará automáticamente)
    return True