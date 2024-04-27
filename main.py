import os
import pdfplumber
from gtts import gTTS

def pdf_to_audio(pdf_path, output_path):
    # Abrir el archivo PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Inicializar una cadena vacía para almacenar el texto del PDF
        text = ""
        # Iterar sobre cada página del PDF
        for page in pdf.pages:
            # Extraer el texto de la página actual y agregarlo a la cadena de texto
            text += page.extract_text()

    # Crear un objeto gTTS con el texto del PDF y el idioma español
    tts = gTTS(text, lang='es')

    # Guardar el audio como un archivo MP3
    tts.save(output_path)

if __name__ == "__main__":
    pdf_file = "renacuajo.pdf"
    audio_output = "audiolibro.mp3"
    pdf_to_audio(pdf_file, audio_output)
