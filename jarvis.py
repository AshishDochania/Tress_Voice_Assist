import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=6 and hour<12):
        speak("Good Morning!")
    
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis sir, please tell me how may i help you")


def takeCommand():
    '''it takes microphone input from the user and returns string output for the use of the computer'''
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        # print(e) this line will print the error which we are getting due to some problem in hearing 
        print("say that again please ...")
        return "None"
    
    return query

# def sendEmail(to,content):



if __name__ =="__main__":
    # speak("Ashish is a good boy")
    wishMe()
    while(True):
        query=takeCommand().lower()
    
        # logic for executing tasks based on querys
        if('wikipedia' in query):
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif ('open youtube' in query):
            speak("opening youtube")
            webbrowser.open("youtube.com",new=1,autoraise=False)

        elif('open google' in query):
            webbrowser.open("google.com",new=2,autoraise=True)
        
        elif('open stackoverflow' in query):
            webbrowser.open("stackoverflow.com",new=1,autoraise=False)

        elif('play music' in query or 'open spotify' in query):
            webbrowser.open("spotify.com",new=1,autoraise=False)

        elif('show photos' in query or 'show pictures' in query):
            pic='D:\\Pictures\\Camera Roll'
            picture=os.listdir(pic)
            # print(picture)
            os.startfile(os.path.join(pic,picture[0]))

        elif('the time' in query):
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif('open code' in query or 'open v s' in query):
            codePAth="C:\\Users\\ashis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePAth)

        # elif("send email" in query):
        #     try:
        #         speak("what should i say?")
        #         content=takeCommand()
        #         to="ashishdochania2003@gmail.com"
        #         sendEmail(to,content)
        #         speak("email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry not able to send it")
            
        elif('exit' in query or 'quit'in query):
            speak("okay sir! , Have a good day sir!")
            break