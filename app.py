from google.cloud import texttospeech, storage
from pdfToString import extractedPDF

def synthesize_long_audio(project_id, location, output_gcs_uri):
    client = texttospeech.TextToSpeechClient()

    textToAudio = extractedPDF

    input = texttospeech.SynthesisInput(text=textToAudio)

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    voice = texttospeech.VoiceSelectionParams(language_code="pt-BR", name="pt-BR-Neural2-C") 
        #Supported voices on: https://cloud.google.com/text-to-speech/docs/voices
        
        #parent = f"projects/{project_id}/locations/{location}"

    request = texttospeech.SynthesizeSpeechRequest(
        input=input,
        voice=voice,
        audio_config=audio_config,
    )

    response = client.synthesize_speech(request=request)

    storage_client = storage.Client()
    bucket_name, object_name = output_gcs_uri.split('/', 2)[-1].split('/', 1)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_string(response.audio_content, content_type='audio/wav')

    print(f'\n Created on "{output_gcs_uri}"')

project_id = 'xx'
location = 'xx'
output_gcs_uri = 'xx'

synthesize_long_audio(project_id, location, output_gcs_uri)
