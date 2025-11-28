# YouTube Transcript to IA Prompt App

A private Streamlit app to extract full YouTube video transcripts (with timestamps) in their original language and generate ready-to-use prompts for AI summarization in English or Spanish. It's 100% local, secure, and runs on your machine without sending data to external servers.

## Features
- **Automatic Processing**: Paste a YouTube link and it fetches the title, transcript, and generates prompts instantly.
- **Timestamps Included**: Transcripts come with formatted timestamps (e.g., [00:01:23]) for easy reference.
- **Bilingual Prompts**: Two buttons to copy prompts tailored for AI summaries in English or Spanish.
- **Clipboard Integration**: One-click copy to your system clipboard using `pyperclip`.
- **Error Handling**: Graceful warnings for videos without subtitles.

## Quick Demo
1. Run the app.
2. Paste a YouTube URL (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).
3. Expand the language sections to view prompts.
4. Click "Copy for English Summary" or "Copy for Spanish Summary".
5. Paste into your AI (e.g., Grok, ChatGPT) for a structured summary!

## Local Installation
1. Clone the repo:
   ```
   git clone https://github.com/your-username/youtube-transcript-prompt-app.git
   cd youtube-transcript-prompt-app
   ```
2. Create a virtual environment (recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```
   - Opens at `http://localhost:8501`.

**Note**: On Linux (e.g., Mint), ensure `xclip` or `xsel` is installed for clipboard support: `sudo apt install xclip`.

## Docker Deployment (Optional)
For easy portability or cloud deployment:
1. Install Docker.
2. Build the image:
   ```
   docker build -t youtube-app .
   ```
3. Run the container:
   ```
   docker run -p 8501:8501 youtube-app
   ```
   - Access at `http://localhost:8501`.

## Requirements
See `requirements.txt` for versions:
- Streamlit
- youtube-transcript-api
- BeautifulSoup4
- Requests
- Pyperclip

## Usage Notes
- **Supported Videos**: Works with videos that have subtitles (manual or auto-generated). If unavailable, shows a warning.
- **Privacy**: All processing is local; no API keys or external calls beyond YouTube's public transcript API.
- **Customization**: Edit `app.py` to tweak prompts or add features (e.g., more languages).
- **Troubleshooting**:
  - Transcript errors? Check video subtitles in YouTube.
  - Clipboard issues? Ensure `pyperclip` is installed and your OS supports it.

## Contributing
Feel free to fork, PR, or open issues! Suggestions for improvements (e.g., translation support, export to file) welcome.

## License
MIT License – See [LICENSE](LICENSE) for details.

---

# App Transcript de YouTube a Prompt para IA

Una app privada en Streamlit para extraer transcripciones completas de videos de YouTube (con timestamps) en su idioma original y generar prompts listos para usar en resúmenes con IA en inglés o español. Es 100% local, segura y se ejecuta en tu máquina sin enviar datos a servidores externos.

## Características
- **Procesamiento Automático**: Pega un enlace de YouTube y obtiene el título, transcript y genera prompts al instante.
- **Timestamps Incluidos**: Las transcripciones vienen con timestamps formateados (ej: [00:01:23]) para referencia fácil.
- **Prompts Bilingües**: Dos botones para copiar prompts adaptados a resúmenes en inglés o español.
- **Integración con Portapapeles**: Copia con un clic al portapapeles del sistema usando `pyperclip`.
- **Manejo de Errores**: Advertencias suaves para videos sin subtítulos.

## Demo Rápido
1. Ejecuta la app.
2. Pega un URL de YouTube (ej: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).
3. Expande las secciones de idioma para ver los prompts.
4. Haz clic en "Copy for English Summary" o "Copy for Spanish Summary".
5. Pégalo en tu IA (ej: Grok, ChatGPT) para un resumen estructurado.

## Instalación Local
1. Clona el repo:
   ```
   git clone https://github.com/tu-usuario/youtube-transcript-prompt-app.git
   cd youtube-transcript-prompt-app
   ```
2. Crea un entorno virtual (recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Ejecuta la app:
   ```
   streamlit run app.py
   ```
   - Se abre en `http://localhost:8501`.

**Nota**: En Linux (ej: Mint), asegúrate de tener `xclip` o `xsel` para soporte de portapapeles: `sudo apt install xclip`.

## Despliegue con Docker (Opcional)
Para portabilidad fácil o despliegue en la nube:
1. Instala Docker.
2. Construye la imagen:
   ```
   docker build -t youtube-app .
   ```
3. Ejecuta el contenedor:
   ```
   docker run -p 8501:8501 youtube-app
   ```
   - Accede en `http://localhost:8501`.

## Requisitos
Ver `requirements.txt` para versiones:
- Streamlit
- youtube-transcript-api
- BeautifulSoup4
- Requests
- Pyperclip

## Notas de Uso
- **Videos Soportados**: Funciona con videos que tengan subtítulos (manuales o auto-generados). Si no hay, muestra una advertencia.
- **Privacidad**: Todo el procesamiento es local; no hay claves API ni llamadas externas más allá de la API pública de transcripciones de YouTube.
- **Personalización**: Edita `app.py` para ajustar prompts o agregar funciones (ej: más idiomas).
- **Solución de Problemas**:
  - Errores en transcript? Verifica subtítulos en YouTube.
  - Problemas con portapapeles? Asegúrate de que `pyperclip` esté instalado y tu SO lo soporte.

## Contribuciones
¡Siéntete libre de hacer fork, PR o abrir issues! Sugerencias de mejoras (ej: soporte para traducción, exportar a archivo) bienvenidas.

## Licencia
Licencia MIT – Ver [LICENSE](LICENSE) para detalles.# youtube-transcript-prompt-app
# youtube-transcript-prompt-app
