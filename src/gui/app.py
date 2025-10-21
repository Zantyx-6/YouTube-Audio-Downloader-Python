"""
Aplicación principal de la interfaz gráfica.
Coordina todos los componentes y maneja la lógica de la aplicación.
"""

import tkinter as tk
from tkinter import messagebox
import threading
from src.gui.components.url_frame import URLFrame
from src.gui.components.path_frame import PathFrame
from src.gui.components.info_frame import InfoFrame
from src.gui.components.progress_frame import ProgressFrame
from src.services.youtube_service import YouTubeService
from src.models.download_config import DownloadConfig

class YouTubeDownloaderApp:
    """Aplicación principal del Descargador de Audio de YouTube."""
    
    def __init__(self, root: tk.Tk):
        """
        Inicializa la aplicación.
        
        Args:
            root (tk.Tk): Ventana principal
        """
        self.root = root
        self.root.title("Descargador de Audio YouTube - MP3")
        self.root.geometry("600x700")
        self.root.configure(bg="#2c3e50")
        
        # Servicios
        self.youtube_service = YouTubeService()
        
        # Configuración actual
        self.current_config = DownloadConfig()
        
        # Inicializar UI
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz de usuario."""
        # Título principal
        self.setup_title()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#34495e", padx=30, pady=30)
        main_frame.pack(expand=True, fill="both", padx=20, pady=10)
        
        # Componentes
        self.setup_components(main_frame)
        
        # Botones de descarga
        self.setup_download_buttons(main_frame)
    
    def setup_title(self):
        """Configura el título de la aplicación."""
        title_frame = tk.Frame(self.root, bg="#2c3e50")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🎵 Descargador de Audio YouTube (MP3)",
            font=("Arial", 20, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50"
        )
        title_label.pack()
    
    def setup_components(self, parent: tk.Widget):
        """Configura los componentes principales."""
        # Frame de URL
        self.url_frame = URLFrame(parent, self.on_url_change)
        self.url_frame.pack(fill="x", pady=(0, 20))
        
        # Frame de ruta
        self.path_frame = PathFrame(parent, self.on_path_change)
        self.path_frame.pack(fill="x", pady=(0, 20))
        
        # Frame de información
        self.info_frame = InfoFrame(parent)
        self.info_frame.pack(fill="x", pady=(0, 20))
        
        # Botón de información
        info_btn = tk.Button(
            parent,
            text="ℹ️ Obtener información",
            command=self.get_video_info,
            font=("Arial", 11, "bold"),
            bg="#f39c12",
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        info_btn.pack(pady=(0, 10))
        
        # Frame de progreso
        self.progress_frame = ProgressFrame(parent)
        self.progress_frame.pack(fill="x", pady=(0, 20))
    
    def setup_download_buttons(self, parent: tk.Widget):
        """Configura los botones de descarga."""
        buttons_frame = tk.Frame(parent, bg="#34495e")
        buttons_frame.pack(pady=20)
        
        single_btn = tk.Button(
            buttons_frame,
            text="🎵 Descargar Solo Esta Canción (MP3)",
            command=self.download_single,
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2"
        )
        single_btn.pack(pady=(0, 10))
        
        playlist_btn = tk.Button(
            buttons_frame,
            text="📀 Descargar Toda la Playlist (MP3)",
            command=self.download_playlist,
            font=("Arial", 12, "bold"),
            bg="#9b59b6",
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2"
        )
        playlist_btn.pack()
    
    def on_url_change(self, url: str):
        """Maneja cambios en la URL."""
        self.current_config.url = url
        if url and self.youtube_service.is_valid_youtube_url(url):
            self.root.after(1000, self.get_video_info)
    
    def on_path_change(self, path: str):
        """Maneja cambios en la ruta."""
        self.current_config.download_path = path
    
    def get_video_info(self):
        """Obtiene información del video o playlist."""
        url = self.current_config.url
        
        if not url:
            self.info_frame.set_info("Por favor, ingresa una URL de YouTube")
            return
        
        if not self.youtube_service.is_valid_youtube_url(url):
            self.info_frame.set_info("URL no válida. Ingresa una URL de YouTube válida")
            return
        
        def fetch_info():
            try:
                self.progress_frame.set_progress_text("Obteniendo información...")
                self.progress_frame.start_progress()
                
                info = self.youtube_service.get_video_info(url)
                
                if info.get('_type') == 'playlist':
                    title = info.get('title', 'Playlist sin título')
                    count = len(info.get('entries', []))
                    uploader = info.get('uploader', 'Canal no disponible')
                    info_text = f"📀 PLAYLIST: {title}\n👤 {uploader}\n🎵 {count} videos"
                else:
                    title = info.get('title', 'Título no disponible')
                    duration = info.get('duration', 0)
                    uploader = info.get('uploader', 'Canal no disponible')
                    
                    if duration:
                        mins, secs = divmod(duration, 60)
                        duration_str = f"{mins:02d}:{secs:02d}"
                    else:
                        duration_str = "Duración no disponible"
                    
                    info_text = f"📹 VIDEO: {title}\n👤 {uploader}\n⏱️ {duration_str}"
                
                self.root.after(0, lambda: self.info_frame.set_info(info_text))
                self.root.after(0, lambda: self.progress_frame.set_progress_text("Información obtenida correctamente"))
                
            except Exception as e:
                error_msg = f"Error al obtener información: {str(e)}"
                self.root.after(0, lambda: self.info_frame.set_info(error_msg))
                self.root.after(0, lambda: self.progress_frame.set_progress_text("Error al obtener información"))
            finally:
                self.root.after(0, self.progress_frame.stop_progress)
        
        thread = threading.Thread(target=fetch_info, daemon=True)
        thread.start()
    
    def download_single(self):
        """Descarga solo una canción."""
        self.current_config.is_playlist = False
        self.start_download()
    
    def download_playlist(self):
        """Descarga toda la playlist."""
        self.current_config.is_playlist = True
        self.start_download()
    
    def start_download(self):
        """Inicia el proceso de descarga."""
        if not self.validate_inputs():
            return
        
        download_thread = threading.Thread(
            target=self.download_audio,
            daemon=True
        )
        download_thread.start()
    
    def validate_inputs(self) -> bool:
        """Valida las entradas del usuario."""
        url = self.current_config.url
        path = self.current_config.download_path
        
        if not url:
            messagebox.showerror("Error", "Por favor, ingresa una URL de YouTube")
            return False
        
        if not self.youtube_service.is_valid_youtube_url(url):
            messagebox.showerror("Error", "URL no válida. Ingresa una URL de YouTube válida")
            return False
        
        if not path:
            messagebox.showerror("Error", "Por favor, selecciona una carpeta válida")
            return False
        
        return True
    
    def download_audio(self):
        """Ejecuta la descarga de audio."""
        try:
            self.progress_frame.set_progress_text("Iniciando descarga...")
            self.progress_frame.start_progress()
            
            def progress_hook(d):
                if d['status'] == 'downloading':
                    percent = d.get('_percent_str', 'N/A')
                    speed = d.get('_speed_str', 'N/A')
                    filename = d.get('filename', '').split('/')[-1].split('\\')[-1]
                    self.root.after(0, lambda: self.progress_frame.set_progress_text(
                        f"Descargando: {filename[:30]}... {percent} - {speed}"
                    ))
                elif d['status'] == 'finished':
                    filename = d.get('filename', '').split('/')[-1].split('\\')[-1]
                    self.root.after(0, lambda: self.progress_frame.set_progress_text(
                        f"Procesando: {filename[:30]}..."
                    ))
                elif d['status'] == 'processing':
                    self.root.after(0, lambda: self.progress_frame.set_progress_text(
                        "Convirtiendo a MP3..."
                    ))
            
            # Realizar descarga
            success_msg = self.youtube_service.download_audio(
                self.current_config, 
                progress_hook
            )
            
            self.root.after(0, lambda: self.progress_frame.set_progress_text("¡Descarga completada exitosamente!"))
            self.root.after(0, lambda: messagebox.showinfo(
                "Éxito", 
                f"{success_msg} en formato MP3 en:\n{self.current_config.download_path}"
            ))
            
        except Exception as e:
            error_msg = f"Error durante la descarga: {str(e)}"
            self.root.after(0, lambda: self.progress_frame.set_progress_text("Error en la descarga"))
            self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
        finally:
            self.root.after(0, self.progress_frame.stop_progress)