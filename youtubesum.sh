#!/bin/bash

# --- Configuración ---
VENV_NAME="venv_youtube"       # Nombre de la carpeta del entorno virtual
SCRIPT_NAME="youtube_summ_cli.py" # Nombre de tu script de Python

# 1. Asegurar que estamos en el directorio donde está este archivo .sh
# Esto permite ejecutar el script desde cualquier lugar sin errores de ruta
cd "$(dirname "$0")"

# 2. Comprobar si el archivo Python existe
if [ ! -f "$SCRIPT_NAME" ]; then
    echo "❌ Error: No encuentro el archivo '$SCRIPT_NAME' en esta carpeta."
    echo "Asegúrate de que este script .sh y el .py estén juntos."
    read -p "Presiona Enter para salir..."
    exit 1
fi

# 3. Comprobar si el entorno virtual existe, si no, crearlo
if [ ! -d "$VENV_NAME" ]; then
    echo "⚙️  Detectado primer uso. Configurando entorno virtual..."
    
    # Crear el entorno
    python3 -m venv "$VENV_NAME"
    
    if [ $? -ne 0 ]; then
        echo "❌ Error al crear el entorno virtual. Asegúrate de tener 'python3-venv' instalado."
        echo "Ejecuta: sudo apt install python3-venv"
        read -p "Presiona Enter para salir..."
        exit 1
    fi

    echo "📦 Instalando librerías necesarias (youtube-transcript-api, requests, pyperclip)..."
    # Usamos el pip del entorno virtual directamente
    ./$VENV_NAME/bin/pip install youtube-transcript-api requests pyperclip
    
    echo "✅ Instalación completada."
    echo "---------------------------------------------------"
fi

# 4. Ejecutar el script usando el Python del entorno virtual
echo "🚀 Iniciando aplicación..."
./$VENV_NAME/bin/python "$SCRIPT_NAME"

# (Opcional) Pausa al final si el script crashea inesperadamente para poder leer el error
echo "👋 Programa finalizado."