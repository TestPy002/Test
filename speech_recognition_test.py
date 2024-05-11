import sounddevice as sd
import numpy as np
import speech_recognition as sr

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
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Record and play audio
    audio_data = record_audio()
    play_audio(audio_data)

    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    # Recognize speech from the recorded audio
    recognize_speech(audio_data, recognizer)
