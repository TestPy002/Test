import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3

def record_audio(duration=5, sample_rate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    print("Recording complete.")
    return audio_data.flatten()

def play_audio(audio_data, sample_rate=44100):
    print("Playing...")
    sd.play(audio_data, samplerate=sample_rate)
    sd.wait()
    print("Playback complete.")

def recognize_speech(audio_data, recognizer):
    try:
        print("Recognizing...")
        audio_source = sr.AudioData(audio_data.tobytes(), sample_rate=44100, sample_width=2)
        recognized_text = recognizer.recognize_google(audio_source)
        print(f"Recognized: {recognized_text}")
        return recognized_text.lower()  # Convert to lowercase for case-insensitive comparison
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None

def speak(text):
    print(f"Speaking: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voice_assistant(command):
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm doing well, thank you!",
        "what's the time": "I'm sorry, I don't have the ability to tell the time yet.",
        "goodbye": "Goodbye! Have a great day.",
    }

    if command in responses:
        speak(responses[command])
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    while True:
        # Record and play audio
        audio_data = record_audio()
        play_audio(audio_data)

        # Recognize speech from the recorded audio
        recognized_text = recognize_speech(audio_data, recognizer)

        # If speech is recognized, let the assistant respond
        if recognized_text:
            voice_assistant(recognized_text)

        # Check if the user said "goodbye" to exit the loop
        if recognized_text == "goodbye":
            break
