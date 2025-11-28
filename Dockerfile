FROM python:3.12-slim

WORKDIR /app

# Copia requirements y instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY . .

# Expone el puerto de Streamlit
EXPOSE 8501

# Comando para correr la app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
