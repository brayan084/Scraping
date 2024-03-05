from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Twitter
def Scraping_Twitter(Urls:list):
    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    url_list = Urls
    result_list = []

    index = 0
    while index < len(url_list):
        url = url_list[index]
        driver.get(url)
        time.sleep(3)

        Nombre = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]').text

        Seguidores = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text

        Siguiendo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
        
        Posts = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div').text
        Posts = Posts.split()
        if Posts[1] == 'mil' or Posts[1] == 'mill':
            Posts = ' '.join(Posts[:2])
        else: 
            Posts = ' '.join(Posts[:1])
            
            
        response = {'Url': url, 'Nombre': Nombre, 'Seguidores': Seguidores, 'Siguiendo': Siguiendo, 'Posts': Posts}
        result_list.append(response)

        index += 1

    print('----------- Twitter ------------ \n')
    print(result_list)

    return result_list