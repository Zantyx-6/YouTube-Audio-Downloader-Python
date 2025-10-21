"""
Componente de interfaz para entrada de URL.
Maneja la entrada y validación de URLs de YouTube.
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable

class URLFrame:
    """Frame para entrada de URL de YouTube."""
    
    def __init__(self, parent: tk.Widget, url_callback: Callable):
        """
        Inicializa el frame de URL.
        
        Args:
            parent (tk.Widget): Widget padre
            url_callback (Callable): Función a llamar cuando cambia la URL
        """
        self.parent = parent
        self.url_callback = url_callback
        
        self.frame = tk.Frame(parent, bg="#34495e")
        self.url_var = tk.StringVar()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura los elementos de la interfaz."""
        url_label = tk.Label(
            self.frame,
            text="URL del video o playlist de YouTube:",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg="#34495e"
        )
        url_label.pack(anchor="w", pady=(0, 5))
        
        self.url_entry = tk.Entry(
            self.frame,
            textvariable=self.url_var,
            font=("Arial", 11),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief="flat",
            bd=0
        )
        self.url_entry.pack(fill="x", ipady=8)
        
        # Bind para detectar cambios
        self.url_entry.bind('<KeyRelease>', self.on_url_change)
    
    def on_url_change(self, event):
        """Maneja cambios en la entrada de URL."""
        self.url_callback(self.url_var.get().strip())
    
    def get_url(self) -> str:
        """Obtiene la URL actual."""
        return self.url_var.get().strip()
    
    def set_url(self, url: str):
        """Establece la URL."""
        self.url_var.set(url)
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)