import logging
import os
import subprocess
from typing import List
from elevenlabs import generate, save, set_api_key

from chatgpt_voice_assistant.bases.text_to_speech_client import TextToSpeechClient



class ElevenLabsTextToSpeechClient(TextToSpeechClient):
    """ElevenLabs TTS API that generates an MP3 file"""

    audio_extension = ".mp3"

    def __init__(self, api_key: str) -> None:
        set_api_key(api_key)

    def convert_text_to_audio(self, text_to_speak: str, audio_file_path: str) -> None:
        if os.path.exists(audio_file_path):
            raise FileExistsError(
                f"The audio file path already exists: {audio_file_path}"
            )

        
        #cmd: List[str] = ["say", text_to_speak, "-o", audio_file_path]
        audio = generate(
            text = text_to_speak,
            voice = "Rachel",
            model="eleven_monolingual_v1"
        )

        save(
            audio =  audio,
            filename = audio_file_path
        )

        file_size = os.path.getsize(audio_file_path)
        logging.debug(f"Wrote {file_size} bytes to {audio_file_path}")

        #logging.debug(cmd)
        #subprocess.call(cmd)

