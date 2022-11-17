import pyautogui
import time
import keyboard

def cautare_google():
 time.sleep(5)
 if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\google_search.png', confidence=0.7) !=None:
    camp_google= pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\google_search.png', confidence=0.7) 
    pyautogui.click(camp_google)
    time.sleep(1)
    pyautogui.write('https://youtube.com')
    pyautogui.press('enter')
 else:
    print("Imaginea nu este pe ecran")


def cautare_youtube():
 time.sleep(5)
 if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\youtube_search.png', confidence=0.7) !=None:
    camp_youtube= pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\youtube_search.png', confidence=0.7) 
    pyautogui.click(camp_youtube)
    time.sleep(1)
    pyautogui.write('Speak')
    pyautogui.press('enter')
 else:
    print("Imaginea nu este pe ecran") 


def accesare_canal():
 time.sleep(5)
 if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\accesare_canal.png', confidence=0.7) !=None:
    camp_youtube= pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\accesare_canal.png', confidence=0.7) 
    pyautogui.click(camp_youtube)
 else:
    print("Imaginea nu este pe ecran")    

def subscribe():
 time.sleep(3)
 if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\subs.png', confidence=0.7) !=None:
    camp_youtube= pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\subs.png', confidence=0.7) 
    pyautogui.click(camp_youtube)
 else:
    print("Imaginea nu este pe ecran")  

cautare_google()
cautare_youtube()
accesare_canal()
subscribe()