"""
Servicio para interactuar con YouTube y descargar contenido.
Maneja toda la lógica de descarga usando yt-dlp.
"""

import yt_dlp
import os
import re
from typing import Dict, Any, Optional, Callable
from src.models.download_config import DownloadConfig

class YouTubeService:
    """Servicio para manejar operaciones relacionadas con YouTube."""
    
    def __init__(self):
        self.youtube_patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+',
            r'(?:https?://)?(?:www\.)?youtu\.be/[\w-]+',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+',
            r'(?:https?://)?(?:www\.)?youtube\.com/v/[\w-]+',
            r'(?:https?://)?(?:www\.)?youtube\.com/playlist\?list=[\w-]+',
        ]
    
    def is_valid_youtube_url(self, url: str) -> bool:
        """
        Valida si la URL es de YouTube.
        
        Args:
            url (str): URL a validar
            
        Returns:
            bool: True si es una URL válida de YouTube
        """
        return any(re.match(pattern, url) for pattern in self.youtube_patterns)
    
    def is_playlist_url(self, url: str) -> bool:
        """
        Verifica si la URL es de una playlist.
        
        Args:
            url (str): URL a verificar
            
        Returns:
            bool: True si es una URL de playlist
        """
        return 'playlist' in url or 'list=' in url
    
    def clean_youtube_url(self, url: str) -> str:
        """
        Limpia la URL para descargar solo el video específico.
        
        Args:
            url (str): URL original
            
        Returns:
            str: URL limpia
        """
        if not url:
            return url
            
        if 'youtube.com/watch' in url and 'v=' in url:
            video_id_match = re.search(r'v=([^&]+)', url)
            if video_id_match:
                video_id = video_id_match.group(1)
                return f"https://www.youtube.com/watch?v={video_id}"
        
        if 'youtu.be/' in url:
            video_id_match = re.search(r'youtu\.be/([^?&]+)', url)
            if video_id_match:
                video_id = video_id_match.group(1)
                return f"https://www.youtube.com/watch?v={video_id}"
        
        return url
    
    def get_video_info(self, url: str) -> Dict[str, Any]:
        """
        Obtiene información del video o playlist.
        
        Args:
            url (str): URL del video/playlist
            
        Returns:
            Dict[str, Any]: Información del contenido
            
        Raises:
            Exception: Si hay error al obtener información
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
    
    def download_audio(self, config: DownloadConfig, progress_callback: Optional[Callable] = None) -> str:
        """
        Descarga el audio del video o playlist.
        
        Args:
            config (DownloadConfig): Configuración de descarga
            progress_callback (Callable, optional): Función para reportar progreso
            
        Returns:
            str: Mensaje de éxito
            
        Raises:
            Exception: Si hay error durante la descarga
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(config.download_path, '%(title)s.%(ext)s'),
            'ignoreerrors': False,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': config.audio_format,
                'preferredquality': config.audio_quality,
            }],
            'postprocessor_args': [
                '-ar', '44100',
            ],
            'prefer_ffmpeg': True,
        }
        
        if config.is_playlist:
            ydl_opts['noplaylist'] = False
            download_url = config.url
        else:
            ydl_opts['noplaylist'] = True
            download_url = self.clean_youtube_url(config.url)
        
        if progress_callback:
            ydl_opts['progress_hooks'] = [progress_callback]
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Obtener información primero
            info = ydl.extract_info(download_url, download=False)
            
            # Determinar mensaje de éxito
            if config.is_playlist:
                title = info.get('title', 'Playlist')
                count = len(info.get('entries', []))
                success_msg = f"Se han descargado {count} audios de la playlist '{title}'"
            else:
                title = info.get('title', 'Audio')
                success_msg = f"El audio '{title}' se ha descargado"
            
            # Realizar descarga
            ydl.download([download_url])
            
            return success_msg