import requests
import json
import os
import time
import random
import base64
import re
from datetime import datetime,timezone
from dhooks import Webhook, File
from cryptography.fernet import Fernet




            
def KEY_CHECKER(KEYS_JSON:dict , KEY:str ):

    

    if "APEXAL" in KEY :                   #<---| APEX AIM LIFETIME
        for X in KEYS_JSON.get("APEXAL"):
            if X == KEY:
                return "APEXAL"
        return False


    elif  "APEXATM" in KEY :                #<---| APEX AIM TIMED MONTHLY
        for X in KEYS_JSON.get("APEXATM"):
            if X == KEY:
                return "APEXATM"
        return False


    elif  "APEXATW" in KEY :                #<---| APEX AIM TIMED WEEKLY
        for X in KEYS_JSON.get("APEXATW"):
            if X == KEY:
                return "APEXATW"
        return False






    elif  "APEXSL" in KEY :                #<---| APEX SCRIPT LIFETIME
        for X in KEYS_JSON.get("APEXSL"):
            if X == KEY:
                return "APEXSL"
        return False


    elif  "APEXSTM" in KEY :                #<---| APEX SCRIPT TIMED MONTHLY
        for X in KEYS_JSON.get("APEXSTM"):
            if X == KEY:
                return "APEXSTM"
        return False


    elif  "APEXSTW" in KEY :                #<---| APEX SCRIPT TIMED WEEKLYY
        for X in KEYS_JSON.get("APEXSTW"):
            if X == KEY:
                return "APEXSTW"
        return False


    elif  "APEXBNDL" in KEY :                #<---| APEX BUNDLE LIFETIME
        for X in KEYS_JSON.get("APEXBNDL"):
            if X == KEY:
                return "APEXBNDL"
        return False


    elif  "APEXBNDTM" in KEY :                #<---| APEX BUNDLE TIMED MONTHLY
        for X in KEYS_JSON.get("APEXBNDTM"):
            if X == KEY:
                return "APEXBNDTM"
        return False






    elif  "RUSTSL" in KEY :                #<---| RUST SCRIPT LIFETIME
        for X in KEYS_JSON.get("RUSTSL"):
            if X == KEY:
                return "RUSTSL"
        return False

    elif  "RUSTSTM" in KEY :                #<---| RUST SCRIPT TIMED MONTHLY
        for X in KEYS_JSON.get("RUSTSTM"):
            if X == KEY:
                return "RUSTSTM"
        return False


    elif  "RUSTSTW" in KEY :                #<---| RUST SCRIPT TIMED WEEKLY
        for X in KEYS_JSON.get("RUSTSTW"):
            if X == KEY:
                return "RUSTSTW"
        return False





    elif  "RUSTFBL" in KEY :                #<---| RUST Fishing BOT LIFETIME
        for X in KEYS_JSON.get("RUSTFBL"):
            if X == KEY:
                return "RUSTFBL"
        return False

    elif  "RUSTFBTM" in KEY :                #<---| RUST Fishing BOT TIMED MONTHLY
        for X in KEYS_JSON.get("RUSTFBTM"):
            if X == KEY:
                return "RUSTFBTM"
        return False


    elif  "RUSTFBTW" in KEY :                #<---| RUST Fishing BOT TIMED WEEKLY
        for X in KEYS_JSON.get("RUSTFBTW"):
            if X == KEY:
                return "RUSTFBTW"
        return False





    elif  "RUSTCDRL" in KEY :                #<---| RUST Code Raider LIFETIME
        for X in KEYS_JSON.get("RUSTCDRL"):
            if X == KEY:
                return "RUSTCDRL"
        return False

    elif  "RUSTCDRTM" in KEY :                #<---| RUST Code Raider TIMED MONTHLY
        for X in KEYS_JSON.get("RUSTCDRTM"):
            if X == KEY:
                return "RUSTCDRTM"
        return False


    elif  "RUSTCDRTW" in KEY :                #<---| RUST Code Raider TIMED WEEKLY
        for X in KEYS_JSON.get("RUSTCDRTW"):
            if X == KEY:
                return "RUSTCDRTW"
        return False





    elif  "SOTCTM" in KEY :                #<---| SOT CHEAT TIMED MONTHLY
        for X in KEYS_JSON.get("SOTCTM"):
            if X == KEY:
                return "SOTCTM"
        return False


    elif  "SOTCTW" in KEY :                #<---| SOT CHEAT TIMED WEEKLY
        for X in KEYS_JSON.get("SOTCTW"):
            if X == KEY:
                return "SOTCTW"
        return False

    

    else:
        return False #<---| Scriptlerin içinde de Key-Request göndermeden önce bu checker'dan var








