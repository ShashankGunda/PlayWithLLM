import sounddevice as sd
import wavio
import assemblyai as aai
import google.generativeai as palm
from gtts import gTTS
import pygame


palm.configure(api_key='AIzaSyDBd-Rq3Rwri3SqtMe6aeF_-vAH2c0Rajg')
# Parameters for audio recording and playback
duration = 10  # Recording duration in seconds
fs = 44100    # Sampling frequency
filename = "recorded_audio.wav"  # Name of the output audio file

def record_audio():
    print("Recording audio...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2, blocking=True)
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    return audio_data

def save_audio_to_file(audio_data, filename):
    wavio.write(filename, audio_data, fs, sampwidth=2)

def transcribe_audio(filename):
    aai.settings.api_key = "f6fbee84cf894c56ba333f2c0b1e2c8a"
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(filename)

    print(transcript.text)
    return transcript.text

def LLM( input ):

    prompt = input+" in below 50 words"

    # Assuming palm is a library for conversation, you can replace this line with your actual code
    response = palm.chat( context = "You are a Cyboo, the latest innovation in an advanced humanoid robot Made in the collaboration of Treeex, Sky N Fire and KSI . The conversation voice to voice assistant makes friendly chit-chat ", messages=prompt, temperature = 0.8, top_k = 40, top_p = 0.95)

    # Print the model's response
    print(response.last)

    return response.last

def TTS( input ):


    # Text you want to convert to speech
    text = input

    # Create a gTTS object
    tts = gTTS(text)

    # Save the generated speech as an audio file
    tts.save("output.wav")

    pygame.init()
    pygame.mixer.init()

    sound = pygame.mixer.Sound('output.wav')
    sound.play()

    pygame.time.wait(int(sound.get_length() * 1000))  # Wait for the sound to finish
    pygame.quit()



while True:
    audioData = record_audio()
    save_audio_to_file(audioData, filename)
    transcription = transcribe_audio(filename)
    speech_text = LLM(transcription)
    TTS(speech_text)