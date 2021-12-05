from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
from time import sleep
from time import time
from random import randint
import os
import datetime
import requests


#anahtarkelime.txt "python egitimi"
#adet.txt   "2"
#hedefsite.txt   "www.udemy.com"

class main_class():

    global settings_read
    def settings_read():
        
        liste_ayarlar = ["anahtarkelime", "adet", "hedefsite"]
        output = list()
        
        for data in liste_ayarlar:
            try:
                with open("settings_text\{}.txt".format(data),"r") as f:
                
                    data = f.read()
                    output.append(data)
            except:
                print("[ Dosya Okuma Hatası ]")
                
        return output

    
    global contrl
    def contrl(anahtar,link_hedef):
        
     
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('disable-infobars')
        
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('disable-popup-blocking')
        link = f"https://www.google.com/search?q={anahtar}&oq={anahtar}&sourceid=chrome&ie=UTF-8"
        driver.get(link)
        driver.maximize_window()
        s = randint(4,8) 
        sleep(s)
     
        indext = 1
        
        for i in range(0,4):
            try:
                
                reklam_ = driver.find_element_by_xpath(f"//*[@id='tads']/div[{indext}]/div/div/div[1]/a/div[2]/span[1]")
                
                xpt = f"//*[@id='tads']/div[{indext}]/div/div/div[1]/a/div[2]/span[1]"
                reklam_title = driver.find_element_by_xpath(f"//*[@id='tads']/div[{indext}]/div/div/div[1]/a/div[2]/span[2]")
                                                                
                try:
                    say = reklam_title.text.count(link_hedef)
                except:
                    say = 0
                 
                try:
                    #print(reklam_.text)
                    if reklam_.text == "Reklam·" and say > 0 or reklam_.text == "Reklam" and say > 0:
                        print(f">> Hedef: ['{reklam_title.text}']",indext-1)
                        return xpt,driver
                        
                    else:
                        print(f">> Hedef Değil: ['{reklam_title.text}']",indext-1)

                except:
                    print("Bu İndex Yok: ['İndex Yok']",indext-1)
                    indext += 1
                    continue

            except:
                print(f"Reklam Değil: ['{reklam_title.text}']",indext-1)
    
            indext += 1

    global adb_command

    def adb_command():
       
        # adb on
        """os.startfile("pi.exe")"""
        os.system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
        os.system("adb shell input tap 907 366")
        os.system("adb shell input keyevent KEYCODE_HOME")

        print("[ Uçak Modu Açılıyor... - sleep 7 ]")
        sleep(7)
        
        # adb off
        """os.startfile("pi.exe")"""
        os.system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
        os.system("adb shell input tap 907 366")
        os.system("adb shell input keyevent KEYCODE_HOME")
        
        print("[ Uçak Modu Kapanıyor... - sleep 7 ]")
        sleep(7)

    global attck

    def attck(xpt,driver):

        try:

            driver.find_element_by_xpath(xpt).click()

        except:
            try:

                driver.quit()
                
            except:
                os.system("taskkill /im firefox.exe")
        try:
            an = datetime.datetime.now()
            saat = str(an.hour) + ":" + str(an.minute)
            print(f"[ Tıklama Başarılı : {saat} ]\n")
        except:
            pass


        s = randint(4,8)
        sleep(s)
        try:

            driver.quit()
        except:
            pass


        
    def __init__(self):

        data_setting = settings_read()
        tekrarla = data_setting[1]
        tekrarla = int(tekrarla)
        
        a = 1
        print(f"""[ Tekrarlanacak miktar: '{tekrarla}' ]\n[ Hedef Site: '{data_setting[2]}' ]""")
        while tekrarla != 0:
            
            print("\n[ Tıklanma Sayısı : {} ]".format(a))
            tekrarla -= 1
            a += 1
            try:

                
                xpt,dr = contrl(data_setting[0],data_setting[2])
                attck(xpt,dr)
                adb_command()
            except:
                print("[ Hedef site ekranda bulunamadı yada ayarlarda bir hata yaptınız. ]")
                print(sys.exc_info()[0])
                os.system("taskkill /im firefox.exe")

                adb_command()


            
                
                
                
main_class()
