import pyttsx3
import speech_recognition as src #shortening the library name
import random
import pyjokes


engine = pyttsx3.init() #creating the engine

def speak(audio):
   engine.say(audio) #our engine speaks audio
   engine.runAndWait()

def get_voices(voice):
     voices = engine.getProperty('voices') #using the property: #voices
     if voice == 1:
          engine.setProperty("voice",voices[0].id) 
          speak("Hello I am a male voice")
     if voice ==2:
          engine.setProperty("voice",voices[1].id)
          speak("Hello I am a female voice")


def takeCommandmic():
   r = src.Recognizer() #creating the recognizer and defining it to #variable
   
   with src.Microphone() as source: #opening mic
        speak("Pleas say a command")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing")
            query = r.recognize_google(audio,language="en-US")  #setting the language to english and tranforming our audio to text
            print(query)
        except:
            print(e)
            speak("Please say that again")
            return "None"
   return query

def flip():  
    options = ['head', 'tails']
    answer = random.choice(options)
    sentence = f"you got {answer}"
    speak(sentence)

if __name__ == "__main__":
      get_voices(1) #setting the voice to girl or boy
      while True:
        query= takeCommandmic().lower() #getting mic input until #program breaks
        if "flip" in query:
            flip()
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif "close" in query:
            break #closes the assistant
        else:
            speak("That is not a command I recognize yet I am sorry")
        


