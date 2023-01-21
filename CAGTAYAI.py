
import speedtest
import pyttsx3 
import datetime
import speech_recognition as sr
import webbrowser
import os
import pyautogui
import time
from gtts import gTTS
import socket
import random
from pygame import mixer
from bs4 import BeautifulSoup
mixer.init()
mixer.music.load('notf.wav')

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()



engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
isim= "Jarvis"






#AI speaking 
def speak(audio):
	engine.say(audio)
	engine.runAndWait()






#Wish me
def wishMe():
	hour = int(datetime.datetime.now().hour)
	
	if hour>=0 and hour<12:
		speak("Günaydın efendim")

	elif hour>=12 and hour<18:
		speak("iyi günler efendim")
	
	else:
		speak("İyi geceler efendim")

	speak("Buyrun size nasıl yardımcı olabilirim?")






#AI turns what you say into text
def takeCommand():
	mixer.music.play()
	#it takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Dinleniyor...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		
	try:
		print("Ses tanınıyor")
		query = r.recognize_google(audio,language='tr')
		print(f"Komut ; {query}\n")
		

	except Exception as e:
		print(e)
		speak("tekrar söylermisiniz")
		return "None"
	
	return query

def CallName():
	#it takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Dinleniyor...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		
	try:
		print("Ses tanınıyor")
		query = r.recognize_google(audio,language='tr')
		print(f"Komut ; {query}\n")
		

	except Exception as e:
		print(e)
		return "None"
	
	return query








wishMe()
def AI():
	
	query = takeCommand().lower()
	if 'open youtube' in query:
		speak('opening youtube..')
		webbrowser.open("youtube.com")
		
	elif 'according to google' in query:
		speak('opening google..')
		query = query.replace('according to google','')
		webbrowser.open("http://google.com/#q="+query,new=2)
	elif 'internet hız testi yap' in query:
		st = speedtest.Speedtest()
		speak("indirme hızınız hesaplanıyor lütfen bekleyin")
		downspeed = st.download()/1048576
		uploadspeed= st.upload()/1048576
		speak("İndirme hızınız saniyede" + str(int(downspeed))+"Megabit" + "Yükleme hızınız ise saniyede  " + str(int(uploadspeed))+"Megabit")
	elif 'adın ne' in query:
		speak("Adım" + isim + "Efendim")
	elif ('ne yapıyorsun' in query) :
		speak("Kendimi olabildiğince geliştirmeye çalışıyorum efendim")
	elif ('nasılsın' in query) or('ne haber' in query):
		speak("iyiyim, siz nasılsınız efendim")
	elif (query== 'yaşın kaç') or ('Kaç yaşındasın' in query):
		speak("1 yaşındayım efendim")

AI()

#AI waiting for you to call
while True:
		query = CallName().lower()
		if query == "hey":
			AI()
