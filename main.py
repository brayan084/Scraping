import pandas as pd


from Facebook import Scraping_Facebook
from Twitter import Scraping_Twitter
from Youtube import Scraping_Youtube
from Instagram import Scraping_Instagram
from TicTok import Scraping_TikTok

def convertir_a_numero(numero):
    
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
    
    
    df_TIK = pd.DataFrame(Scraping_TikTok(urls_TIK))
    df_TIK['Seguidores'] = df_TIK['Seguidores'].apply(convertir_a_numero)
    df_TIK['Siguiendo'] = df_TIK['Siguiendo'].apply(convertir_a_numero)
    df_TIK['Me Gusta'] = df_TIK['Me Gusta'].apply(convertir_a_numero)
    print(df_TIK.head())
    
    df_TW = pd.DataFrame(Scraping_Twitter(urls_TW))
    df_TW['Seguidores'] = df_TW['Seguidores'].apply(convertir_a_numero)
    df_TW['Siguiendo'] = df_TW['Siguiendo'].apply(convertir_a_numero)
    df_TW['Posts'] = df_TW['Posts'].apply(convertir_a_numero)
    print(df_TW.head())
        
    df_YT = pd.DataFrame(Scraping_Youtube(urls_YT))
    df_YT['Subscripciones'] = df_YT['Subscripciones'].apply(convertir_a_numero)
    df_YT['Videos'] = df_YT['Videos'].apply(convertir_a_numero)
    print(df_YT.head())
    
    df_IG = pd.DataFrame(Scraping_Instagram(urls_IG))
    df_IG['Seguidores'] = df_IG['Seguidores'].apply(convertir_a_numero)
    df_IG['Seguidos'] = df_IG['Seguidos'].apply(convertir_a_numero)
    df_IG['Publicaciones'] = df_IG['Publicaciones'].apply(convertir_a_numero)
    print(df_IG.head())
        
    df_FB = pd.DataFrame(Scraping_Facebook(urls_FB))
    df_FB['Seguidores'] = df_FB['Seguidores'].apply(convertir_a_numero)
    df_FB['Me Gusta'] = df_FB['Me Gusta'].apply(convertir_a_numero)    
    print(df_FB.head())
    
    # Crear un ExcelWriter con el nombre del archivo Excel
    with pd.ExcelWriter('./Redes-Sociales.xlsx', engine='openpyxl') as writer:
        # Guardar cada DataFrame en una hoja diferente
        df_FB.to_excel(writer, sheet_name='Facebook', index=False)
        df_IG.to_excel(writer, sheet_name='Instagram', index=False)
        df_YT.to_excel(writer, sheet_name='Youtube', index=False)
        df_TW.to_excel(writer, sheet_name='Twitter', index=False)
        df_TIK.to_excel(writer, sheet_name='TikTok', index=False)

    print("DataFrames guardados en diferentes hojas de Excel exitosamente.")
    
    
urls_FB = ['https://www.facebook.com/PandoraEspana/', 'https://www.facebook.com/tousjewelry', 'https://www.facebook.com/AristocrazySpain/'] 
urls_IG = ['https://www.instagram.com/theofficialpandora/', 'https://www.instagram.com/tousjewelry/', 'https://www.instagram.com/aristocrazy/'] 
urls_TIK = ['https://www.tiktok.com/@theofficialpandor', 'https://www.tiktok.com/@tousjewelry']
urls_TW = ['https://twitter.com/PANDORA_Corp', 'https://twitter.com/tousjewelry']
urls_YT = ['https://www.youtube.com/user/TheOfficialPandora', 'https://www.youtube.com/user/tousjewelry', 'https://www.youtube.com/@MrBeast']

Run_All()