##"NTY==_NDk=_=CXH=__Njk==_NTc=_=XFZ=__NTI==_Njg=_=RDX=__NTQ==_NjY=_=LBI=__NTU==_NDU=_=OHS=__NTI==_NTA=_=BDR=__NTc==_NDk=_=VQR=__Njc==_NjY=_=IJZ=__NDg==_NTI=_=VUQ=__NDk==_NDU=_=KMJ=__Njc==_NTc=_=MFB=__NTU==_NTY=_=WDZ=__NDU==_NTM=_=FCT=__NjU==_NTU=_=BZA=__NTQ==_NDU=_=DLL=__NjU==_NTY=_=DUU=__NTQ==_NjU=_=XYP=__NDU==_NTE=_=TRL=__NTM==_NTM=_=ZEE=__NTA==_NzA=_=EEW=__NTQ==_NTA=_=VUL=__NTE==_Njg=_=ECR=__NDU==_NTI=_=MZR=__Njc==_OTU=_=OGQ=__NzA==_OTU=_=WJG=__NTc==_OTU=_=YZS=__NTM==_OTU=_=PYR=__NDU==_OTU=_=QMQ=__NjU==_OTU=_=MED=__NDk==_OTU=_=FRS=__NDk==_OTU=_=FYM=__NTY==_OTU=_=PRH=__NjU==_OTU=_=XOD=__NTc==_OTU=_=HND=__NTA==_OTU=_=SEE=__Njc==_OTU=_=KIX=__  || 
    

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







def HWID_REGISTER(TYPE:str , ENCRYPTED_KEY:str):

    Epoch = int(time.time())

    if (TYPE == "APEXATM") or (TYPE == "APEXSTM") or (TYPE == "RUSTSTM") or (TYPE == "RUSTFBTM") or (TYPE == "RUSTCDRTM") or (TYPE == "SOTCTM") or (TYPE == "APEXBNDTM") :
        ADD_Time = 24*3600*30
        TIME = str(Epoch + ADD_Time)

    elif (TYPE == "APEXATW") or (TYPE == "APEXSTW") or (TYPE == "RUSTSTW") or (TYPE == "RUSTFBTW") or (TYPE == "RUSTCDRTW") or (TYPE == "SOTCTW") :
        ADD_Time = 24*3600*7
        TIME = str(Epoch + ADD_Time)

    elif (TYPE == "APEXAL") or (TYPE == "APEXSL") or (TYPE == "RUSTSL") or (TYPE == "APEXBNDL")  or (TYPE == "RUSTFBL") or (TYPE == "RUSTCDRL")  :
        TIME = 'LIFETIME'


    
    REGISTERY = ENCRYPTED_KEY + "++" + TIME


    
    key = b'QEVnNNCUXbGmYHjV-1-CAO1q-w6eX_qimZH8Mrf9-9w='
    f = Fernet(key)

    TOKEN = f.encrypt(REGISTERY.encode('utf-8'))


    return str(TOKEN)




    



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






    


def DECRYPT_RESELLER_PAGE( RESELLER_PAGE:str ):
    try:
        RESELLER_PAGE = RESELLER_PAGE.split("'")[1]   #<---| Sayfadan str olarak indiği için geri Byte formuna çeviriyoruz
    except:
        pass
    
    RESELLER_PAGE = RESELLER_PAGE.encode('utf-8')
    

    key = b'YhK1GzHsBMBuCS9_jOCzqIsrKay8qLkOaCtGFd7RSwQ='
    f = Fernet(key)
    RESELLER_PAGE_DECRYPT = f.decrypt(RESELLER_PAGE) #<---| Önce Fernet decrypt edilir// sonra Base64



    RESELLER_PAGE_DECRYPT = str(RESELLER_PAGE_DECRYPT).split("'")[1] #<----| Alttaki Base64 Decryption için Byte'dan STR formatına çeviriyoruz




    Decrypt_list = re.split("_=|=__" , RESELLER_PAGE_DECRYPT)

    real_s3 = []
    for x in range (len(Decrypt_list)):
        if x%2 ==0:
            real_s3.append(Decrypt_list[x])   

    del real_s3[-1]

    Decrypted_Body=""
    for x in range (len(real_s3)):
        Decrypted_Body += chr(int(str(base64.b64decode(real_s3[x].encode("ascii"))).split("'")[1]))

    Decrypted_Body = Decrypted_Body[::-1]

    return Decrypted_Body






def ENCRYPT_RESELLER_PAGE(RESELLER_PAGE:str):
    LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']   

    #### Encrypting the data back after replacing the used key with buyer information ↓↓↓↓↓
    #try:
    #    RESELLER_PAGE = str(RESELLER_PAGE).split("'")[1]
    #except:
    #    pass
        

    data=RESELLER_PAGE[::-1]
    Encrypt_list=""
    for x in data:
        Random =""
        for y in range(3):
            Random += random.choice(LIST)                                 
        Encrypt_list+= str(base64.b64encode(str(ord(x)).encode("ascii"))).split("'")[1] + "_=" + Random + "=__"



    key = b'YhK1GzHsBMBuCS9_jOCzqIsrKay8qLkOaCtGFd7RSwQ='
    f = Fernet(key)

    RESELLER_PAGE_ENCRYPTED = f.encrypt(Encrypt_list.encode('utf-8'))

    return RESELLER_PAGE_ENCRYPTED

    







