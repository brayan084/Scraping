import pandas as pd


from Facebook import Scraping_Facebook
from Twitter import Scraping_Twitter
from Youtube import Scraping_Youtube
from Instagram import Scraping_Instagram
from TicTok import Scraping_TikTok

def Run_All():
    
    df_FB = pd.DataFrame(Scraping_Facebook(urls_FB))
    # df_FB.to_excel('Data_Facebook.xlsx')
    df_IG = pd.DataFrame(Scraping_Instagram(urls_IG))
    df_YT = pd.DataFrame(Scraping_Youtube(urls_YT))
    df_TW = pd.DataFrame(Scraping_Twitter(urls_TW))
    df_TIK = pd.DataFrame(Scraping_TikTok(urls_TIK))
    
        # Crear un ExcelWriter con el nombre del archivo Excel
    with pd.ExcelWriter('./Redes-Sociales.xlsx', engine='openpyxl') as writer:
        # Guardar cada DataFrame en una hoja diferente
        df_FB.to_excel(writer, sheet_name='Facebook', index=False)
        df_IG.to_excel(writer, sheet_name='Instagram', index=False)
        df_YT.to_excel(writer, sheet_name='Youtube', index=False)
        df_TW.to_excel(writer, sheet_name='Twitter', index=False)
        df_TIK.to_excel(writer, sheet_name='TikTok', index=False)

    print("DataFrames guardados en diferentes hojas de Excel exitosamente.")
    
    
urls_FB = ['https://www.facebook.com/PandoraEspana/', 'https://www.facebook.com/tousjewelry'] 
urls_IG = ['https://www.instagram.com/theofficialpandora/', 'https://www.instagram.com/tousjewelry/'] 
urls_TIK = ['https://www.tiktok.com/@theofficialpandor', 'https://www.tiktok.com/@tousjewelry']
urls_TW = ['https://twitter.com/PANDORA_Corp', 'https://twitter.com/tousjewelry']
urls_YT = ['https://www.youtube.com/user/TheOfficialPandora', 'https://www.youtube.com/user/tousjewelry']

Run_All()