import speech_recognition as sr
import pyttsx3 as ttx


listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty("voices")
engine.setProperty("voice", "french")

#definissons une fonction pour le parler

def parler(text):
    engine.say(text)
    engine.runAndWait()


#definissons une fonction pour le Ecouter

def ecouter():
    try:
        with sr.Microphone() as source:
            print("Parler maintenant")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language="fr-FR")
            command.lower()

    except:
        pass
    return command


#Definissons la fonction lancer assistant


def lancer_assistant():
    command = ecouter()
    print(command)
    if "bonjour" in command:
        text = "Bonjour, ça va ?"
        parler(text)




lancer_assistant()
