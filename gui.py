import tkinter as tk
import threading
import speech_recognition as sr
import webbrowser
import pyttsx3
from gtts import gTTS
import pygame
import os
from openai import OpenAI
import musiclibrary

# Voice and AI setup
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiprocess(command):
    client = OpenAI(api_key="abcd1234")  # Replace with actual API key
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis. Respond briefly."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower() or "open insta" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "news" in c.lower():
        webbrowser.open("https://www.bbc.com/news")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
    else:
        output = aiprocess(c)
        speak(output)
        update_jarvis_response(output)

# GUI Setup
root = tk.Tk()
root.title("Jarvis - Voice Assistant")
root.geometry("400x300")
root.resizable(False, False)

status_var = tk.StringVar(value="Status: Idle")

transcription_label = tk.Label(root, text="Heard:", font=("Arial", 12))
transcription_label.pack(pady=5)

transcription_box = tk.Text(root, height=5, width=45)
transcription_box.pack(pady=5)

response_label = tk.Label(root, text="Jarvis says:", font=("Arial", 12))
response_label.pack(pady=5)

response_box = tk.Label(root, text="", wraplength=350, font=("Arial", 10), justify="left")
response_box.pack(pady=5)

status_label = tk.Label(root, textvariable=status_var)
status_label.pack(pady=5)

listening = False

def update_transcription(text):
    transcription_box.delete(1.0, tk.END)
    transcription_box.insert(tk.END, text)

def update_jarvis_response(text):
    response_box.config(text=text)

def listen():
    global listening
    listening = True
    speak("Initializing Jarvis...")
    while listening:
        try:
            with sr.Microphone() as source:
                status_var.set("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                command = recognizer.recognize_google(audio)

                update_transcription(command)
                if command.lower() == "jarvis":
                    speak("Yaa?")
                    with sr.Microphone() as source:
                        status_var.set("Jarvis Active. Listening for command...")
                        audio = recognizer.listen(source)
                        word = recognizer.recognize_google(audio)
                        update_transcription(word)
                        processcommand(word)
                status_var.set("Waiting...")
        except Exception as e:
            status_var.set(f"Error or timeout: {str(e)}")

def start_listening():
    threading.Thread(target=listen, daemon=True).start()

def stop_listening():
    global listening
    listening = False
    status_var.set("Stopped.")

start_button = tk.Button(root, text="Start Listening", command=start_listening)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Listening", command=stop_listening)
stop_button.pack(pady=5)

root.mainloop()
