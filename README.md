# YouTube Transcript to IA Prompt App 🎥 🤖

A private Streamlit app to extract full YouTube video transcripts (with timestamps) in their original language and generate ready-to-use prompts for AI summarization in English or Spanish. It's 100% local, secure, and runs on your machine without sending data to external servers.

![App Icon](logo.png)

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
5. Paste into your AI (e.g., Grok, ChatGPT, Claude) for a structured summary!

## Installation & Usage

### 🚀 Option 1: Quick Start (Recommended for Linux/Mac)
Use the included script to set up the environment and run the app automatically.

1. Clone the repo:
   ```bash
   git clone [https://github.com/your-username/youtube-transcript-prompt-app.git](https://github.com/your-username/youtube-transcript-prompt-app.git)
   cd youtube-transcript-prompt-app
````

2.  Run the start script:
    ```bash
    chmod +x start.sh
    ./start.sh
    ```

### ⚙️ Option 2: Manual Installation

1.  Create a virtual environment:
      * **Important**: Use a stable Python version (3.10, 3.11, or 3.12). Avoid Python 3.14 (alpha) to prevent compilation errors.
    <!-- end list -->
    ```bash
    # Standard
    python3 -m venv venv

    # If you have multiple versions (e.g., Fedora)
    python3.12 -m venv venv
    ```
2.  Activate the environment:
    ```bash
    source venv/bin/activate      # Linux/Mac
    venv\Scripts\activate         # Windows
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the app:
    ```bash
    streamlit run app.py
    ```

## OS-Specific Requirements

### 🐧 Linux (Fedora, Ubuntu, Mint, etc.)

To enable clipboard copying (`pyperclip`) and ensure libraries compile correctly:

  * **Fedora**:

    ```bash
    sudo dnf install xclip python3.12
    ```

    *(Note: Python 3.12 is recommended if your system defaults to Python 3.14)*

  * **Debian/Ubuntu/Mint**:

    ```bash
    sudo apt install xclip
    ```

### 🐳 Docker Deployment (Optional)

For easy portability without installing Python locally:

1.  Build the image:
    ```bash
    docker build -t youtube-app .
    ```
2.  Run the container:
    ```bash
    docker run -p 8501:8501 youtube-app
    ```
    Access at `http://localhost:8501`.

## Troubleshooting

  - **"Failed to build wheel for Pillow/lxml"**: This usually happens if you are using an experimental Python version (like 3.14). Install Python 3.12 (`sudo dnf install python3.12`) and recreate your virtual environment using that version.
  - **Clipboard not working**: Ensure `xclip` is installed on Linux. On Wayland, it should work, but `wl-clipboard` might be needed in some rare configurations.
  - **Transcript errors**: Verify the video actually has subtitles/captions available on YouTube.

## Contributing

Feel free to fork, PR, or open issues\! Suggestions for improvements (e.g., translation support, export to file) welcome.

## License

MIT License – See [LICENSE](https://www.google.com/search?q=LICENSE) for details.
