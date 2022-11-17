import pyautogui
import time
import keyboard
import webbrowser
pozitie_initial_x=220
pozitie_initiala_y=270
pos_fin_x=1120
pos_fin_y=292
dif_x=1120-pozitie_initial_x
dif_y=1120-pozitie_initiala_y
curent_x=pozitie_initial_x
curent_x=220
curent_y=270
def autoviwe(curent_x,pos_fin_x,pozitie_initial_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y):
    time.sleep(1)
    while not keyboard.is_pressed('esc'):
        time.sleep(3)
        if curent_x<=pos_fin_x :
            pyautogui.click(curent_x,curent_y)
            print(1,curent_x,curent_y)
            curent_x=curent_x+260
            time.sleep(3)
            if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\back.png' , confidence=0.7)!= None:
                #camp_google=pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss' , confidence=0.7)
                pyautogui.click(pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\ss\back.png' , confidence=0.7))
        else:
            curent_x=pozitie_initial_x
            time.sleep(5)
            pyautogui.move(curent_x,curent_y)
            pyautogui.scroll(-350)
            time.sleep(5)   
webbrowser.open("https://www.youtube.com/")
time.sleep(5)           
autoviwe(curent_x,pos_fin_x,pozitie_initial_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y)