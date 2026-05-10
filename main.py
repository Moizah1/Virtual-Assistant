import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
#speak function
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
# Initialize the mixer
    pygame.mixer.init()
# Load and play the mp3
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
# Keep the script running until the audio ends
    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

#without api key it will not work
def aiprocess(command):
    client = OpenAI(
    api_key="abcd1234"  #openai api key is paid 
    )
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages = [
        {"role":"system", "content":"you are virtual assistant named Jarvis skilled in general tasks like Alexa and Google cloud. give short responses "},
        {"role": "user", "content" :command} ])
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
        webbrowser.open("https://www.bbc.com/news")  # or any news site you prefer
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
    else:
        #let openAi handle the request
        output = aiprocess(c)
        speak(output)


if __name__ =="__main__":
    speak("Initializing jarvis...")
    while True:
        #Listen for the specific word
        #obtain audio from microphone
        
        
        #recognizer speech using Google
        try:
            with sr.Microphone() as source:
             print("Listening.....")
             audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
             command = recognizer.recognize_google(audio)
            if(command.lower()== "jarvis"):
                speak("Yaaa")

                #Listen for command
                with sr.Microphone() as source:
                 print("jarvis active.....")
                 audio = recognizer.listen(source)
                 word = recognizer.recognize_google(audio)
                 processcommand(word)
                 
            print("Recognizing.....")
     
            print("jarvis thinks you said "+ command)   #fast understanding
        except Exception as e:
            print("Error; {}".format(e))    

