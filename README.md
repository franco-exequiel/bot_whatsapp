# 🤖 Bot de WhatsApp con Transcripción de Audio

Este es un bot de WhatsApp que recibe mensajes de voz y responde con la transcripción del audio.  
Funciona utilizando la **API oficial de OpenAI (Whisper en la nube)**, sin necesidad de procesamiento local.

En esta versión, se le envía un mensaje al número asignado por Twilio, y en segundos se recibe su transcripción.  
No importa si el audio es enviado directamente desde el chat, o si se le reenvía desde otra conversación.

---

## 🚀 Tecnologías usadas

- **Python 3**
- **Flask** para el servidor web (API)
- **OpenAI Whisper API (cloud)** para la transcripción de voz
- **PostgreSQL** para guardar usuarios y transcripciones
- **Ngrok** para exponer el servidor local y testear los webhooks
- **Git + GitHub** para versionado

---

## 🧠 Decisiones técnicas

- Se utiliza la **API en la nube de OpenAI** para la transcripción.
- **No se usa Whisper local** ni procesamiento con `torch`, `ffmpeg` o `pydub`.
- Se modularizó el código en:
  - `app.py`: servidor Flask
  - `audio_processing.py`: descarga de audio desde Twilio
  - `config.py`: variables de entorno y autenticación
- La conexión a base de datos se hace vía SQLAlchemy y PostgreSQL.

---

## ⚙️ Variables de entorno

> ✅ Podés copiar el archivo `.env.example` y completar tus credenciales.

Creá un archivo `.env` con lo siguiente:

```env
# OpenAI
OPENAI_API_KEY=tu_clave_openai

# Twilio
TWILIO_SID=ACxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxx

# Base de datos
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/tu_base

### Como correr el proyecto:

#Crear entorno virtual

python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

#Instalar dependencias

pip install -r requirements.txt

#Correr el servidor Flask

python app.py

#Exponer el servidor con ngrok
#Este proyecto fue testeado con ngrok para recibir mensajes desde el exterior:

ngrok http 5000
Copiá la URL pública generada (ej: https://xxxx.ngrok-free.app/webhook) y configurala como webhook en la plataforma que estés usando (Twilio o WhatsApp Business Cloud API de Meta).
