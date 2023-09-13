import pyttsx3
import pyautogui
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to execute commands
def execute_command(command):
    if "open notepad" in command:
        pyautogui.press('win')
        pyautogui.write('Notepad', interval=0.25)
        pyautogui.press('enter')
        speak("Opening Notepad")
    elif "open calculator" in command:
        pyautogui.press('win')
        pyautogui.write('Calculator', interval=0.25)
        pyautogui.press('enter')
        speak("Opening Calculator")
    elif "close" in command:
        pyautogui.hotkey('alt', 'f4')
        speak("Closing applications")
    elif command.startswith("type"):
        text_to_type = command.split("type", 1)[1].strip()
        pyautogui.write(text_to_type)
        speak(f"Typing: {text_to_type}")
    elif command.startswith("search"):
        search_query = command.split("search", 1)[1].strip()
        pyautogui.press('win')
        pyautogui.write(search_query, interval=0.25)
        pyautogui.press('enter')
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
        user_input = input("Enter a command (or say it aloud): ").lower()
        
        if user_input:
            execute_command(user_input)
        
        voice_command = listen_to_user()
        if voice_command:
            execute_command(voice_command)
