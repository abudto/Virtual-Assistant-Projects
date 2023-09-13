import speech_recognition as sr
import os
import pyttsx3
import pyautogui

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to execute commands
def execute_command(command):
    if "open notepad" in command:
        os.system("start notepad.exe")
        speak("Opening Notepad")
    elif "open calculator" in command:
        os.system("start calc.exe")
        speak("Opening Calculator")
    elif "close" in command:
        os.system("taskkill /f /im notepad.exe")
        os.system("taskkill /f /im calculator.exe")
        speak("Closing applications")
    elif "type" in command:
        text_to_type = command.split("type")[-1].strip()
        pyautogui.typewrite(text_to_type)
        speak(f"Typing: {text_to_type}")
    elif "search" in command:
        search_query = command.split("search")[-1].strip()
        os.system(f"start microsoft-edge:{search_query}")
        speak(f"Searching for: {search_query}")
    else:
        speak("Sorry, I don't understand that command.")

# Function to listen to user commands
def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio.")
        return None

if __name__ == "__main__":
    speak("Hello! How can I assist you?")
    
    while True:
        command = listen_to_user()
        if command:
            execute_command(command)
