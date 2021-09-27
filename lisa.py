import pyttsx3 
import speech_recognition as sr 
import datetime ,wikipedia
import pyaudio,smtplib,webbrowser,os





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am lisa maam . Please tell me how can i help you !! ")
def takeCommand():
    #it takes microphone input from the user and returns string output 
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising....")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
       # print(e)
       print("Say that again please.....")
       return "None"
    return query 
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('dikshakakati2@gmail.com','Kakati017##')
    server.sendmail('dikshakakati2@gmail.com',to,content)
    server.close


    

if __name__ == "__main__":
    wishMe()
    
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia'in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query :
            webbrowser.open("youtube.com") 
        elif 'open google' in query :
            webbrowser.open("google.com")
        elif'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam , the time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codepath = "C:\\Users\\user\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email'in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "dikshakakati@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry maam , I am not able to send this mail.")
       