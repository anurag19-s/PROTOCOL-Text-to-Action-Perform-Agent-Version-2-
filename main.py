from config import ASSISTANT_NAME
from commands import process_command
from speaker import speak


def run_assistant() -> None:
    print(f"{ASSISTANT_NAME} activated.")
    speak(f"{ASSISTANT_NAME} activated.")

    print("Type commands like:")
    print("- open youtube")
    print("- open notepad")
    print("- open downloads")
    print("- search google python tutorial")
    print("- search youtube node js crud api")
    print("- time")
    print("- date")
    print("- shutdown")
    print("- cancel shutdown")
    print("- exit")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            speak("Please type a command.")
            continue

        response = process_command(user_input)

        if response == "exit":
            speak("Shutting down. Goodbye.")
            break

        speak(response)


if __name__ == "__main__":
    run_assistant() 