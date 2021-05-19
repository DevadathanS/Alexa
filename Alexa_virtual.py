import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.capitalize()
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk("according to wikipedia, " + info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who are you' in command:
        info = wikipedia.summary("Alexa", 4)
        print(info)
        talk("according to wikipedia, I am " + info)
    elif "thank" in command:
        talk("It's my pleasure to work accordingly to your words!")
    elif "give me info about" in command:
        try:
            wiki = command.replace("give me info about ", "")
            s = wikipedia.summary(wiki, sentences=2)
            talk("According to wikipedia, " + str(s))
        except:
            pass
    elif "open google" in command:
        print("Opening google..")
        talk("opening google")
        open("https://www.google.co.in/search?q=")
    elif "search" in command:
        se = command.replace("search ", "")
        talk("Opening google...")
        open("https://www.google.co.in/search?q=" + str(se))
    else:
        print("I don't know that!")
        talk("I don't know that")


while True:
    run_alexa()
