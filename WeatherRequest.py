from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests



########################
# WeatherRequest class #
########################

class WeatherRequest:
    """Contains method for retrieving weather info"""

    @staticmethod
    def get_weather_info(location):
        """Search for the weather using Selenium and retrieve the weather info using BeautifulSoup
        
        Returns weather information in the form of a dictionary
        """

        #BeautifulSoup variables

        #Selenium variables
        options = Options()
        options.add_argument('--headless')
        service = Service(r'C:\Users\Bla125\PythonDev\GeckoDriver\geckodriver.exe')
        driver = webdriver.Firefox(service=service, options=options)

        ############
        # Selenium #
        ############
        driver.get('https://weather.com/')
        print('open web - done')

        try:
            search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#LocationSearch_input')))
            print('find search box - done')
        except:
            driver.quit()

        try:
            search.send_keys(f'{location}')
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#LocationSearch_input'), f'{location}'))
            print('type in box - done')
        except:
            driver.quit()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#LocationSearch_listbox')))
            search.send_keys(Keys.RETURN)
            print('hit enter - done')
        except:
            driver.quit()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , '.CurrentConditions--tempHiLoValue--3SUHy')))
            current_page = driver.current_url
            print('new page loaded - done')
        except:
            driver.quit()
        
        driver.quit()

        #################
        # BeautifulSoup #
        #################
        page = requests.get(f'{current_page}')
        soup = BeautifulSoup(page.content, 'html.parser')
        weather_info = {}


        # Gathers general weather info for today
        today_weather = soup.select('div.CurrentConditions--primary--2SVPh')

        for info in today_weather:
            today_temp = info.select('span.CurrentConditions--tempValue--3a50n')[0].text.strip()
            today_phrase = info.select('div.CurrentConditions--phraseValue--2Z18W')[0].text.strip()
            today_temp_hilo = info.select('div.CurrentConditions--tempHiLoValue--3SUHy')[0].get_text(strip = True)   

            weather_info = {
            'today_temp': today_temp, 
            'today_phrase': today_phrase, 
            'today_temp_hilo': today_temp_hilo
            } 


        # Gathers hourly weather info for today
        hourly_weather = soup.select('div.HourlyWeatherCard--TableWrapper--1IGDr')

        for info in hourly_weather:
            hr_time1 = info.select('span.Ellipsis--ellipsis--1sNTm')[0].text.strip()
            hr_temp1 = info.select('div.Column--temp--5hqI_')[0].text.strip()
            hr_cond1 = info.select('div.Column--icon--1MoS8')[0].text.strip()
            hr_precip1 = info.select('span.Column--precip--2ck8J')[0].text.strip()

            hr_time2 = info.select('span.Ellipsis--ellipsis--1sNTm')[1].text.strip()
            hr_temp2 = info.select('div.Column--temp--5hqI_')[1].text.strip()
            hr_cond2 = info.select('div.Column--icon--1MoS8')[1].text.strip()
            hr_precip2 = info.select('span.Column--precip--2ck8J')[1].text.strip()

            hr_time3 = info.select('span.Ellipsis--ellipsis--1sNTm')[2].text.strip()
            hr_temp3 = info.select('div.Column--temp--5hqI_')[2].text.strip()
            hr_cond3 = info.select('div.Column--icon--1MoS8')[2].text.strip()
            hr_precip3 = info.select('span.Column--precip--2ck8J')[2].text.strip()

            hr_time4 = info.select('span.Ellipsis--ellipsis--1sNTm')[3].text.strip()
            hr_temp4 = info.select('div.Column--temp--5hqI_')[3].text.strip()
            hr_cond4 = info.select('div.Column--icon--1MoS8')[3].text.strip()
            hr_precip4 = info.select('span.Column--precip--2ck8J')[3].text.strip()

            hr_time5 = info.select('span.Ellipsis--ellipsis--1sNTm')[4].text.strip()
            hr_temp5 = info.select('div.Column--temp--5hqI_')[4].text.strip()
            hr_cond5 = info.select('div.Column--icon--1MoS8')[4].text.strip()
            hr_precip5 = info.select('span.Column--precip--2ck8J')[4].text.strip()

            hour_info = {
            'hr_time1': hr_time1, 
            'hr_temp1': hr_temp1, 
            'hr_cond1': hr_cond1,
            'hr_precip1': hr_precip1,

            'hr_time2': hr_time2, 
            'hr_temp2': hr_temp2, 
            'hr_cond2': hr_cond2,
            'hr_precip2': hr_precip2,

            'hr_time3': hr_time3, 
            'hr_temp3': hr_temp3, 
            'hr_cond3': hr_cond3,
            'hr_precip3': hr_precip3,

            'hr_time4': hr_time4, 
            'hr_temp4': hr_temp4, 
            'hr_cond4': hr_cond4,
            'hr_precip4': hr_precip4,

            'hr_time5': hr_time5, 
            'hr_temp5': hr_temp5, 
            'hr_cond5': hr_cond5,
            'hr_precip5': hr_precip5
            }
        weather_info.update(hour_info) 


        # Gathers five day weather info
        five_day_weather = soup.select('div.DailyWeatherCard--TableWrapper--3mjsg')

        for info in five_day_weather:
            fd_day1 = info.select('span.Ellipsis--ellipsis--1sNTm')[0].text.strip()
            fd_temp1_hi = info.select('div.Column--temp--5hqI_')[0].text.strip()
            fd_temp1_lo = info.select('div.Column--tempLo--1GNnT')[0].text.strip()
            fd_cond1 = info.select('div.Column--icon--1MoS8.Column--small--3yLq9')[0].text.strip()
            fd_precip1 = info.select('span.Column--precip--2ck8J')[0].text.strip()

            fd_day2 = info.select('span.Ellipsis--ellipsis--1sNTm')[1].text.strip()
            fd_temp2_hi = info.select('div.Column--temp--5hqI_')[1].text.strip()
            fd_temp2_lo = info.select('div.Column--tempLo--1GNnT')[1].text.strip()
            fd_cond2 = info.select('div.Column--icon--1MoS8.Column--small--3yLq9')[1].text.strip()
            fd_precip2 = info.select('span.Column--precip--2ck8J')[1].text.strip()

            fd_day3 = info.select('span.Ellipsis--ellipsis--1sNTm')[2].text.strip()
            fd_temp3_hi = info.select('div.Column--temp--5hqI_')[2].text.strip()
            fd_temp3_lo = info.select('div.Column--tempLo--1GNnT')[2].text.strip()
            fd_cond3 = info.select('div.Column--icon--1MoS8.Column--small--3yLq9')[2].text.strip()
            fd_precip3 = info.select('span.Column--precip--2ck8J')[2].text.strip()

            fd_day4 = info.select('span.Ellipsis--ellipsis--1sNTm')[3].text.strip()
            fd_temp4_hi = info.select('div.Column--temp--5hqI_')[3].text.strip()
            fd_temp4_lo = info.select('div.Column--tempLo--1GNnT')[3].text.strip()
            fd_cond4 = info.select('div.Column--icon--1MoS8.Column--small--3yLq9')[3].text.strip()
            fd_precip4 = info.select('span.Column--precip--2ck8J')[3].text.strip()

            fd_day5 = info.select('span.Ellipsis--ellipsis--1sNTm')[4].text.strip()
            fd_temp5_hi = info.select('div.Column--temp--5hqI_')[4].text.strip()
            fd_temp5_lo = info.select('div.Column--tempLo--1GNnT')[4].text.strip()
            fd_cond5 = info.select('div.Column--icon--1MoS8.Column--small--3yLq9')[4].text.strip()
            fd_precip5 = info.select('span.Column--precip--2ck8J')[4].text.strip()



            five_day_info = {
            'fd_day1': fd_day1,
            'fd_temp1_hi': fd_temp1_hi,
            'fd_temp1_lo': fd_temp1_lo,
            'fd_cond1': fd_cond1,
            'fd_precip1': fd_precip1,

            'fd_day2': fd_day2,
            'fd_temp2_hi': fd_temp2_hi,
            'fd_temp2_lo': fd_temp2_lo,
            'fd_cond2': fd_cond2,
            'fd_precip2': fd_precip2,

            'fd_day3': fd_day3,
            'fd_temp3_hi': fd_temp3_hi,
            'fd_temp3_lo': fd_temp3_lo,
            'fd_cond3': fd_cond3,
            'fd_precip3': fd_precip3, 

            'fd_day4': fd_day4,
            'fd_temp4_hi': fd_temp4_hi,
            'fd_temp4_lo': fd_temp4_lo,
            'fd_cond4': fd_cond4,
            'fd_precip4': fd_precip4, 

            'fd_day5': fd_day5,
            'fd_temp5_hi': fd_temp5_hi,
            'fd_temp5_lo': fd_temp5_lo,
            'fd_cond5': fd_cond5,
            'fd_precip5': fd_precip5    
            }
        weather_info.update(five_day_info)

        print(weather_info)
        return(weather_info)
