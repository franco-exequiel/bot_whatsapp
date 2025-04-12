#Configuración Bot DALAS
import os
from dotenv import load_dotenv

#Cargar variables de entonro
load_dotenv()

# Twilio Authentication
def get_twilio_auth():
    twilio_sid = os.getenv("TWILIO_SID")
    twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
    if not twilio_sid or not twilio_token:
        raise ValueError("El SID o el TOKEN no están definidos en el entorno") 
    return twilio_sid, twilio_token

# OPENAI Token
def get_openai_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("La API KEY no está definida en el entonro")
    return key