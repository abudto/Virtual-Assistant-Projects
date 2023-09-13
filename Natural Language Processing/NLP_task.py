import pyttsx3
import pyautogui
import tkinter as tk

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
    elif "type" in command:
        text_to_type = command.split("type", 1)[1].strip()
        pyautogui.write(text_to_type)
        speak(f"Typing: {text_to_type}")
    elif "search" in command:
        search_query = command.split("search", 1)[1].strip()
        pyautogui.press('win')
        pyautogui.write(search_query, interval=0.25)
        pyautogui.press('enter')
        speak(f"Searching for: {search_query}")
    elif "open browser" in command:
        pyautogui.press('win')
        pyautogui.write('Microsoft Edge', interval=0.25)
        pyautogui.press('enter')
        speak("Opening the web browser")
    elif "open file explorer" in command:
        pyautogui.press('win')
        pyautogui.write('File Explorer', interval=0.25)
        pyautogui.press('enter')
        speak("Opening File Explorer")
    elif "volume up" in command:
        pyautogui.press('volumeup')
        speak("Increasing the volume")
    elif "volume down" in command:
        pyautogui.press('volumedown')
        speak("Decreasing the volume")
    elif "mute" in command:
        pyautogui.press('volumemute')
        speak("Muting the volume")
    else:
        speak("Sorry, I don't understand that command.")

# Function to handle button click
def on_button_click():
    user_input = user_input_entry.get().lower()
    if user_input:
        execute_command(user_input)

# Create the main application window
app = tk.Tk()
app.title("Virtual Assistant")

# Create a label
label = tk.Label(app, text="Enter a command:")
label.pack(pady=10)

# Create an entry field
user_input_entry = tk.Entry(app, width=40)
user_input_entry.pack()

# Create a button to submit the command
submit_button = tk.Button(app, text="Submit", command=on_button_click)
submit_button.pack(pady=10)

# Start the application loop
app.mainloop()
