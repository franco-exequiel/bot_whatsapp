import requests
from io import BytesIO
from config import get_twilio_auth

def audio_file(form_data):
    media_url = form_data.get("MediaUrl0")
    
    print("Media URL:", media_url[:5] + "...")

    if not media_url or not media_url.startswith("http"):
        raise ValueError("No se recibió un MediaUrl válido")

    response = requests.get(media_url, auth=get_twilio_auth())
    del media_url
    content_type = response.headers.get("Content-Type", "")
    print("Tipo real recibido:", content_type)
    print("Tamaño recibido:", len(response.content), "bytes")

    if response.status_code != 200:
        raise ValueError(f"Error al descargar audio: {response.status_code}")

    if "xml" in content_type or len(response.content) < 500:
        raise ValueError(f"Contenido inválido recibido de Twilio.")

    audio = BytesIO(response.content)
    audio.name = "audio.ogg"
    return audio

if __name__ == '__main__':
    pass