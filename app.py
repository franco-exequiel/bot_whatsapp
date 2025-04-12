from flask import Flask, request,  Response
from openai import OpenAI
#Modulos Locales
from config import get_openai_api_key
from audio_processing import audio_file

app = Flask(__name__)

# Inicializar cliente de OpenAI con tu API key
client = OpenAI(api_key=get_openai_api_key())




@app.route("/webhook", methods=["POST"])
def webhook():
    

    try:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file = audio_file(request.form),
            language="es"
        )

        
        twiml_response = """<?xml version="1.0" encoding="UTF-8"?>
        <Response>
        <Message>Transcripción recibida: {}</Message>
        </Response>""".format(transcription.text)
        return Response(twiml_response, mimetype='application/xml'), 200
        

    except Exception as e:
        print("llega acá?")
        print("Error en transcripción:", str(e))
        return f"Error en transcripción: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)