def KEY_CREATOR( APP_NAME :str ) -> str :
    LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0']

    KEY = ""
    for x in range(8):
        KEY += random.choice(LIST)

    KEY += "-"

    for x in range(4):
        KEY += random.choice(LIST)

    KEY += "-"

    for x in range(4):    
        KEY += random.choice(LIST)

    KEY += "-"

    KEY += APP_NAME

    return KEY
    



def RESELLER_PAGE_LOAD(): #<-----| Load resellerPage from Txt instead of Web, This way Even if websites not updated after 20 seconds; it keeps last changes
    
    if os.path.isfile(r'RESELLER_PAGE/index.html'):
        print("Reseller Page Hazır olanı kullanıyorum")
        with open(r'RESELLER_PAGE/index.html', 'r') as file:
            RESELLER_PAGE = str(file.readlines())


    else:
        print("Webe Gidiyorum")
        RESELLER_PAGE = requests.get("https://superlative-gecko-db063d.netlify.app").text
        try:
            RESELLER_PAGE = ((RESELLER_PAGE).split("<body>")[1].split("</body>")[0])
        except:
            pass

    return RESELLER_PAGE






def KEYS_PAGE_LOAD(): #<-----| Load KeysPage from Txt instead of Web, This way Even if websites not updated after 20 seconds; it keeps last changes
    
    if os.path.isfile(r'KEYS_PAGE/index.html'):
        print("Keys Page Hazır olanı kullanıyorum")
        with open(r'KEYS_PAGE/index.html', 'r') as file:
            KEYS_PAGE = str(file.readlines()).split("'")[1]


    else:
        print("Webe Gidiyorum")
        KEYS_PAGE = requests.get("https://zesty-axolotl-30435b.netlify.app").text
        try:
            KEYS_PAGE = (KEYS_PAGE).split("<body>")[1].split("</body>")[0]
        except:
            pass

    print((KEYS_PAGE))
    
    return str(KEYS_PAGE)





def HWID_PAGE_LOAD(): #<-----| Load KeysPage from Txt instead of Web, This way Even if websites not updated after 20 seconds; it keeps last changes
    
    if os.path.isfile(r'HWIDS_PAGE/index.html'):
        print("HWIDS_PAGE Page Hazır olanı kullanıyorum")
        with open(r'HWIDS_PAGE/index.html', 'r') as file:
            HWIDS_PAGE = str(file.readlines()[0])


    else:
        print("Webe Gidiyorum")
        HWIDS_PAGE = requests.get("https://jovial-youtiao-c70a95.netlify.app").text
        try:
            HWIDS_PAGE = (HWIDS_PAGE).split("<body>")[1].split("</body>")[0]
        except:
            pass

    print(HWIDS_PAGE)
    
    return str(HWIDS_PAGE)









def LOGGER(LOG_REASON , RESELLER_PAGE , HWIDS_PAGE , KES_PAGE):

    hook = Webhook('https://discord.com/api/webhooks/1112865938409263194/cS5Lwc89d14Qx2RHy88uvOzRuKX5zB5AHiA5NnKeNiG2-UwRzrI9sfk1Q6r9JaYDbf-0')

    hook.send("\n\n~~||--------------------------------------------------------------------||~~\n> ## **`LOG_REASON:`** " + "`" + LOG_REASON + "`")

    if RESELLER_PAGE:
        file = File('RESELLER_PAGE\index.html', name='RESELLER_PAGE')  
        hook.send('## `RESELLER_PAGE ' + str(datetime.now(timezone.utc)).split(".")[0][0:16] + "`"  , file=file)


    if KES_PAGE:
        file = File('KEYS_PAGE\index.html', name='KEYS_PAGE')  
        hook.send('## `KEYS_PAGE ' + str(datetime.now(timezone.utc)).split(".")[0][0:16] + "`" , file=file)

    if HWIDS_PAGE:
        file = File('HWIDS_PAGE\index.html', name='HWIDS_PAGE')  
        hook.send('## `HWIDS_PAGE ' + str(datetime.now(timezone.utc)).split(".")[0][0:16] + "`" , file=file)

    hook.send("‎ \n‎ \n‎ \n‎ ")






##TT = "asd"
##
##
##from cryptography.fernet import Fernet
##key = b'YhK1GzHsBMBuCS9_jOCzqIsrKay8qLkOaCtGFd7RSwQ='     #key = Fernet.generate_key()
##key = Fernet.generate_key()
##
##print(key)

##print(key)
##
##f = Fernet(key)
##
##
##token = b'gAAAAABkIu73CwdYZCn1ReyyNTX9Cul1F89UY9EoL_LngfVQ3d5jF_o2Imnahb4pop2r2nAM2hO-9dSWwqAQOmsJDZSaE78HXw==' #f.encrypt(TT.encode('utf-8'))
##
##print(token)
##
##Decrypted = f.decrypt(token)
##
##
##
##print(str(Decrypted).split("'")[1])
##

