
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random
import requests 
from bs4 import BeautifulSoup
import datetime

def get_weather():
    appid=''#add your's appid
    s_city = 'Sochi,RU'
    city_id = 491422
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        weather_today=('Сейчас в Сочи:'+data['weather'][0]['description']+', температура:'+str(data['main']['temp'])+
            ',ощущается как:'+str(data['main']['temp'])+' градусов цельсия, минимальная и максимальная температура'+str(data['main']['temp_min'])+' , '+
            str(data['main']['temp_max'])+' градусов цельсия. ' )
        return(weather_today)
   

    except Exception as e:
        print("Exception (find):", e)
        pass





def login(username, password):
    browser = webdriver.Chrome('/Users/rubyben/Desktop/bot_6am/chromedriver')

    try:
        browser.get('https://vk.com/')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_xpath("//*[@id='index_email']")
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_xpath( '//*[@id="index_pass"]')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(4)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)
        id =''#add an id of person who you want to write 
        browser.get('https://vk.com/'+id)

        time.sleep(10)
        send_button = browser.find_element_by_xpath( '/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/aside/div/div[1]/div/a[1]/button').click()
        time.sleep(10)
        p='//*[@id="mail_box_editable"]'

        now = datetime.datetime.now()
        sec = str(now)#time of sending
    

        send_message=browser.find_element_by_xpath(p)
        send_message.clear()
        send_message.send_keys(' Время отправки данного сообщения: '+sec+' ' +get_weather()+'')#here you can add a message
        time.sleep(4)

        send = browser.find_element_by_xpath(u).click()
        time.sleep(10)
        browser.close()
        browser.quit()


       
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

login(username,password)
