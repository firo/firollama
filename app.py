import ollama  # Importa il modulo Ollama per la chat
import streamlit as st  # Importa Streamlit per creare l'applicazione web

st.title("Firollama")  # Imposta il titolo dell'applicazione

# Inizializza lo storico dei messaggi
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Inizializza i modelli disponibili
if "model" not in st.session_state:
    st.session_state["model"] = ""
with st.sidebar:
    # Ottieni i nomi dei modelli disponibili da Ollama
    models = [model["name"] for model in ollama.list()["models"]]
    # Imposta il modello selezionato dall'utente
    st.session_state["model"] = st.selectbox("Scegli il modello:", models)

# Generatore per ottenere le risposte del modello in streaming
def model_res_generator():
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]

# Mostra i messaggi della chat dallo storico all'avvio dell'app
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dell'utente
if prompt := st.chat_input("Come posso aiutarti?"):
    # Aggiungi l'ultimo messaggio alla cronologia nel formato {ruolo, contenuto}
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Mostra il messaggio dell'utente
    with st.chat_message("user"):
        st.markdown(prompt)

    # Ottieni e mostra la risposta del modello
    with st.chat_message("assistant"):
        st.write(st.session_state["model"])
        message = st.write_stream(model_res_generator())
        st.session_state["messages"].append({"role": "assistant", "content": message})
