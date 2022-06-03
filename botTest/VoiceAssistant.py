import datetime
from email.mime import audio
from jmespath import search
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import weathercom
import json
import webbrowser
import random
import pyttsx3 
from time import ctime
import time
import wikipedia
import urllib.request
import requests
import bs4 as bs

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "french")


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            kakiri_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio,  language="fr-FR")
        except sr.UnknownValueError:
            kakiri_speak("Désoler je n'ai rien capter")
        except sr.RequestError:
            kakiri_speak("Désoler, je ferme mon service")
        return voice_data
    


def kakiri_speak(audio_string):
    tts = gTTS(text=audio_string, lang="fr")
    r = random.randint(1,10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if "quel est ton nom" in voice_data:
        kakiri_speak("Mon nom est Kakiri, votre assistant vocal")
    if "temps" in voice_data:
        kakiri_speak(ctime())
    if "recherche" in voice_data:
        search = record_audio("que voulez-vous chercher?")
        if "où suis-je" in voice_data:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        kakiri_speak("Vous devez être quelque part près d'ici, selon Google Maps")   

        url = "https://google.com/search?q=" + search
        kakiri_speak("Voici le  resultat de mes recherches concernat " + search)
        webbrowser.get().open(url)
    if "localisation" in voice_data:
        location = record_audio("que voulez-vous localiser")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        kakiri_speak("Voici la localisation de " + search)
        webbrowser.get().open(url)
    if "heure" in voice_data:
        heure = datetime.datetime.now().strftime("%H:%M")
        kakiri_speak("il est "+ heure)

    if "bnjour" or "bonsoir" or "coucou" or "salut" in voice_data:
        kakiri_speak("Salut")

    if "wikipedia" or "Wikipedia" in voice_data:
        def wiki_person(text):
            list_wiki = text.split()
            for i in range(0, len(list_wiki)):
                if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "qui" and list_wiki[i + 1].lower() == "est":
                    return list_wiki[i + 2] + " " + list_wiki[i + 3]
        if "qui est" or "qu'est-ce que" in voice_data:
            wikipedia.set_lang("fr")
            person = wiki_person(voice_data)
            wiki = wikipedia.summary(person, sentences=2)
            kakiri_speak(wiki)

    if "qui suis-je" in voice_data:
        kakiri_speak( "Votre etes probablement mon detenteur")

    if "que fais-tu" or "pourquoi existe tu" in voice_data :
        kakiri_speak("C'est un secret")

    if "définition de" in voice_data:
        definition=record_audio("Avez-vous besoin de la définition de")
        url=urllib.request.urlopen('https://fr.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                kakiri_speak("Je suis désolé, je n'ai pas trouvé cette définition, veuillez essayer une recherche sur le Web")
            elif definitions[1]:
                kakiri_speak("Voici ce que j'ai trouver"+definitions[1])
            else:
                kakiri_speak ("Voici ce que j'ai trouver"+definitions[2])
        else:
                kakiri_speak("Désolé je n'ai pas pu trouver la definition de "+definition)


 
        
    if ("sortir" or "stop" or "sortie") in voice_data:
        exit()


time.sleep(1)
kakiri_speak("que puis-je pour vous?")

while(1):
    voice_data = record_audio()
    respond(voice_data)

# def voice_command_processor(ask=False):
#     with sr.Microphone() as source:
#         print("En écoute...")
#         if(ask):
#             audio_playback(ask)
#         audio = r.listen(source)
#         text = ''
#         try:
#             text=r.recognize_google(audio, language="fr-FR")
#         except sr.UnknownValueError as e:
#             print(e)
#         except sr.RequestError as e:
#             print("le service est en panne")

#         return text.lower()



# def audio_playback(text):
#     filename = "test.mp3"
#     tts = gTTS(text=text, lang='fr-FR')
#     tts.save(filename)
#     playsound.playsound(filename)
#     os.remove(filename)


# def execute_voice_command(text):
#     if ("qu'es-tu" or "qu'est-ce que tu es") in text:
#         audio_playback("je suis un système d'assistance vocale ")

#     if ("quel temps fait-il aujourd'hui" or "météo") in text:
#         city = voice_command_processor("quelle ville")
#         humidity, temp, phrase = weatherReport(city)
#         audio_playback("Actuellement à " + city + "  la température est " + str(temp)
#                        + " degré Celsius, " + "l'humidité est " + str(humidity) + " pour cent et le ciel est " + phrase)
#         print("Actuellement à " + city + "  la température est " + str(temp)
#               + "degré Celsius, " + "l'humidité est " + str(humidity) + " pour cent et le ciel est " + phrase)


# def weatherReport(city):
#     weatherDetails = weathercom.getCityWeatherDetails(city)
#     humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
#     temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
#     phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
#     return humidity, temp, phrase


# while True:
#     command = voice_command_processor()
#     print(command)
#     execute_voice_command(command)