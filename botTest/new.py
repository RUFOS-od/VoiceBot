import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

#moteur parle
def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialiser un reconnaisseur
# écouter l'audio et le convertir en texte
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # écouter l'audio via la source
        print("Écoute terminée")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # erreur : le module de reconnaissance ne comprend pas
            engine_speak("je n'ai pas compris cela")
        except sr.RequestError:
            engine_speak('Désolé, le service est en panne') #erreur : le module de reconnaissance n'est pas connecté
        print(">>", voice_data.lower()) # imprimer ce que l'utilisateur a dit
        return voice_data.lower()

# obtenir une chaîne et créer un fichier audio à lire
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='fr-FR') # synthèse vocale (voix)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # sauvegarder entand que mp3
    playsound.playsound(audio_file) # lire le fichier audio
    print(asis_obj.name + ":", audio_string) # imprimer ce que l'application a dit
    os.remove(audio_file) # supprimer le fichier audio

def respond(voice_data):
    # 1 : salutation
    if there_exists(['salut','bonjour','hello']):
        greetings = ["salut, comment puis-je vous aider ?" + person_obj.name, "salut comment allez-vous?" + person_obj.name, "Je suis à votre écoute" + person_obj.name, "Que desirez-vous?" + person_obj.name, "coucou" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: nom
    if there_exists(["Comment t'appelles-tu "," comment t'appelles-tu "," dis-moi ton nom"]):

        if person_obj.name:
            engine_speak(f"Mon nom est {asis_obj.name}, {person_obj.name}") #obtient le nom des utilisateurs à partir de la saisie vocale
        else:
            engine_speak(f"Mon nom est {asis_obj.name}. Quel est ton nom?") #au cas où vous n'auriez pas fourni votre nom.

    if there_exists(["mon nom est"]):
        person_name = voice_data.split("est")[-1].strip()
        engine_speak("d'accord, Je vais me souvenir de cela " + person_name)
        person_obj.setName(person_name) # Se rappeler du nom est utlisateur
    if there_exists(["Quel est ton nom?"]):
        engine_speak("Votre nom doit être " + person_obj.name)
    
    if there_exists(["votre nom devrait être"]):
        asis_name = voice_data.split("être")[-1].strip()
        engine_speak("d'accord, Je vais me souvenir de cela, mon nom est " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: salutation
    if there_exists(["comment vas-tu", "comment tu vas"]):
        engine_speak("Je vais très bien, merci d'avoir demandé " + person_obj.name)

    # 4: temps
    if there_exists(["quelle heure est-il", "dis-moi l'heure", "il fait quelle heure", "heure"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " heure et " + minutes + "minutes"
        engine_speak(time)

    # 5: Recherche sur google
    if there_exists(["recherche"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Voici ce que j'ai trouvé pour" + search_term + "sur google")
    
    if there_exists(["chercher"]) and 'youtube' not in voice_data:
        search_term = voice_data.replace("chercher","")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: recherche sur youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("recherche","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Voici ce que j'ai trouvé pour " + search_term + "sur youtube")

     #7: obtenir le cours de l'action
    if there_exists(["prix de"]):
        search_term = voice_data.split("pour")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Voici ce que j'ai trouvé pour " + search_term + " sur google")
    


     #8 emploi du temps
    if there_exists(["afficher mon emploi du temps"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()
    
     #9 meteo
    if there_exists(["la météo"]):
        search_term = voice_data.split("la météo")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Voici ce que j'ai trouvé pour sur google")
     

     #10 ciseaux à papier de pierre
    if there_exists(["jeux"]):
        voice_data = record_audio("choisir entre papier pierre ou ciseaux")
        moves=["pierre", "papier", "ciseaux"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("La marchine a choisr" + cmove)
        engine_speak("votre choix est " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("le match est nul")
        elif pmove== "pierre" and cmove== "ciseaux":
            engine_speak("Gagner")
        elif pmove== "pierre" and cmove== "papier":
            engine_speak("Vous avez perdu")
        elif pmove== "papier" and cmove== "pierre":
            engine_speak("Bravo vous avez gagner")
        elif pmove== "papier" and cmove== "ciseaux":
            engine_speak("Vous avez perdu")
        elif pmove== "ciseaux" and cmove== "papier":
            engine_speak("Bravo vous avez gagner")
        elif pmove== "ciseaux" and cmove== "pierre":
            engine_speak("Vous avez perdu")

     #11 lancer une pièce
    if there_exists(["lancer", "retourner", "pièce de monnaie"]):
        moves=["face", "pile"]   
        cmove=random.choice(moves)
        engine_speak("la marchine a choisir " + cmove)

     #12 calc
    if there_exists(["plus","moins","multiplier","diviser","puissance","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiplier' or 'x':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'diviser':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'puissance':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Mauvais opérateur")
        
     #13 screenshot
    if there_exists(["capture","mon écran","capture d'écran"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')
    
    
     #14 pour rechercher sur wikipedia les définitions
    if there_exists(["définition de"]):
        definition=record_audio("De quoi avez-vous besoin de la définition de")
        url=urllib.request.urlopen('https://fr.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak("Je suis désolé, je n'ai pas trouvé cette définition, veuillez essayer une recherche sur le Web")
            elif definitions[1]:
                engine_speak("Voici ce que j'ai trouver"+definitions[1])
            else:
                engine_speak ("Voici ce que j'ai trouver"+definitions[2])
        else:
                engine_speak("Désolé je n'ai pas pu trouver la definition de "+definition)


    if there_exists(["sortie", "arrêter", "au revoir"]):
        engine_speak("au revoir")
        exit()

    # # Ville ou région actuelle
    # if there_exists(["Où suis-je"]):
    #     Ip_info = requests.get('https://api.ipdata.co?api-key=test').json() #api a changer
    #     loc = Ip_info['région']
    #     engine_speak(f"Vous devez être quelque part dans {loc}")    
   
   # Emplacement actuel selon Google maps
    if there_exists(["Où suis-je"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("Vous devez être quelque part près d'ici, selon Google Maps")    



time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'kakiri'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Enregistrement") # obtenir l'entrée vocale
    print("Raire")
    print("Q:", voice_data)
    respond(voice_data) # respond