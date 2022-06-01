import speech_recognition as sr
import pyttsx3 
import wikipedia
import pywhatkit

listener = sr.Recognizer()
player = pyttsx3.init()
voice=player.getProperty('voices')
player.setProperty('voice','french')



def listen():
    with sr.Microphone() as input_device:
        print("Je suis prêt, à l'écoute....")
        voice_content = listener.listen(input_device)
        text_command = listener.recognize_google(voice_content,language='fr-FR')
        text_command = text_command.lower()
        print(text_command)

    return text_command;


def talk(text):
    player.say(text)
    player.runAndWait()


def run_voice_bot():
     command = listen()
     if "wikipedia" in command:
        command = command.replace("wikipedia","")
        if "qu'est-ce que" in command:
            command = command.replace("qu'est-ce que", "")
            info = wikipedia.summary(command, 5)
            talk(info)
        elif "qui est" in command:
            command = command.replace("qui est", "")
            info = wikipedia.summary(command, 5)
            talk(info)
        elif "jouer" in command:
            command = command.replace("jouer", "")
            pywhatkit.playonyt(command)
        else:
            talk("Désolé, je ne comprends pas")

while True:
    run_voice_bot()