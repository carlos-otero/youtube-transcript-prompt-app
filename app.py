import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import requests
from bs4 import BeautifulSoup
from datetime import timedelta  # For formatting timestamps
import pyperclip  # For copying to clipboard (install with pip install pyperclip)

# Function to extract video ID from YouTube URL
def extract_video_id(url):
    pattern = r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([^&\n?#]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# Function to get the video title
@st.cache_data
def get_video_title(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.text.replace(' - YouTube', '').strip()
            return title
    return "Title not available"

# Helper to format seconds to [HH:MM:SS]
def format_time(seconds):
    td = timedelta(seconds=int(seconds))
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60
    secs = td.seconds % 60
    return f"[{hours:02d}:{minutes:02d}:{secs:02d}]"

# Function to get transcript in original language WITH TIMESTAMPS
@st.cache_data
def get_transcript(video_id):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.list(video_id)  # List of available transcripts
        
        if not transcript_list:
            return None
        
        # Prioritize manual/original transcript (not generated)
        fetched = None
        for tr in transcript_list:
            if not tr.is_generated:  # Manual/original per docs
                fetched = tr.fetch()
                break
        
        # Fallback to the first (usually generated in original language)
        if not fetched:
            first_tr = next(iter(transcript_list))
            fetched = first_tr.fetch()
        
        # Build transcript with timestamps manually
        transcript_lines = []
        for snippet in fetched:
            timestamp = format_time(snippet.start)
            transcript_lines.append(f"{timestamp} {snippet.text}")
        
        transcript = "\n".join(transcript_lines)
        return transcript
    except StopIteration:
        # Rare case: empty list in fallback
        return None
    except Exception as e:
        if "No transcript" in str(e) or "Transcript Unavailable" in str(e) or "Video unavailable" in str(e):
            return None
        else:
            st.error(f"Error getting transcript: {str(e)}")
            return None

# Main interface
st.set_page_config(page_title="YouTube Transcript to IA Prompt", layout="wide")
st.title("🔒 YouTube Transcript to IA Prompt")

# CSS for polished and compact look
st.markdown("""
    <style>
    .main {padding: 1.5rem;}
    .stTextInput > div > div > input {border-radius: 8px; border: 2px solid #e1e5e9; padding: 12px;}
    .stButton > button {border-radius: 8px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; font-weight: bold;}
    .prompt-box {background: #f8f9fa; border-radius: 8px; padding: 12px; border-left: 4px solid #667eea;}
    </style>
""", unsafe_allow_html=True)

# Centered and prominent input
#st.markdown("### 📎 Paste the YouTube video link here (processes automatically):")
#url = st.text_input("", placeholder="https://www.youtube.com/watch?v=...", key="url_input")
st.text_input(
    "Paste the YouTube video link here (processes automatically)",
    placeholder="https://www.youtube.com/watch?v=...",
    key="url_input",
    label_visibility="collapsed"  # Or "hidden" if you want it fully invisible
)
# Auto-processing: If valid URL, process
url = st.session_state.get("url_input", "")  # Ensure 'url' is defined; use session_state to retrieve value
if url:
    video_id = extract_video_id(url)
    if video_id:
        with st.spinner("🎥 Downloading title and transcript..."):
            title = get_video_title(video_id)
            transcript = get_transcript(video_id)
            
            if transcript:
                # English prompt
                english_prompt = f"""Conversation title: {title}

You are an expert in YouTube video summaries. You have been tasked with creating a concise and in-depth summary of the following video transcript. Use **only** the provided transcript text, without incorporating external information or assumptions.

**Step-by-step instructions for the summary:**
1. **Main summary**: Write a detailed, exhaustive, thorough, and concise summary in paragraph format. Capture the main ideas and essential information, eliminating unnecessary details and emphasizing critical points. Maintain clarity and fluency for easy reading. Bold (**text**) key terms, complex vocabulary, or important concepts within the summary, and provide a brief definition or explanation inline based on their use in the transcript.

2. **Contextual analogy**: Create a short and complex analogy from everyday life to provide context or illustrate the main theme of the transcript (e.g., comparing it to something relatable like a train journey or an urban ecosystem).

3. **Key points**: Generate 8-12 bullet points (each with a relevant emoji) that summarize the important moments or key ideas from the transcript. Keep each point brief but impactful.

4. **Keywords and terms**: Extract the 5-10 most important keywords, complex words not common to the average reader, and acronyms mentioned. For each, provide a brief explanation and definition based on its context in the transcript. Format as a list with **bold** for the term.

**General rules:**
- Keep the summary objective, clear, and user-friendly.
- Focus on the essence of the content to maximize understanding.
- End your notes with [End of Notes, Message #1] to indicate completion (increment the counter in future interactions if applicable).

Video transcript:
{transcript}"""

                # Spanish prompt
                spanish_prompt = f"""Título de la conversación: {title}

Eres un experto en resúmenes de videos de YouTube. Has sido asignado para crear un resumen conciso y profundo del siguiente transcript del video. Usa **solo** el texto proporcionado del transcript, sin incorporar información externa o suposiciones.

**Instrucciones paso a paso para el resumen:**
1. **Resumen principal**: Escribe un resumen detallado, exhaustivo, thorough y conciso en formato de párrafo. Captura las ideas principales y la información esencial, eliminando detalles innecesarios y enfatizando puntos críticos. Mantén claridad y fluidez para una lectura fácil. Bold (**texto**) los términos clave, vocabulario complejo o conceptos importantes dentro del resumen, y proporciona una breve definición o explicación inline basada en su uso en el transcript.

2. **Analogía contextual**: Crea una analogía corta y compleja de la vida cotidiana para dar contexto o ilustrar el tema principal del transcript (por ejemplo, comparándolo con algo relatable como un viaje en tren o un ecosistema urbano).

3. **Puntos clave**: Genera 8-12 bullet points (cada uno con un emoji relevante) que resuman los momentos importantes o ideas clave del transcript. Mantén cada punto breve pero impactante.

4. **Keywords y términos**: Extrae los 5-10 keywords más importantes, palabras complejas no comunes para un lector promedio, y acrónimos mencionados. Para cada uno, proporciona una explicación breve y una definición basada en su contexto en el transcript. Formatea como una lista con **bold** para el término.

**Reglas generales:**
- Mantén el resumen objetivo, claro y user-friendly.
- Enfócate en la esencia del contenido para maximizar la comprensión.
- Termina tus notas con [End of Notes, Message #1] para indicar completitud (incrementa el contador en futuras interacciones si aplica).

Transcript del video:
{transcript}"""
                
                st.success(f"✅ Done! Title: **{title}**. Choose a language to copy the prompt.")
                
                # Show English prompt in text_area
                with st.expander("📖 English Prompt (expand to view/edit):", expanded=False):
                    st.text_area("Generated English Prompt:", english_prompt, height=250)
                
                # Show Spanish prompt in text_area
                with st.expander("🇪🇸 Spanish Prompt (expand to view/edit):", expanded=False):
                    st.text_area("Generated Spanish Prompt:", spanish_prompt, height=250)
                
                # Two buttons for copying
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📋 Copy for English Summary"):
                        pyperclip.copy(english_prompt)
                        st.success("✅ English prompt copied to clipboard! (Paste it into your favorite IA with Ctrl+V)")
                with col2:
                    if st.button("📋 Copy for Spanish Summary"):
                        pyperclip.copy(spanish_prompt)
                        st.success("✅ Spanish prompt copied to clipboard! (Paste it into your favorite IA with Ctrl+V)")
            else:
                st.warning("⚠️ Could not get the transcript. Verify that the video has available subtitles.")
    else:
        st.warning("⚠️ Invalid link. Make sure it's a valid YouTube link.")

# Footer
st.markdown("---")
st.info("💡 This app is 100% private and local. Just paste and go!")