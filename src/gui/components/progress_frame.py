"""
Componente de interfaz para mostrar progreso de descarga.
Incluye barra de progreso y etiqueta de estado.
"""

import tkinter as tk
from tkinter import ttk

class ProgressFrame:
    """Frame para mostrar progreso de descarga."""
    
    def __init__(self, parent: tk.Widget):
        """
        Inicializa el frame de progreso.
        
        Args:
            parent (tk.Widget): Widget padre
        """
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#34495e")
        self.progress_var = tk.StringVar(value="Listo para descargar")
        
        self.setup_ui()
        self.setup_styles()
    
    def setup_ui(self):
        """Configura los elementos de la interfaz."""
        # Barra de progreso
        self.progress_bar = ttk.Progressbar(
            self.frame,
            mode="indeterminate",
            style="Custom.Horizontal.TProgressbar"
        )
        self.progress_bar.pack(fill="x", pady=(0, 10))
        
        # Etiqueta de estado
        self.status_label = tk.Label(
            self.frame,
            textvariable=self.progress_var,
            font=("Arial", 10),
            fg="#95a5a6",
            bg="#34495e"
        )
        self.status_label.pack()
    
    def setup_styles(self):
        """Configura los estilos de la barra de progreso."""
        style = ttk.Style()
        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="#27ae60",
            troughcolor="#ecf0f1",
            borderwidth=0,
            lightcolor="#27ae60",
            darkcolor="#27ae60"
        )
    
    def set_progress_text(self, text: str):
        """
        Establece el texto de progreso.
        
        Args:
            text (str): Texto a mostrar
        """
        self.progress_var.set(text)
    
    def start_progress(self):
        """Inicia la animación de la barra de progreso."""
        self.progress_bar.start()
    
    def stop_progress(self):
        """Detiene la animación de la barra de progreso."""
        self.progress_bar.stop()
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)