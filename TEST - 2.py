import json
import requests
from datetime import datetime , timezone
from helper import KEY_CHECKER , HWID_REGISTER 
import random
import base64


from helper import ENCRYPT_RESELLER_PAGE , DECRYPT_RESELLER_PAGE
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











RESELLER_PAGE = requests.get("https://resselllersspage.netlify.app").text
try:
    RESELLER_PAGE = ((RESELLER_PAGE).split("<body>")[1].split("</body>")[0])
except:
    pass




RESELLER_PAGE = DECRYPT_RESELLER_PAGE(RESELLER_PAGE)
##print(RESELLER_PAGE)

#RESELLER_PAGE = ENCRYPT_RESELLER_PAGE(RESELLER_PAGE)


##print(RESELLER_PAGE)

with open("test.txt", "w") as lemon:
    lemon.write(str(RESELLER_PAGE))
##RESELLER_PAGE = DECRYPT_RESELLER_PAGE( RESELLER_PAGE )  #<---| SAYFADAN GELEN TEXTİ DECRYPE EDİYOR  







####    from cryptography.fernet import Fernet
####    key = b'QEVnNNCUXbGmYHjV-1-CAO1q-w6eX_qimZH8Mrf9-9w='   
####    f = Fernet(key)
####    Decrypted = f.decrypt(TOKEN)
####
####
####    """print(   str(Decrypted).split("++")[0].split("'")[1] )"""
####    """print(   str(Decrypted).split("++")[1].split("'")[0] )"""














aaa = """
{

"RESELLERS":[]
}

"""




##print("\n\n\n")
##print(ENCRYPT_RESELLER_PAGE(aaa))



#########################################3


from cryptography.fernet import Fernet
import re
import time

def DECRYPT_HWID(HWID_ENCRYPTED:str):
    "HWID Pageindeki Hwidleri incelemek için Decryptler"



    key = b'QEVnNNCUXbGmYHjV-1-CAO1q-w6eX_qimZH8Mrf9-9w='
    f = Fernet(key)

    try:
        HWID_ENCRYPTED = HWID_ENCRYPTED.split("'")[1]   #<---| Sayfadan str olarak indiği için geri Byte formuna çeviriyoruz
    except:
        pass

    HWID_ENCRYPTED = HWID_ENCRYPTED.encode('utf-8')
    HWID_DECRYPTED_0 = f.decrypt(HWID_ENCRYPTED)
    HWID_DECRYPTED_0 = str(HWID_DECRYPTED_0).split("'")[1] #<----| Yeniden Byte formundan String formuna çevirdik

    
    ENCRYPTED_KEY = HWID_DECRYPTED_0.split("++")[0] #<----| Base64 partını Time/Epoch partından ayırdık


    ENCRYPTED_KEY = re.split("_=|=__" , ENCRYPTED_KEY) 
    real_s3 = []
    for x in range(len(ENCRYPTED_KEY)):
        if x%2 ==0:
            real_s3.append(ENCRYPTED_KEY[x])
    del real_s3[-1]


    KEY=""
    for x in range (len(real_s3)):
        KEY += chr(int(str(base64.b64decode(real_s3[x].split("=_")[1].encode("ascii"))).split("'")[1]))
    KEY = KEY[::-1]


    HWID=""
    for x in range (len(real_s3)):
        HWID += chr(int(str(base64.b64decode(real_s3[x].split("=_")[0].encode("ascii"))).split("'")[1]))
    HWID = HWID[::-1]


    if not ("LIFETIME" in HWID_DECRYPTED_0.split("++")[1]):
        KEY_DEADLINE = int(HWID_DECRYPTED_0.split("++")[1]) #<----| Time/Epoch partını Base64 partından ayırdık
    else:
        KEY_DEADLINE = "LIFETIME"


    return HWID , KEY , KEY_DEADLINE





def HWID_REGISTER(TYPE:str , ENCRYPTED_KEY:str):

    Epoch = int(time.time())

    if (TYPE == "APEXATM") or (TYPE == "APEXSTM") or (TYPE == "RUSTSTM") or (TYPE == "SOTCTM") or (TYPE == "APEXBNDTM") :
        ADD_Time = 24*3600*30
        TIME = str(Epoch + ADD_Time)

    elif (TYPE == "APEXATW") or (TYPE == "APEXSTW") or (TYPE == "RUSTSTW") or (TYPE == "SOTCTW") :
        ADD_Time = 24*3600*7
        TIME = str(Epoch + ADD_Time)

    elif (TYPE == "APEXAL") or (TYPE == "APEXSL") or (TYPE == "RUSTSL") or (TYPE == "APEXBNDL")  :
        TIME = 'LIFETIME'


    
    REGISTERY = ENCRYPTED_KEY + "++" + TIME


    
    key = b'QEVnNNCUXbGmYHjV-1-CAO1q-w6eX_qimZH8Mrf9-9w='
    f = Fernet(key)

    TOKEN = f.encrypt(REGISTERY.encode('utf-8'))


    return str(TOKEN)







HWIDS_PAGE = requests.get("https://realhworrdss.netlify.app").text
try:
    HWIDS_PAGE = (HWIDS_PAGE).split("<body>")[1].split("</body>")[0]
except:
    pass

HWIDS_JSON = json.loads(HWIDS_PAGE)

print(len(HWIDS_JSON.get("RUSTSL")))



for X in range(len(HWIDS_JSON.get("RUSTSL"))):
    #print(DECRYPT_HWID(HWIDS_JSON[X]))
    print(X)     
    if DECRYPT_HWID(HWIDS_JSON.get("RUSTSL")[X])[1]=="___________V6AC0NKO-4RAR-5OAX-RUSTSL":
        print(HWIDS_JSON.get("RUSTSL")[X])
        
        

ENCRYPTED_KEY = Key_Encoder("2F3711D3-01D6-AE0C-C0E9-581122CCF416" , "V6AC0NKO-4RAR-5OAX-RUSTSL")


REGISTERED_HIWD = HWID_REGISTER( "RUSTSL", ENCRYPTED_KEY)

print(REGISTERED_HIWD)

HWIDS_JSON.get("RUSTSL")[24] = REGISTERED_HIWD

HWIDS_JSON = str(HWIDS_JSON).replace("'APEXAL'", '"APEXAL"').replace("'APEXATM'", '"APEXATM"').replace("'APEXATW'", '"APEXATW"').replace("'APEXSL'", '"APEXSL"').replace("'APEXSTM'", '"APEXSTM"').replace("'APEXSTW'", '"APEXSTW"').replace("'RUSTSL'", '"RUSTSL"').replace("'RUSTSTM'", '"RUSTSTM"').replace("'RUSTSTW'", '"RUSTSTW"').replace("'SOTCTM'", '"SOTCTM"').replace("'SOTCTW'", '"SOTCTW"').replace("'APEXBNDL'", '"APEXBNDL"').replace("'APEXBNDTM'", '"APEXBNDTM"')

with open(r'HWIDS_PAGE/index.html', 'w') as file:    
    file.write( HWIDS_JSON )


    
