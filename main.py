import pandas as pd

from Twitter import Scraping_Twitter
from Facebook import Scraping_Facebook
from Youtube import Scraping_Youtube
from InstagramApify import obtener_datos_de_instagram
from TicTok import Scraping_TikTok
# from Instagram import Scraping_Instagram

def convertir_a_numero(numero):
    
    numero = numero.replace('suscriptores', '').strip()
    numero = numero.replace(' ', '').replace(',', '')
    if numero.endswith(('K', 'k')):
        return '{:,.0f}'.format(float(numero[:-1]) * 1000).replace(',', '.')
    elif numero.endswith(('M', 'm')):
        return '{:,.0f}'.format(float(numero[:-1]) * 1000000).replace(',', '.')
    elif numero.endswith('mil'):
        return '{:,.0f}'.format(float(numero[:-3]) * 1000).replace(',', '.')
    elif numero.endswith('mill'):
        return '{:,.0f}'.format(float(numero[:-4]) * 1000000).replace(',', '.')
    elif numero.endswith('mill.'):
        return '{:,.0f}'.format(float(numero[:-5]) * 1000000).replace(',', '.')
    else:
        return numero

def Run_All():
        
    # Instagram 
    df_IG_Apify = pd.DataFrame(obtener_datos_de_instagram(lista_urls_Instagram))
    # Formatear los números en el DataFrame con puntos
    df_IG_Apify['postsCount'] = df_IG_Apify['postsCount'].apply(lambda x: '{0:,}'.format(x))  
    df_IG_Apify['followersCount'] = df_IG_Apify['followersCount'].apply(lambda x: '{0:,}'.format(x))  
    df_IG_Apify['followsCount'] = df_IG_Apify['followsCount'].apply(lambda x: '{0:,}'.format(x))  
    print(df_IG_Apify.head(30))
    
    # Tiktok 
    df_TIK = pd.DataFrame(Scraping_TikTok(lista_urls_TikTok))
    df_TIK['Seguidores'] = df_TIK['Seguidores'].apply(convertir_a_numero)
    df_TIK['Siguiendo'] = df_TIK['Siguiendo'].apply(convertir_a_numero)
    df_TIK['Me Gusta'] = df_TIK['Me Gusta'].apply(convertir_a_numero)
    print(df_TIK.head(30))
    
    # YouTube 
    df_YT = pd.DataFrame(Scraping_Youtube(lista_urls_Youtube))
    df_YT['Subscripciones'] = df_YT['Subscripciones'].apply(convertir_a_numero)
    df_YT['Videos'] = df_YT['Videos'].apply(convertir_a_numero)
    print(df_YT.head(30))
    
    # Twitter  
    df_TW = pd.DataFrame(Scraping_Twitter(lista_urls_Twitter))
    df_TW['Seguidores'] = df_TW['Seguidores'].apply(convertir_a_numero)
    df_TW['Siguiendo'] = df_TW['Siguiendo'].apply(convertir_a_numero)
    df_TW['Posts'] = df_TW['Posts'].apply(convertir_a_numero)
    print(df_TW.head(30))
    
    # Facebook 
    df_FB = pd.DataFrame(Scraping_Facebook(lista_urls_facebook))
    df_FB['Seguidores'] = df_FB['Seguidores'].apply(convertir_a_numero)
    df_FB['Me Gusta'] = df_FB['Me Gusta'].apply(convertir_a_numero)    
    print(df_FB.head(30))
    
    # Instagram 
    # df_IG = pd.DataFrame(Scraping_Instagram(lista_urls_Instagram))
    # df_IG['Seguidores'] = df_IG['Seguidores'].apply(convertir_a_numero)
    # df_IG['Seguidos'] = df_IG['Seguidos'].apply(convertir_a_numero)
    # df_IG['Publicaciones'] = df_IG['Publicaciones'].apply(convertir_a_numero)
    # print(df_IG.head(30))
    
    # Crear un ExcelWriter con el nombre del archivo Excel
    with pd.ExcelWriter('./Redes-Sociales.xlsx', engine='openpyxl') as writer:
        # Guardar cada DataFrame en una hoja diferente
        df_YT.to_excel(writer, sheet_name='Youtube', index=False)
        df_TW.to_excel(writer, sheet_name='Twitter', index=False)
        df_FB.to_excel(writer, sheet_name='Facebook', index=False)
        df_IG_Apify.to_excel(writer, sheet_name='Instagram', index=False)
        df_TIK.to_excel(writer, sheet_name='TikTok', index=False)
        # df_IG.to_excel(writer, sheet_name='Instagram', index=False)

    print("DataFrames guardados en diferentes hojas de Excel exitosamente.")
    
    
excel = 'E:\Sumate\Scraping\Backup - Importación de datos de APIs.xlsx'
hoja = 'Empresas'

data = pd.read_excel(excel, sheet_name=hoja)

data.fillna('NO TIENE', inplace=True)

lista_urls_facebook = data['RRSS - FB (URL)'].to_list()
lista_urls_Instagram = data['RRSS - IG (URL)'].to_list()
lista_urls_TikTok = data['RRSS - TT (URL)'].to_list()
lista_urls_Twitter = data['RRSS - TW (URL)'].to_list()
lista_urls_Youtube = data['RRSS - YT (URL)'].to_list()
    

Run_All()