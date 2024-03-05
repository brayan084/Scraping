from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# YouTube
def Scraping_Youtube(Urls:list):

    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    url_list_YT = Urls
    result_list_YT = []

    index_YT = 0
    while index_YT < len(url_list_YT):
        url = url_list_YT[index_YT]
        driver.get(url)
        time.sleep(3)

        Nombre = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/div[2]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string').text

        Nombre_Canal = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/div[2]/div/div[1]/div/div[1]/span[1]/yt-formatted-string').text
        
        Subscripciones = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/div[2]/div/div[1]/div/div[1]/span[3]/yt-formatted-string').text
        Subscripciones = ' '.join(Subscripciones.split()[:2])
        
        Videos = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/div[2]/div/div[1]/div/div[1]/span[4]/yt-formatted-string/span[1]').text
        
        response = {'Nombre': Nombre, 'Nombre_Canal': Nombre_Canal, 'Subscripciones': Subscripciones, 'Videos': Videos}
        result_list_YT.append(response)

        index_YT += 1

    print('----------- Youtube ------------ \n')
    print(result_list_YT)
    
    return result_list_YT