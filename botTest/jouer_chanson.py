import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime


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

    #pour jouer la musique sur youtube
    if ("chanson" or "musique") in command:
        chanteur = command.replace("mets la chanson de", "")
        print(chanteur)
        pywhatkit.playonyt(chanteur)
        parler(chanteur)
    #pour avoir l'heur een temps reel
    elif "heure" in command:
        heure = datetime.datetime.now().strftime("%H:%M")
        parler("Il est"+heure)

    elif "Bonjour" in command:
        parler("Bonjour ça va ?")



#pour faire paser en bloucle mon programme

while True:
    lancer_assistant()