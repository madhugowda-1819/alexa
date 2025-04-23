import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
import datetime
import pyjokes
import time
import threading
import signal
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

keep_listening = True

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('🎤 Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5, phrase_time_limit=8)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
    except sr.WaitTimeoutError:
        print("⌛ Listening timed out, no speech detected.")
    except:
        pass

    return command

def run_alexa(command):
    global keep_listening

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'The current time is {current_time}')

    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        try:
            info = wikipedia.summary(person, 1)
            talk(info)
            print(info)
        except:
            talk("Sorry, I couldn't find any information about that.")

    elif 'date' in command:
        today = datetime.datetime.today().strftime("%d %B, %Y")
        talk(f"Today's date is {today}")

    elif 'are you single' in command:
        talk("I'm in a relationship with WiFi.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'bye' in command or 'stop' in command or 'exit' in command:
        talk("Goodbye! Have a nice day.")
        keep_listening = False  

    else:
        talk("Sorry, I didn't understand that. Can you say it again?")
         

    return True

def signal_handler(sig, frame):
    global keep_listening
    keep_listening = False
    talk("Goodbye!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    global keep_listening
    talk("Hello, I'm Alexa. How can I help you?")
    keep_listening = True
    while keep_listening:
        command = take_command()
        if command:
            run_alexa(command)
        time.sleep(2)
    talk('Alexa is going to sleep...')

def call():
    raw_command = ""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=10, phrase_time_limit=5)
            raw_command = listener.recognize_google(voice).lower()
            print(f"🎧 Recognized: {raw_command}")
    except sr.WaitTimeoutError:
        print("⌛ No wake word heard. Timeout.")
    except:
        pass

    if 'alexa' in raw_command:
        main()
    else:
        # talk('Please say "Alexa" to wake me up.')
        time.sleep(2)

if __name__ == "__main__":
    while True:
        call()
