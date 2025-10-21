"""
Componente de interfaz para mostrar información del video/playlist.
Muestra detalles como título, duración, canal, etc.
"""

import tkinter as tk

class InfoFrame:
    """Frame para mostrar información del contenido de YouTube."""
    
    def __init__(self, parent: tk.Widget):
        """
        Inicializa el frame de información.
        
        Args:
            parent (tk.Widget): Widget padre
        """
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#34495e")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura los elementos de la interfaz."""
        self.info_label = tk.Label(
            self.frame,
            text="Ingresa una URL para ver la información",
            font=("Arial", 10),
            fg="#bdc3c7",
            bg="#34495e",
            wraplength=500,
            justify="left"
        )
        self.info_label.pack(anchor="w")
    
    def set_info(self, info_text: str):
        """
        Establece el texto de información.
        
        Args:
            info_text (str): Texto a mostrar
        """
        self.info_label.config(text=info_text)
    
    def clear_info(self):
        """Limpia la información mostrada."""
        self.info_label.config(text="Ingresa una URL para ver la información")
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)