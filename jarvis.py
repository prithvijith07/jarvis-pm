import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

    data = ""
    try:
        #  API key
       
        data = r.recognize_google(audio)
        print("what you said is: " + data)
    except sr.UnknownValueError:
        print("Google could not understand what you said")
    except sr.RequestError as e:
        print("Could not request results from Google service; {0}".format(e))

    return data
#berthe kore data
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())


#location valikkal
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on bro, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization
time.sleep(2)
speak("Hi bro, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
