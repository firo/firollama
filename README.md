# Firollama

Questo repository contiene un semplice progetto Streamlit che viene eseguito all'interno di un container Docker.

## Come costruire l'immagine Docker

Usa Portainer o il comando Docker per costruire l'immagine direttamente dal Dockerfile:

Per eseguire il container
```bash
docker run -d -p 80:8501 firollama

docker build -t firollama .


