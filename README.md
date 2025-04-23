🗣️ Alexa-Inspired Voice Assistant in Python 
📌 Project Overview
This is a simple and beginner-friendly Python voice assistant inspired by Amazon Alexa. Built without multithreading, the assistant runs sequentially in a single loop and listens for user commands through the microphone. It's designed for those who want to understand the fundamentals of voice recognition and speech response using Python.

🚀 Features
Wake Word Detection: Listens for the keyword “Alexa” to activate command mode.

Voice Command Recognition: Converts spoken language into text using Google’s Speech Recognition.

Text-to-Speech Response: Talks back using a natural-sounding female voice.

Play Songs: Plays YouTube videos when a command like “play [song name]” is given.

Time & Date: Tells the current time or date on request.

Wikipedia Lookup: Provides a short summary of famous people or topics.

Humor: Tells jokes using the pyjokes library.

Exit Commands: Gracefully ends the session when the user says "bye", "stop", or "exit".

🛠 Technologies Used
Python: The core programming language for building the assistant.

SpeechRecognition: For capturing and interpreting audio commands.

pyttsx3: For offline voice output.

pywhatkit: To play YouTube videos based on voice input.

Wikipedia: For retrieving short information summaries.

pyjokes: Adds a fun and engaging element by telling jokes.
