import datetime
from email import message
import webbrowser
from numpy import tile
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui as p
import random
from plyer import notification
from pygame import mixer
import speedtest
import cv2
import time
import platform

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

password_attempts = 4
password_file = "password.txt"
correct_password = False

for i in range(password_attempts):
    password = input("Enter Password to open Jarvis: ")
    with open(password_file, "r") as file:
        stored_password = file.read()
    if password == stored_password:
        correct_password = True
        break
    else:
        speak("Incorrect password.")

if not correct_password:
    print("Maximum password attempts reached. Exiting...")
    speak("Maximum password attempts reached, Exiting..")
    exit()

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")
  
def recognize_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    id_1 = "JASHAN"
    id_2 = "JASHAN"
    id_3 = "JASHAN"
    id_4 = "JASHAN"
    id_5 = "JASHAN"
    id_6 = "JASHAN"
    id_7 = "JASHAN"
    id_8 = "JASHAN"
    id_9 = "JASHAN"
    id_10 = "JASHAN"

    names = ['','JASHAN','JAHSAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN']

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3,640)
    cam.set(4,480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    should_exit = False  # Flag variable to control loop execution

    while not should_exit:
        ret, img = cam.read()
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(converted_image, scaleFactor=1.1, minNeighbors=5, minSize=(int(minW), int(minH)))

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            id, accuracy = recognizer.predict(converted_image[y:y+h, x:x+w])

            if accuracy < 55:
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                time.sleep(1)
                p.press("esc")

            else:
                id = "Unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))

            cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(1)
        if k == 27:  # Press 'Esc' key to exit
            should_exit = True

            time.sleep(1)
            cam.release()
            cv2.destroyAllWindows()
            print("Welcome back! Jashan ")     
            from GreetMe import greetMe
            greetMe()
 
if __name__ == "__main__":
    recognize_faces()
    while True:
        query = takeCommand().lower()
            
        if "go to sleep" in query:
            speak("Okay sir, you can call me anytime")
            break
        
        #################### JARVIS: The Trilogy 2.0 #####################
        
        if "change password" in query:
            speak("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"Your new password is {new_pw}")


        elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Please speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write("")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks: "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task: "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks: "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task: "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                                        
        elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

        elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("E:\\jashan\\jashan work\\Jarvis_Final\\FocusMode.py")
                        exit()

                    
                    else:
                        pass

        elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)


        elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")                       
                     
        elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    
        elif "ipl score" in query:
                   from plyer import notification  # pip install plyer
                   import requests  # pip install requests
                   from bs4 import BeautifulSoup  # pip install bs4

                   url = "https://www.cricbuzz.com//cricket-match//live-scores"
                   page = requests.get(url)
                   soup = BeautifulSoup(page.text, "html.parser")

                   team1_elements = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
                   team_score_elements = soup.find_all(class_="cb-ovr-flo")

                   if len(team1_elements) >= 2 and len(team_score_elements) >= 11:
                       team1 = team1_elements[0].get_text()
                       team2 = team1_elements[1].get_text()
                       team1_score = team_score_elements[8].get_text()
                       team2_score = team_score_elements[10].get_text()

                       print(f"{team1} : {team1_score}")
                       print(f"{team2} : {team2_score}")

                       notification.notify(
                           title="IPL SCORE",
                           message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                           timeout=15
                       )
                   else:
                       print("Failed to fetch the IPL score. Please try again later.")

                               
        elif "play a game" in query:
                    available_games = ["rock paper scissors", "guess the number"]
                    
                    speak("Sure! Here are the available games:")
                    for game in available_games:
                        speak(game)
                        print(game)
    
                    speak("Please choose a game to play.")
                    game_choice = takeCommand().lower()

                    if game_choice == "rock paper scissors":
        
                        speak("OK Let's play Rock Paper Scissors!")
                        print("OK Let's PLAY ROCK PAPER SCISSORS!")
                        
                        i = 0
                        Me_score = 0
                        Com_score = 0
                        
                        while i < 5:
                            choose = ("rock", "paper", "scissors")
                            com_choose = random.choice(choose)
            
                            speak("Choose rock, paper, or scissors.")
                            query = takeCommand().lower()
            
                            if query == "rock":
                                if com_choose == "rock":
                                    speak("ROCK")
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
                                elif com_choose == "paper":
                                    speak("Paper")
                                    Com_score += 1
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
                                else:
                                    speak("Scissors")
                                    Me_score += 1
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")

                            elif query == "paper":
                                if com_choose == "rock":
                                    speak("ROCK")
                                    Me_score += 1
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
                                elif com_choose == "paper":
                                    speak("Paper")
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
                                else:
                                    speak("Scissors")
                                    Com_score += 1
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
            
                            elif query == "scissors":
                                if com_choose == "rock":
                                    speak("ROCK")
                                    Com_score += 1
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
                                elif com_choose == "paper":
                                    speak("Paper")
                                    Me_score += 1
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
                                else:
                                    speak("Scissors")
                                    print(f"Score: ME - {Me_score} | COM - {Com_score}")
            
                            i += 1
        
                        print(f"FINAL SCORE: ME - {Me_score} | COM - {Com_score}")
        
                    elif game_choice == "guess the number":
        # Guess the Number game code
                        speak("Let's play Guess the Number!")
                        print("LET'S PLAY GUESS THE NUMBER!")
        
                        secret_number = random.randint(1, 100)
                        attempts = 0
                        guessed = False
        
                        while not guessed and attempts < 5:  # Limit attempts to 5
                            speak("Take a guess")
                            print("Take a guess:")
                            query = input().lower()
                            try:
                                guess = int(query)
                                attempts += 1
                
                                if guess < secret_number:
                                    speak("Too low!")
                                    print("Too low!")
                                elif guess > secret_number:
                                    speak("Too high!")
                                    print("Too high!")
                                else:
                                    speak(f"Congratulations! You guessed the number in {attempts} attempts!")
                                    print(f"Congratulations! You guessed the number in {attempts} attempts!")
                                    guessed = True
                            except ValueError:
                                speak("Invalid input! Please try again.")
                                print("Invalid input! Please try again.")
                        
                        if not guessed:
                            speak(f"Sorry, you have reached the maximum number of attempts. The secret number was {secret_number}.")
                            print(f"Sorry, you have reached the maximum number of attempts. The secret number was {secret_number}.")
        
                    else:
                        speak("I'm sorry, that game is not available.")
                        print("I'm sorry, that game is not available.")
                              
                
        elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

        elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                
        
        elif "how old am i" in query or "tell me my age" in query or "what is my age" in query:
                   speak("who are you please enter your name.")
                   name = input("Enter your name: ").lower()

                   if name == "jashan" or "Jashan" or "JASHAN":
                       birth_date = datetime.datetime(2010, 9, 18)
                       current_date = datetime.datetime.now()
                       age = current_date - birth_date
                       years = age.days // 365
                       months = (age.days % 365) // 30
                       days = (age.days % 365) % 30
                       hours = age.seconds // 3600
                       minutes = (age.seconds % 3600) // 60
                       seconds = (age.seconds % 3600) % 60
                       age_message = f"{name}, you are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old."
                       speak(age_message)
                       print(age_message)

                   if name == "sumer" or "Sumer" or "SUMER":
                       birth_date = datetime.datetime(1986, 8, 8)
                       current_date = datetime.datetime.now()
                       age = current_date - birth_date
                       years = age.days // 365
                       months = (age.days % 365) // 30
                       days = (age.days % 365) % 30
                       hours = age.seconds // 3600
                       minutes = (age.seconds % 3600) // 60
                       seconds = (age.seconds % 3600) % 60
                       age_message = f"{name}, you are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old."
                       speak(age_message)
                       print(age_message)

                   if name == "monika" or "Monika" or "MONIKA":
                       birth_date = datetime.datetime(1991, 12, 31)
                       current_date = datetime.datetime.now()
                       age = current_date - birth_date
                       years = age.days // 365
                       months = (age.days % 365) // 30
                       days = (age.days % 365) % 30
                       hours = age.seconds // 3600
                       minutes = (age.seconds % 3600) // 60
                       seconds = (age.seconds % 3600) % 60
                       age_message = f"{name}, you are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old."
                       speak(age_message)
                       print(age_message)

                   if name == "rishika" or "Rishika" or "RISHIKA":
                       birth_date = datetime.datetime(2005, 2, 8)
                       current_date = datetime.datetime.now()
                       age = current_date - birth_date
                       years = age.days // 365
                       months = (age.days % 365) // 30
                       days = (age.days % 365) % 30
                       hours = age.seconds // 3600
                       minutes = (age.seconds % 3600) // 60
                       seconds = (age.seconds % 3600) % 60                                 
                       age_message = f"{name}, you are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old."
                       speak(age_message)
                       print(age_message)

                   if name == "rahul" or "Rahul" or "RAHUL":
                       birth_date = datetime.datetime(2009, 10, 28)
                       current_date = datetime.datetime.now()
                       age = current_date - birth_date
                       years = age.days // 365
                       months = (age.days % 365) // 30
                       days = (age.days % 365) % 30
                       hours = age.seconds // 3600
                       minutes = (age.seconds % 3600) // 60
                       seconds = (age.seconds % 3600) % 60
                       age_message = f"{name}, you are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old."
                       speak(age_message)
                       print(age_message)  
                                               
                   else:
                       speak("Sorry, I don't have your details.")
        
    

                ############################################################
        elif "hello" in query:
                    speak("Hello sir, how are you ?")
        elif "i am fine" in query:
                    speak("that's great, sir")
        elif "how are you" in query:
                    speak("Perfect, sir")
        elif "thank you" in query:
                    speak("you are welcome, sir")
                
        elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=E3jOYQGu1uw&t=1246s&ab_channel=scientificoder")
                    

        elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
        elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
        elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                


        elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
        elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

        elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
        elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


        elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
        elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
        elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
        elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

        elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

        elif "message" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

        elif "temperature in chandigargh" in query:
                    search = "temperature in chandigarh"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

        elif "temperature of chandigargh" in query:
                    search = "temperature in chandigarh"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

        elif "weather in zirakpur" in query:
                    search = "weather in zirakpur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

        elif "temprature in zirakpur" in query:
                    search = "temprature in zirakpur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")    

                
                           
        elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

        elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

        elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                    
        elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

        elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                




                


 