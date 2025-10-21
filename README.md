# 🎵 Descargador de Audio YouTube (MP3)

Una aplicación de escritorio desarrollada en Python para descargar audio de videos y playlists de YouTube en formato MP3.

## ✨ Características

- 📹 Descarga audio de videos individuales de YouTube
- 📀 Descarga audio de playlists completas
- 🎵 Conversión automática a formato MP3
- 🎨 Interfaz gráfica moderna e intuitiva
- ⚡ Descargas rápidas y eficientes
- 📊 Información detallada del contenido
- 🔄 Progreso de descarga en tiempo real

## 🛠️ Requisitos del Sistema

### Dependencias de Python
- Python 3.7 o superior
- yt-dlp

### Dependencias del Sistema
- **FFmpeg** (requerido para conversión a MP3)

## 📦 Instalación

### 1. Instalar Python
Asegúrate de tener Python 3.7 o superior instalado:
```bash
python --version

### 2. Instalar FFmpeg

Windows:
# Opción 1: Usando Chocolatey (recomendado)
choco install ffmpeg

# Opción 2: Descarga manual
# 1. Ve a https://ffmpeg.org/download.html
# 2. Descarga la versión para Windows
# 3. Extrae el archivo y añade la carpeta 'bin' al PATH del sistema

macOS:
# Opción 1: Usando Homebrew
brew install ffmpeg

# Opción 2: Usando MacPorts
sudo port install ffmpeg

Linux (Debian/Ubuntu):
sudo apt update
sudo apt install ffmpeg

Linux (Arch):
sudo pacman -S ffmpeg

### 3. Instalar Dependencias de Python

pip install -r requirements.txt

🚀 Uso
1. Ejecutar la aplicación:

python main.py

2.Interfaz de usuario:

- Ingresa la URL del video o playlist de YouTube

- Selecciona la carpeta de destino

- Haz clic en "Obtener información" para ver detalles

- Elige "Descargar Solo Esta Canción" o "Descargar Toda la Playlist"

🏗️ Estructura del Proyecto:

youtube-downloader/
├── main.py                 # Punto de entrada principal
├── requirements.txt        # Dependencias de Python
├── README.md              # Documentación
└── src/                   # Código fuente
    ├── __init__.py
    ├── models/            # Modelos de datos
    │   ├── __init__.py
    │   └── download_config.py
    ├── services/          # Lógica de negocio
    │   ├── __init__.py
    │   └── youtube_service.py
    ├── gui/               # Interfaz gráfica
    │   ├── __init__.py
    │   ├── app.py
    │   └── components/
    │       ├── __init__.py
    │       ├── url_frame.py
    │       ├── path_frame.py
    │       ├── info_frame.py
    │       └── progress_frame.py
    └── utils/             # Utilidades
        ├── __init__.py
        └── dependency_checker.py

