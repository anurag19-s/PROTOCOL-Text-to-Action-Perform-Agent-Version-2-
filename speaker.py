import pyttsx3


def speak(text: str) -> None:
    print(f"Aayu: {text}")
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)

        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[0].id)

        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as error:
        print("Speech error:", error)