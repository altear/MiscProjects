import subprocess
from gtts import gTTS

audio_file = "hello.mp3"
tts = gTTS(text="Hello World!", lang="en")
tts.save(audio_file)
return_code = subprocess.call(["play", audio_file])
