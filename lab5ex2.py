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

def coordonate():
    print(pyautogui.position())

col=1
#cautare_google()
while not keyboard.is_pressed('esc'):
        
        coordonate()
