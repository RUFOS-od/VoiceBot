import webbrowser
import bs4 as bs
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
import random
import pyautogui
import urllib3 #screenshot
import urllib.request
import wikipedia
import webbrowser


listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french')
#la fonction qui permet de parler
def parler(text):
    engine.say(text)
    engine.runAndWait()
 #fbdhbhfjbsvdhjcbvjshvf
 #jfv,rhfkvfhgnre

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

    # if "chanson" or "Chanson" or "Musique" or "musique" in command:
    #     chanteur=command.replace('mets la chanson de','')
    #     print(chanteur)
    #     pywhatkit.playonyt(chanteur)
    if 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est'+heure)
    elif command in ['Salut','Bonjour','hello']:
        greetings = ["Salut, Bonjour",command+ "comment puis-je vous aider ?" , command+" comment allez-vous?", command+"Je suis à votre écoute" , command+"Que desirez-vous?", "coucou" ]
        greet = greetings[random.randint(0,len(greetings)-1)]
        parler(greet)

    elif "ton nom" in command:
        nom = "Je suis Kakiri, votre robot d'assistance"
        parler(nom)

    elif "qui suis-je" in command:
        moi = "Votre etes probablement mon detenteur"

    elif "que fais-tu" or "pourquoi existe tu" in command:
        cal = "C'est un secret"
        parler(cal)

    elif "ça va" in command:
        rep = "Je vais bien merci de demander. J'espère que vous-allez aussi bien que moi "

    elif "bien" in command:
        parler("Heureux d'entendre que tout vas bien")

    elif "où suis-je" in command:
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        parler("Vous devez être quelque part près d'ici, selon Google Maps")   

    # elif command in ["capture","mon écran","capture d'écran"]:
    #     myScreenshot = pyautogui.screenshot()
    #     myScreenshot.save('D:/screenshot/screen.png') 

    #pour jouer la musique sur youtube
    if "chanson" in command:
        chanteur = command.replace("mets la chanson de", "")
        print(chanteur)
        pywhatkit.playonyt(chanteur)
        parler(chanteur)


    elif "wikipedia" or "Wikipedia" in command:
        def wiki_person(text):
            list_wiki = text.split()
            for i in range(0, len(list_wiki)):
                if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "qui" and list_wiki[i + 1].lower() == "est":
                    return list_wiki[i + 2] + " " + list_wiki[i + 3]
        if "qui est" or "qu'est-ce que" in command:
            wikipedia.set_lang("fr")
            person = wiki_person(command)
            wiki = wikipedia.summary(person, sentences=2)
            parler(wiki)
 


#la boucle tanque les conditions ci-dessus sont vrais
while True:
    lancer_assistant()