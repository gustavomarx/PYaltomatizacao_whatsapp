
from openai import OpenAI
client = OpenAI(api_key='sk-XYPRNRMbRuoFqesO3tsjCcSmwS6z6_SGUA53lSH33mT3BlbkFJSADWQHwZ05F9RuxMWXNZp_NGns3v3QQn_zYM0BHYsA')

audio_file = open("c:/Users/gusta/OneDrive/Área de Trabalho/Dev Python/workspace/automacao_crash/audioteste.mp3", "rb")
transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file,  response_format="text")
print(transcription.text)