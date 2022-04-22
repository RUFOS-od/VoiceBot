import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french')
#la fonction qui permet de parler
def parler(text):
    engine.say(text)
    engine.runAndWait()
 

 #la fonction qui permet d'écouter

def ecouter():
    try:
        with sr.Microphone() as source: #lorsque le micro est allumer il affiche ("parler maintenant")
            print("parlez maintenant")
            voix=listener.listen(source) #recuperer la voix
            command=listener.recognize_google(voix,language='fr-FR') #reconnaitre le langage français
            command.lower()
  #s'il ne comprend rien alors il pass avec l'except          
    except:
        pass
    return command


 #la fonction qui permet de lancer le programme tout entier
def lancer_assistant():
    command=ecouter()
    print(command)
    if 'mets la chanson de' in command:
        chanteur=command.replace('mets la chanson de','')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est'+heure)
    elif 'Bonjour' in command:
        parler('bonjour,ca va?')
    else:
        print('je ne comprends pas')

#la boucle tanque les conditions ci-dessus sont vrais
while True:
    lancer_assistant()