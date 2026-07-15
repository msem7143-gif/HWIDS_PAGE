import json
import requests
from datetime import datetime , timezone
from helper import KEY_CHECKER , HWID_REGISTER
import random
import base64


def Key_Encoder(HWID:str , KEY:str):
    LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    ENCRYPTED = ""
    HWID = HWID[::-1]
    KEY  = KEY[::-1]
    for i in range(len(HWID)):
        Random =""
        for x in range(3):
            Random += random.choice(LIST) #Üstteki alfabe listesinden 3 tane rastgele harf seçiyor

        if i < len(KEY):
            ENCRYPTED += str(base64.b64encode(str(ord(HWID[i])).encode("ascii"))).split("'")[1]  +   "=_"   +str(base64.b64encode(str(ord(KEY[i])).encode("ascii"))).split("'")[1] + "_=" + Random + "=__"
        elif i>= len(KEY):
            ENCRYPTED += str(base64.b64encode(str(ord(HWID[i])).encode("ascii"))).split("'")[1]  +   "=_"   +str(base64.b64encode(str(ord('_')).encode("ascii"))).split("'")[1] + "_=" + Random + "=__"

        " ^^HWID VE KEY'deki karakterleri ASCII değerine çevirip base64'e uygun olması için 'encode(ascii)' kullanıyor, base64 'byte' formatında encodeliyor; sonra 'str'ye çevirip byte formatından kalan izleri 'split' ile temizliyoruz"
        
    return ENCRYPTED








KEY  = "26W8FQ4X-YIVZ-EG8J-APEXATM"
HWID = "AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA"
 
KEYS_PAGE = requests.get("https://keytest31.netlify.app").text
KEYS_JSON = json.loads(KEYS_PAGE)





TYPE = KEY_CHECKER(KEYS_JSON , KEY)

print(TYPE)


if TYPE :
    print("ye")
    KEYS_PAGE = KEYS_PAGE.replace(KEY, f"-USED KEY || TIME: {str(datetime.now(timezone.utc)).split('.')[0]}")#Kullanılan keyi sayfada "-USED KEY-" ile değiştiriyoruz. Buraya hangi keyin used olduğu bilgisini eklemenin bir gereği yok bence zaten discordda görücez 2 Ayrı @everyone postuyla hangi key ile register olduğunu




    HWIDS_PAGE = requests.get("https://keytest31.netlify.app").text
    HWIDS_JSON = json.loads(HWIDS_PAGE)


    ENCRYPTED_KEY = Key_Encoder(HWID,KEY)


    TOKEN = HWID_REGISTER(TYPE , ENCRYPTED_KEY)

##    print(TOKEN , "\n\n\n")






from dhooks import Webhook, File


def LOGGERR():

    hook = Webhook('https://discord.com/api/webhooks/1112865938409263194/cS5Lwc89d14Qx2RHy88uvOzRuKX5zB5AHiA5NnKeNiG2-UwRzrI9sfk1Q6r9JaYDbf-0')

    file = File('AFFILIATE\index.html', name='RESELLER_PAGE.html')  # optional name for discord

    hook.send(str(datetime.now(timezone.utc)).split(".")[0][-2], file=file)



LOGGERR()







####    from cryptography.fernet import Fernet
####    key = b'QEVnNNCUXbGmYHjV-1-CAO1q-w6eX_qimZH8Mrf9-9w='   
####    f = Fernet(key)
####    Decrypted = f.decrypt(TOKEN)
####
####
####    """print(   str(Decrypted).split("++")[0].split("'")[1] )"""
####    """print(   str(Decrypted).split("++")[1].split("'")[0] )"""










