import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

Key = os.getenv('KEY_APIFY')

def obtener_datos_de_instagram(Urls:list):
    api_key = Key

    # Lista de perfiles de Instagram
    lista_perfiles = Urls
    
    Fields = 'username,fullName,url,biography,postsCount,followersCount,followsCount,highlightReelCount,hasChannel,isBusinessAccount,businessCategoryName,private,verified'

    # Configuración de la solicitud a la API
    config_apify = {
        "usernames": lista_perfiles
    }

    headers = {'Content-Type': 'application/json'}

    # Realizar la solicitud a la API
    url = f'https://api.apify.com/v2/acts/apify~instagram-profile-scraper/run-sync-get-dataset-items?token={api_key}&format=json&fields={Fields}'
    response = requests.post(url, headers=headers, data=json.dumps(config_apify))
    # print(response)
    
    if response.status_code == 201 or 200:
        responseData = response.json()
        
        return responseData
    
    return None
    
    


