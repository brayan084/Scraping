from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Tiempo inicial
start_time = time.time()

# Abrir una página web
driver.get("https://twitter.com/apify")

# Esperar a que la página se cargue completamente
try:
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span")))
    # Tiempo final
    end_time = time.time()
    # Calcular el tiempo transcurrido
    elapsed_time = end_time - start_time
    print("La página se ha cargado completamente. Tiempo transcurrido:", elapsed_time, "segundos")
except:
    print("La página no se ha cargado completamente en el tiempo especificado.")

# Cerrar el navegador
driver.quit()