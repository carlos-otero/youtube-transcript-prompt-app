import re
import sys
import json
import requests
import pyperclip
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def extract_video_id(url):
    """
    Extrae el ID del video de varios formatos de URL de YouTube.
    """
    # Expresión regular para encontrar el ID
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None

def get_video_title(video_id):
    """
    Obtiene el título del video usando la API oEmbed de YouTube (no requiere API Key).
    """
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
        response = requests.get(oembed_url)
        if response.status_code == 200:
            data = response.json()
            return data.get('title', 'Video sin título')
    except Exception as e:
        print(f"⚠️ No se pudo obtener el título: {e}")
    return "Video de YouTube"

def get_transcript_text(video_id):
    """
    Intenta obtener la transcripción en el idioma original.
    """
    try:
        # Obtiene la lista de transcripciones disponibles
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Intenta obtener la generada manualmente o la autogenerada
        # Prioriza español o inglés, pero acepta cualquiera que sea el "original"
        transcript = transcript_list.find_transcript(['es', 'en', 'aa', 'ab', 'af', 'ak', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bn', 'ba', 'eu', 'be', 'bho', 'bs', 'br', 'bg', 'my', 'ca', 'ceb', 'zh-Hans', 'zh-Hant', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'dz', 'eo', 'et', 'ee', 'fo', 'fj', 'fil', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'kri', 'ku', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nso', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'ss', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'])
        
        # Descarga los datos
        transcript_data = transcript.fetch()
        
        # Une todo el texto en un solo string
        full_text = " ".join([entry['text'] for entry in transcript_data])
        return full_text, transcript.language
        
    except (TranscriptsDisabled, NoTranscriptFound):
        return None, None
    except Exception as e:
        print(f"❌ Error al obtener transcripción: {e}")
        return None, None

def generate_prompt(title, transcript_text):
    """
    Crea el prompt para la IA.
    """
    prompt = f"""Hola, actúa como un experto analista de contenidos y redactor.
    
Tengo la transcripción del siguiente video de YouTube:
Título: "{title}"

Por favor, realiza las siguientes tareas:
1. Genera un resumen ejecutivo de los puntos clave.
2. Extrae las conclusiones principales.
3. Si hay pasos prácticos o tutoriales, lístalos.

Aquí está la transcripción:
---
{transcript_text}
---
"""
    return prompt

def main():
    print("\n🎬 --- YouTube Transcript a IA --- 🎬")
    print("Este programa copiará al portapapeles un prompt listo para ChatGPT/Claude/Gemini.\n")
    
    while True:
        url = input("Pegue el enlace del video de YouTube (o 'salir' para terminar): ").strip()
        
        if url.lower() in ['salir', 'exit', 'quit']:
            break
            
        video_id = extract_video_id(url)
        
        if not video_id:
            print("❌ URL no válida. Inténtalo de nuevo.")
            continue
            
        print("⏳ Obteniendo información del video...")
        title = get_video_title(video_id)
        print(f"✅ Video detectado: {title}")
        
        print("⏳ Descargando transcripción...")
        text, lang = get_transcript_text(video_id)
        
        if text:
            print(f"✅ Transcripción obtenida (Idioma: {lang})")
            
            final_prompt = generate_prompt(title, text)
            
            try:
                pyperclip.copy(final_prompt)
                print("\n✨ ¡ÉXITO! ✨")
                print(f"El prompt para el video '{title}' ha sido copiado a tu portapapeles.")
                print("Ahora solo tienes que ir a tu IA favorita y presionar 'Pegar' (Ctrl+V).")
            except Exception as e:
                print(f"⚠️ No se pudo copiar al portapapeles automáticamente: {e}")
                print("Guardando en un archivo de texto 'prompt.txt' en su lugar...")
                with open("prompt.txt", "w", encoding="utf-8") as f:
                    f.write(final_prompt)
        else:
            print("❌ No se pudo encontrar una transcripción para este video (puede que no tenga subtítulos activados).")
        
        print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    main()