import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import jenkins
def jenkins_output():
    server = jenkins.Jenkins('http://localhost:8080', username='mukunth', password='admin')
    version = server.get_version()
    #print(version)
    job_name = server.get_all_jobs()[0].get('name')
    #print(job_name)
    job_status = server.get_job_info(job_name, depth=1, fetch_all_builds=False)
    result = job_status.get('lastBuild').get('result')
    return result

text = jenkins_output()
print(text)
abc = ("Jenkins has executed, and the result is " + jenkins_output())
print(abc)


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
#speak(abc)

def get_audio():
    r = sr.Recognizer()
    global said
    with sr.Microphone() as source:
        audio = r.listen(source)
        get_audio.said = ""

        try:
            get_audio.said = r.recognize_google(audio)
            #print(get_audio.said)
        except Exception as e:
            print("Exception :" + str(e))
    return get_audio.said



speak("Hi, I am your personal assistant. May i have your name ?")
get_audio()
name = get_audio.said
speak("Hello" + name)
speak("Do you want to know the project status, say yes or no")
get_audio()
print(get_audio.said)
if get_audio.said == "yes":
    speak("Well, I guessed so. Let me check the project status. Can i proceed ? Yes or No")
    get_audio()
    print(get_audio.said)
    if get_audio.said == "yes":
        speak(abc)
        speak("Do you want to find another project status?. Yes Or no")
        get_audio()
        if get_audio.said == "yes":
            speak(abc)
        else:
            speak("Have a good day then, nice talking to you")
    else:
        speak("Okay, let me know whenever you wanted me to check")
else:
    speak("Sure, let me know if you need any help. Bye for now")



print(0)
