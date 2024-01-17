import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for the wake word...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()

                if "genius" in command:
                    print("Wake word detected!")
                    speak("Yes, how can I assist you?")
                    return True

            except sr.UnknownValueError:
                # Ignore if no speech is detected
                pass
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        if listen_for_wake_word():
            # Perform actions or initiate a conversation after detecting the wake word
            print("Performing actions or initiating a conversation...")
            break
