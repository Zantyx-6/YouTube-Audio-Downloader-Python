"""
Modelo de configuración para descargas.
Define la estructura de datos para la configuración de descargas.
"""

from dataclasses import dataclass
from pathlib import Path

@dataclass
class DownloadConfig:
    """
    Configuración para la descarga de audio.
    
    Attributes:
        url (str): URL del video o playlist de YouTube
        download_path (str): Ruta donde guardar los archivos
        is_playlist (bool): True si es playlist, False si es video individual
        audio_format (str): Formato de audio (mp3 por defecto)
        audio_quality (str): Calidad del audio (192k por defecto)
    """
    url: str = ""
    download_path: str = str(Path.home() / "Downloads")
    is_playlist: bool = False
    audio_format: str = "mp3"
    audio_quality: str = "192"