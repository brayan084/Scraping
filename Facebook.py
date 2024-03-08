from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Facebook
def Scraping_Facebook(Urls):
    
    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    driver.get("https://www.facebook.com/PandoraEspana")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/i').click()

    url_list = Urls
    result_list = []

    index = 0
    while index < len(url_list):
        url = url_list[index]
        time.sleep(2)

        if url == 'NO TIENE':
            index += 1
            continue
        
        driver.get(url)
        time.sleep(4)
        
        try:
            Nombre = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1').text
            Nombre = Nombre.strip()
        except Exception:
            Nombre = 'No hay nombre'

        try:
            seguidores = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]').text
            seguidores = ' '.join(seguidores.split()[:2])
        except Exception:
            seguidores = 'No hay seguidores'

        try:
            me_gusta = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[1]').text
            me_gusta = ' '.join(me_gusta.split()[:2])
        except Exception:
            me_gusta = 'No hay me gusta'

        response = {'Url': url, 'Nombre': Nombre, 'Seguidores': seguidores, 'Me Gusta': me_gusta}
        result_list.append(response)

        index += 1
    
    print('----------- Facebook ------------ \n')
    # print(result_list)
    
    return result_list