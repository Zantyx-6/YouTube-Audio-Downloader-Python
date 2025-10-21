"""
Componente de interfaz para selección de directorio.
Maneja la selección y visualización de la ruta de descarga.
"""

import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from typing import Callable

class PathFrame:
    """Frame para selección de directorio de descarga."""
    
    def __init__(self, parent: tk.Widget, path_callback: Callable):
        """
        Inicializa el frame de ruta.
        
        Args:
            parent (tk.Widget): Widget padre
            path_callback (Callable): Función a llamar cuando cambia la ruta
        """
        self.parent = parent
        self.path_callback = path_callback
        
        self.frame = tk.Frame(parent, bg="#34495e")
        self.path_var = tk.StringVar(value=str(Path.home() / "Downloads"))
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura los elementos de la interfaz."""
        path_label = tk.Label(
            self.frame,
            text="Carpeta de descarga:",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg="#34495e"
        )
        path_label.pack(anchor="w", pady=(0, 5))
        
        path_input_frame = tk.Frame(self.frame, bg="#34495e")
        path_input_frame.pack(fill="x")
        
        self.path_entry = tk.Entry(
            path_input_frame,
            textvariable=self.path_var,
            font=("Arial", 11),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief="flat",
            bd=0,
            state="readonly"
        )
        self.path_entry.pack(side="left", fill="x", expand=True, ipady=8)
        
        browse_btn = tk.Button(
            path_input_frame,
            text="📁 Explorar",
            command=self.browse_folder,
            font=("Arial", 10, "bold"),
            bg="#3498db",
            fg="white",
            relief="flat",
            bd=0,
            padx=15,
            cursor="hand2"
        )
        browse_btn.pack(side="right", padx=(10, 0), ipady=8)
    
    def browse_folder(self):
        """Abre el diálogo para seleccionar carpeta."""
        folder = filedialog.askdirectory(
            title="Seleccionar carpeta de descarga",
            initialdir=self.path_var.get()
        )
        if folder:
            self.path_var.set(folder)
            self.path_callback(folder)
    
    def get_path(self) -> str:
        """Obtiene la ruta actual."""
        return self.path_var.get().strip()
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)