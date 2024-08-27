# Usa Debian per ARM64 come base
FROM arm64v8/debian:bookworm-slim

# Aggiorna i pacchetti e installa Python, pip, e git
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Installa le librerie Python necessarie
RUN pip3 install \
    langchain \
    langchain_community \
    streamlit \
    urllib3==1.26.6

# Aggiungi Ollama (modifica il comando in base alla modalità di installazione di Ollama)
RUN apt-get install -y ollama

# Clona il repository GitHub nel container
RUN git clone https://github.com/firo/firollama.git /app

# Imposta la directory di lavoro
WORKDIR /app

# Espone la porta 8501, ma ricorda di mappare la porta 80 quando esegui il container
EXPOSE 8501

# Comando di default quando si esegue il container
CMD ["streamlit", "run", "app.py"]
