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
    if "chanson" in command:
        chanteur = command.replace("mets la chanson de", "")
        print(chanteur)
        pywhatkit.playonyt(chanteur)
        parler(chanteur)
    #pour avoir l'heur een temps reel
    elif "heure" in command:
        heure = datetime.datetime.now().strftime("%H:%M")
        parler("Il est"+heure)

    elif "Bonjour" in command:
        parler("Bonjour comment allez vous ?")

    elif "concepteur" in command:
        parler("J'ai  été créer par le groupe 2, de la quatrième cohorte de orange digital academie ")

    #else:
        #parler("Bonjour, je suis Rufoce Bot. Votre assistant personnel. Je suis là pour vous faciliter la vie. Vous pouvez me commander d'effectuervdiverses tâches telles que: Vous informer sur l'actualité,  sur la metéo, l'heure, la prise de rendez-vous chez votre medecin, commander des achats en ligne, émettre des appels et pleine de chose.")


#pour faire paser en bloucle mon programme

while True:
    lancer_assistant()