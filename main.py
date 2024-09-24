import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os
import requests
import yt_dlp

def audio_downloader():
    url = ""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'verbose': True
    }
    # Download the audio
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download and conversion completed successfully!")
    except Exception as e:
        print("thanks for using sir")

def web_downloader():
    chunk_size = 300
    url = ""
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open("video.mp4", "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
    else:
        print(f"Failed to download the file. Status code: {r.status_code}")


def video_downloader():
    url = ""
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return "Listening timed out, sorry"
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "Could not understand audio, please try again"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "Some error occurred, sorry"
        return query

def download_image( filename):
    url=""
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded as: {filename}")
    else:
        print("Failed to download image")

if __name__ == "__main__":
    speak("Hello, I am Jarvis AI. how can i help you?")
    sites = ["youtube", "google", "wikipedia", "canva"]
    cus_sites = [["machine learning"], ["https://www.youtube.com/watch?v=_u-PaJCpwiU&list=PLu0W_9lII9ai6fAMHp-acBmJONT7Y4BSG"]]

    while True:
        query = takecommand().lower()
        speak(query)

        for site in sites:
            if f"open {site}" in query:
                print(f"Opening {site} sir...")
                speak(f"Opening {site} sir...")
                webbrowser.open(f"https://{site}.com")

        if "open machine learning" in query:
            print(f"Opening Machine Learning sir...")
            speak(f"Opening Machine Learning sir...")
            webbrowser.open(cus_sites[1][0])

        if "download from web".lower() in query.lower():
            speak("downloading from web sir")
            web_downloader()
            speak("downloaded from web sir")

        if "who are you".lower() in query.lower():
            speak("iam jarvis,created by muhammad ibtisam asim.i can do any thing you want to do")

        # Search in Wikipedia
        if "search in wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("search in wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        # Play music
        l1=["song one","song 2","song 3","song for"]
        l2=["song1","song2","song3","song4"]
        if "play" in query:
            song_request = query.replace("play", "").strip()
            print("1.Courestry call")
            print("2.Lengends never die")
            print ("3.My demons")
            print("4.Nefex-Grateful")
            if song_request in l1:
                song_index = l1.index(song_request)
                music_dir = rf'C:\Users\Khirad\OneDrive\Desktop\python\songs\{l2[song_index]}.webm'
                print(f"Playing {song_request}...")
                os.startfile(music_dir)
            else:
                print("Song not found in the list.")
                speak("Song not found in the list.")

        # Open VS Code
        if "open vs code" in query:
            os.startfile("C:\\Users\\Khirad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        # Open ChatGPT
        if "open chat gpt" in query:
            os.startfile("C:\\Program Files\\ChatGPT\\ChatGPT.exe")

        # Open Excel
        if "open excel" in query:
            speak("Opening Excel sir")
            webbrowser.open("https://www.microsoft365.com/launch/Excel/?auth=1")


        if"download image".lower() in query.lower():
            speak("Downloading image sir...")
            download_image("custom_image_name.jpg")
            speak("Image successfully downloaded sir")

        if "download video".lower() in query.lower():
            speak("downloading video sir")
            video_downloader()
            speak("video has been downloaded sir")

        if "download audio".lower() in query.lower():
            speak("downloading audio sir")
            audio_downloader()
            speak("audio has been downloaded sir")

        # Exit the program
        if "exit the program" in query:
            speak("Bye bye sir")
            exit()