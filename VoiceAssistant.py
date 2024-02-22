import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import operator
import pyjokes
from bs4 import BeautifulSoup
import subprocess
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from VoiceAssistantGUI import Ui_MainWindow
import GoogleCalendar
from twilio.rest import Client

EMAIL_DIC = {
    'myself': 'tanishsharma2003@gmail.com',
    'my college email': 'tanish.sharma3@s.amity.edu',
    'my second email': 'tanishsharma12062003@gmail.com',
    'harry': 'harshitsharma0912206@gmail.com'

}

NUMBERS = {
    'myself': '+919971030315',
    'mummy': '+919910366207',
    'papa': '+919810900108',
    'harry': '+919717291511'
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

# Text to Speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Speech to Text


# Greet


def greet():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir")
    elif hour > 12 and hour < 17:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("How may I help you?")

# Sending Email


def sendEmail(to, content):
    # try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("tanishsharma2003@gmail.com", "ovyvxbpxtupidltf")
    server.sendmail("tanishsharma2003@gmail.com", to, content)
    server.close()
    # return True
    # except Exception as e:
    # return False


def news():
    try:
        main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=1009205573d84e3985445bb97418b2ec"
        main_page = get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first", "second", "third", "fourth", "fifth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            speak(f"{day[i]} : {head[i]}")
    except Exception as e:
        print(e)
        speak("I am unable to get the news right now")


def call(to_num):
    to_call = NUMBERS.get(to_num)
    if to_call:
        account_sid = "ACf5bfa662973b617e6f07a56e5baed093"
        auth_token = "69266a625eaa563760db0a4d7624300d"
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            twiml="<Response><Say>Hi I am Jarvis. This is a test call.</Say></Response>", from_="+919971030315", to=to_call)
        print(call.sid)
    else:
        speak("Sorry Sir, but I couldn't find the person in your contacts")


WAKE = "hey jarvis"
WAKE1 = "hello jarvis"


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        while True:
            self.query = self.takecommand()
            if WAKE in self.query or WAKE1 in self.query:
                self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=3)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            speak("")
            return "none"
        query = query.lower()
        return query

    def TaskExecution(self):
        greet()

        while True:
            self.query = self.takecommand()

        # Logic Building for Tasks

            if "open notepad" in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open word" in self.query:
                wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(wpath)

            elif "open powerpoint" in self.query:
                ppath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(ppath)

            elif "open excel" in self.query:
                epath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(epath)

            elif "take a note" in self.query or "make a note" in self.query:
                speak("What should i write, sir?")
                note_text = self.takecommand().lower()
                date = datetime.datetime.now()
                file_name = str(date).replace(":", "-") + "-note.txt"
                with open(file_name, "w") as f:
                    f.write(note_text)
                notepad = "C:\\WINDOWS\\system32\\notepad.exe"
                subprocess.Popen([notepad, file_name])
                speak("Okay sir, I've made a note of that")

            elif "play music" in self.query:
                music_dir = "E:\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"Your IP Adress is {ip}")

            elif "wikipedia" in self.query:
                speak("Searching on Wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences=3)
                speak("According to Wikipedia")
                speak(result)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open google" in self.query:
                speak("What should I search on Google?")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "send message" in self.query or "send a message" in self.query:
                try:
                    speak("Whom do you wanna send the text sir?")
                    to_input = self.takecommand()
                    to_txt = NUMBERS.get(to_input)
                    if to_txt:
                        txt_h = int(datetime.datetime.now().hour)
                        txt_m = int(datetime.datetime.now().minute) + 2
                        speak("What's the message sir?")
                        msg = self.takecommand()
                        kit.sendwhatmsg(to_txt,
                                        msg, txt_h, txt_m)
                        speak("Message has been sent successfully")
                    else:
                        speak(
                            "Sorry Sir, but I couldn't find the requested person the contact list")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send that text")

            elif "youtube" in self.query:
                video = self.query.split(' ')[1:-2]
                speak(f"Okay sir, playing {video} on youtube")
                kit.playonyt(video)

            elif "send email" in self.query or "send an email" in self.query:
                try:
                    speak("Whom do you want to email sir?")
                    recepient = self.takecommand()
                    to_mail = EMAIL_DIC.get(recepient)
                    if to_mail:
                        speak("What is the subject sir?")
                        subject = self.takecommand()
                        speak("What should I say?")
                        message = self.takecommand()
                        content = 'Subject: {}\n\n{}'.format(subject, message)
                        sendEmail(to_mail, content)
                        speak("Email has been successfully sent")
                    else:
                        speak(
                            "Sorry Sir, but I couldn't find the requested person's email in my database")

                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send that mail")

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "tell me news" in self.query:
                speak("Today's latest news is")
                news()

            elif "do some calculations" in self.query or "can you calculate" in self.query:
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("What do you wanna calculate?")
                        print("Listening...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)

                    def get_operator_fn(op):
                        return {
                            '+': operator.add,
                            '-': operator.sub,
                            'x': operator.mul,
                            'divided': operator.__truediv__,
                        }[op]

                    def eval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("Your Result is")
                    speak(eval_binary_expr(*(my_string.split())))
                except Exception as e:
                    speak("Say that again please")

            elif "temperature" in self.query or "weather" in self.query:
                search = "temperature in delhi"
                url = f"https://www.google.com/search?q={search}"
                r = get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "what do i have today" in self.query:
                GoogleCalendar.main()

            elif "call" in self.query:
                try:
                    speak("Who do you wanna call sir")
                    to_num = self.takecommand()
                    call(to_num)
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, but I couldn't make the call")

            elif "sleep" in self.query:
                speak("Good Bye Sir")
                break

            elif "exit" in self.query:
                speak("Good Bye Sir")
                sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("bg.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
window = Main()
window.show()
exit(app.exec_())
[]
