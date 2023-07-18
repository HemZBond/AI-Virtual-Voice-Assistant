import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser
import gtts as gt
import os
import sys
import random

from questions import quiz


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 178)


def talk(text):
    engine.say(text)
    engine.runAndWait()


#talk('Hi i am Jessi. how can i help you')


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jessi' in command:
                command = command.replace('jessi', '')
                print(command)
    except:
        pass

    return command



def check_ans(question, ans, attempts, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        talk(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(
            f"Wrong Answer :")
        talk(
            f"Wrong Answer :")
        return False


def intro_message():
    print("Welcome to this fun marvel quiz! \nAre you ready to test your knowledge about marvel?")
    talk("Welcome to this fun marvel quiz! \nAre you ready to test your knowledge about marvel?")
    print("There are a total of 6 questions, you can skip a question anytime by telling 'skip'")
    talk("There are a total of 6 questions, you can skip a question anytime by telling 'skip'")
    print("To move to the next question, say 'skip'")
    talk("To move to the next question, say 'skip'")


def take_test():
    intro = intro_message()
    while True:
        score = 0
        for question in quiz:
            attempts = 1
            while attempts > 0:
                print(quiz[question]['question'])
                talk(quiz[question]['question'])

                print(
                    "Tell your Answer  : ")
                talk(
                    "Tell your Answer : ")

                answer = take_command()
                print(take_command())
                if 'skip' in answer:
                    break

                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1

        break

    print(f"Your final score is {score}!\n\n")
    talk(f"Your final score is {score}!\n\n")
    print("Thanks for playing! ")
    talk("Thanks for playing! ")


def run_Jessi():

    contact_details = [["abhinav", "+917985617107"],
                       ["hemanth", "+919940029855"],
                       ["hemant", "+919940029855"]]
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'youtube' in command:
        talk('opening youtube')
        webbrowser.open('www.youtube.com')
    elif 'help' in command:
        #with sr.Microphone() as source:
        #     talk('tell me the contact person')
        #     listener.adjust_for_ambient_noise(source, duration=1)
        #     voice = listener.listen(source)
        #     command_name = listener.recognize_google(voice)
        #     command_name = command_name.lower()
        #     print(command_name)
        #     for i in range(0, 3):
        #         if command_name == contact_details[i][0]:
        #             cmd_name = contact_details[i][1]
        #     talk('tell me the message')
        #     listener.adjust_for_ambient_noise(source, duration=1)
        #     voice = listener.listen(source)
        #     command_msg = listener.recognize_google(voice)
        #     command_msg = command_msg.lower()
        #     print(command_msg)
        # talk('Opening whatsapp')
        pywhatkit.sendwhatmsg_instantly('+918489444533', 'Hemanth is in DANGER!', 10)
    elif 'chrome' in command:
        talk('opening Google chrome')
        webbrowser.open('www.google.co.in')
    elif 'whatsapp' in command:
        talk('opening Whatsapp')
        webbrowser.open('https://web.whatsapp.com/')
    elif 'close my assistant' in command:
        talk('See you soon boss')
        sys.exit()
    elif 'google meet' in command:
        talk('opening Google Meet')
        webbrowser.open('https://meet.google.com/')
    elif 'zoom meeting' in command:
        talk('opening zoom meeting')
        webbrowser.open('https://zoom.us/')
    elif 'gmail' in command:
        talk('opening g mail')
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    # elif 'ar' in command:
        # webbrowser.open(
        # 'https://drive.google.com/file/d/1IJU9GSM5n-UP6GIgxNwl0vfoNTm15skA/view?usp=sharing')
        #talk('Please scan the QR code to download the Augmented Reality application')
    elif 'gmail' in command:
        talk('opening gmail')
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    elif 'a r website' in command:
        talk('opening your website')
        webbrowser.open(
            """file:///D:/New%20folder/3D-Carousel-Using-Materialize-Html-CSS-jQuery/Model%20Page/index.html""")
    elif 'ar website' in command:
        talk('opening your augmented reality website')
        webbrowser.open(
            """file:///D:/New%20folder/3D-Carousel-Using-Materialize-Html-CSS-jQuery/Model%20Page/index.html""")
    elif 'sign language' in command:
        talk('opening your sign language website')
        webbrowser.open(
            """D:\Webpages\sIGN lANG\index.html""")
    elif 'assistant website' in command:
        talk('opening your voice assistant website')
        webbrowser.open(
            """https://codepen.io/Hemanth282002/full/LYdKzKj""")
    elif 'web portal' in command:
        talk('opening web portal')
        webbrowser.open(
            """http://teamtoofan.unaux.com/?i=1""")
        sys.exit()
    elif 'take test' in command:
        talk('opening your test module')
        take_test()
    elif 'test' in command:
        talk('opening your test module')
        take_test()
    elif 'google classroom' in command:
        talk('opening Google Classroom')
        webbrowser.open('https://classroom.google.com/')
    elif 'skillrack' in command:
        talk('opening skillrack')
        webbrowser.open(
            'https://www.skillrack.com/faces/ui/profile.xhtml;jsessionid=58DE74648AFC9DADB2EA9F17C2C3F0E2')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'when' in command:
        person = command.replace('when', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "where is" in command:
        ind = command.lower().split().index("is")
        location = command.split()[ind + 1:]
        url = "https://www.google.com/maps/place/" + "".join(location)
        talk("This is where" + str(location) + "is.")
        webbrowser.open(url)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hi' in command:
        talk('hello')
    elif 'sun' in command:
        talk('opening virtual reality model of sun')
        pywhatkit.sendwhatmsg_instantly(
            "+919840147595", "https://sketchfab.com/models/9ef1c68fbb944147bcfcc891d3912645/embed?autostart=1&cardboard=1&internal=1&tracking=0&ui_ar=0&ui_infos=0&ui_snapshots=1&ui_stop=0&ui_theatre=1&ui_watermark=0", 10)
        sys.exit()
    elif 'who are my teammates' in command:
        talk('Your team mates are Sudharsan, Shrinithi, Abhinav, Adarsh and Nivetha, you have a great team')
    elif 'do you know my name' in command:
        talk('Hi Hemanth, how can i forget you, you are my best friend')
    elif 'can you describe about my idea' in command:
        talk('You are doing Smart education: an innovative teaching module as your project. It contains Virtual voice assistant, IoT enabled classroom and an augmented reality teaching module. Your idea is really great, L-O-L your idea deserves first prize')
    elif 'who is my project guide' in command:
        talk('Your project guide is doctor swagata sarkar, you must be lucky to have such a great guide')
    elif 'about yourself' in command:
        talk('My name is Jessi, i am your virtual voice assistant. i will be helping you with all your assignments and homeworks, i can also remind you about your daily time table. And you can ask me any questions you want, I can answer all them ')
    elif 'myself' in command and 'tamil' in command:
        TamilText = "எனது பெயர் ஹேமந்த் ஸ்ரீ சாய்ராம் பொறியியல் கல்லூரி, தற்போது செயற்கை நுண்ணறிவு மற்றும் தரவு அறிவியலில் எனது 3வது இளங்கலைப் பட்டப்படிப்பைப் படித்து வருகிறேன்.!"
        tts = gt.gTTS(text=TamilText, lang='ta')
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    elif 'introduce' in command and 'tamil' in command:
        TamilText = "என் பெயர் ஜெஸ்ஸி, நான் உங்கள் மெய்நிகர் குரல் உதவியாளர். உங்கள் வீட்டுப்பாடம் மற்றும் அன்றாட நடவடிக்கைகளில் நான் உங்களுக்கு உதவுவேன். உங்களது அன்றாடப் பணியையும் என்னால் நினைவூட்ட முடியும்.!"
        tts = gt.gTTS(text=TamilText, lang='ta')
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    # elif 'welcome' in command and 'tamil' in command:
    #     TamilText = "மாண்புமிகு தமிழக முதல்வர் திரு.ஸ்டாலின் அவர்களுக்கு அன்பான வரவேற்பு. உங்களை சந்தித்ததில் மிக்க மகிழ்ச்சி. உங்கள் பணியை எனது குழு மிகவும் பாராட்டுகிறது. உங்கள் எதிர்கால வெற்றிகளுக்கு அனைத்து நல்வாழ்த்துக்களும். இதுவரை எங்கள் மாநிலத்திற்கு நீங்கள் செய்ததற்கு நன்றி.!"
    #     tts = gt.gTTS(text=TamilText, lang='ta')
    #     tts.save("Tamil-Audio.mp3")
    #     os.system("Tamil-Audio.mp3")
    elif ' bye' in command:
        talk('See you soon, Byee')
        sys.exit()
    elif 'netflix' in command:
        talk('''Sorry, I can't ruin your future, you are very precious''')
    elif 'hotstar' in command:
        talk('''Sorry, I can't ruin your future, you are very precious''')
    elif 'amazon prime' in command:
        talk('''Sorry, I can't ruin your future, you are very precious''')
    elif 'solar system' in command:
        talk('''Opening solar system 3D model''')
        webbrowser.open(
            'https://sketchfab.com/models/178d1deb210a4bc4a63ee05bc6cb6dcf/embed')
    elif 'sun' in command:
        talk('''Opening virtual reality of sun''')
        webbrowser.open(
            'https://sketchfab.com/models/9ef1c68fbb944147bcfcc891d3912645/embed?autostart=1&cardboard=1&internal=1&tracking=0&ui_infos=0&ui_snapshots=1&ui_stop=0&ui_watermark=0')
    elif 'earth' in command:
        talk('Earth is the third planet from the Sun and the only astronomical object known to harbor life. While large volumes of water can be found throughout the Solar System, only Earth sustains liquid surface water. About 71% of Earths surface is made up of the ocean, dwarfing Earths polar ice, lakes, and rivers. The remaining 29% of Earths surface is land, consisting of continents and islands. Earths surface layer is formed of several slowly moving tectonic plates, interacting to produce mountain ranges, volcanoes, and earthquakes. Earths liquid outer core generates the magnetic field that shapes Earths magnetosphere, deflecting destructive solar winds.')
    else:
        talk('Please say the command again.')


while True:
    run_Jessi()
