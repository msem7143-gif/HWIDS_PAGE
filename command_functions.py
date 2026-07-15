from dhooks import Webhook, Embed
from cryptography.fernet import Fernet
import time
from helper import DECRYPT_HWID , KEY_CREATOR


def DISPLAY_KEY_COUNT(KEYS_PAGE:dict):
    "Displays amount of already used keys and keys that are waiting to be purchased // for each prrogram/script/cheat"


    ######## APEX AIMBOT KEYS ########

    APEXAL_USED = []
    APEXAL      = []
    for X in KEYS_PAGE.get("APEXAL"):
        
        if "USED KEY" in X :
            APEXAL_USED.append(X)
        else:
            APEXAL.append(X)


    APEXATM_USED = []
    APEXATM      = []
    for X in KEYS_PAGE.get("APEXATM"):
        if "USED KEY" in X :
            APEXATM_USED.append(X)
        else:
            APEXATM.append(X)

            
    APEXATW_USED = []
    APEXATW      = []
    for X in KEYS_PAGE.get("APEXATW"):
        if "USED KEY" in X :
            APEXATW_USED.append(X)
        else:
            APEXATW.append(X)


    
    ######## APEX SCRIPT KEYS ########



    APEXSL_USED = []
    APEXSL      = []
    for X in KEYS_PAGE.get("APEXSL"):
        
        if "USED KEY" in X :
            APEXSL_USED.append(X)
        else:
            APEXSL.append(X)
            

    APEXSTM_USED = []
    APEXSTM      = []
    for X in KEYS_PAGE.get("APEXSTM"):
        
        if "USED KEY" in X :
            APEXSTM_USED.append(X)
        else:
            APEXSTM.append(X)


    
    APEXSTW_USED = []
    APEXSTW      = []
    for X in KEYS_PAGE.get("APEXSTW"):
        
        if "USED KEY" in X :
            APEXSTW_USED.append(X)
        else:
            APEXSTW.append(X)


    ######## RUST SCRIPT KEYS ########


    RUSTSL_USED = []
    RUSTSL      = []
    for X in KEYS_PAGE.get("RUSTSL"):
        
        if "USED KEY" in X :
            RUSTSL_USED.append(X)
        else:
            RUSTSL.append(X)


    RUSTSTM_USED = []
    RUSTSTM      = []
    for X in KEYS_PAGE.get("RUSTSTM"):
        
        if "USED KEY" in X :
            RUSTSTM_USED.append(X)
        else:
            RUSTSTM.append(X)


    RUSTSTW_USED = []
    RUSTSTW      = []
    for X in KEYS_PAGE.get("RUSTSTW"):
        
        if "USED KEY" in X :
            RUSTSTW_USED.append(X)
        else:
            RUSTSTW.append(X)


    ######## RUST CHEAT KEYS ########


    SOTCTM_USED = []
    SOTCTM      = []
    for X in KEYS_PAGE.get("SOTCTM"):
        
        if "USED KEY" in X :
            SOTCTM_USED.append(X)
        else:
            SOTCTM.append(X)


    SOTCTW_USED = []
    SOTCTW      = []
    for X in KEYS_PAGE.get("SOTCTW"):
        
        if "USED KEY" in X :
            SOTCTW_USED.append(X)
        else:
            SOTCTW.append(X)


    #################################





    from dhooks import Webhook, Embed

    hook = Webhook('https://discord.com/api/webhooks/1091108019573637130/7KUt-4Xw6EQPUiR9K51nfKWS1I35OqxdBposKAndD8dk2AKbL0EYbDCUnzbTKP7rxnxl')

    embed = Embed(
        description=f"———————————————————————————————————\n ‎ 𝗣𝗥𝗢𝗚𝗥𝗔𝗠‎‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗞𝗲𝘆𝘀‎  ‎ ‎‎ ‎ ‎ ‎ ㅤ‎ 𝗨𝘀𝗲𝗱 𝗞𝗲𝘆𝘀ㅤㅤ\n———————————————————————————————————\n\n ‎ `APEX SCRIPT LIFETIME             {len(APEXSL)}                {len(APEXSL_USED)}       `\n ‎ `APEX SCRIPT MONTHLY              {len(APEXSTM)}                {len(APEXSTM_USED)}       `\n‎  `APEX SCRIPT WEEKLY               {len(APEXSTW)}                {len(APEXSTW_USED)}       `\n\n‎  `APEX AIMBOT LIFETIME             {len(APEXAL)}                {len(APEXAL_USED)}       `\n‎  `APEX AIMBOT MONTHLY              {len(APEXATM)}                {len(APEXATM_USED)}       `\n ‎ `APEX AIMBOT WEEKLY               {len(APEXATW)}                {len(APEXATW_USED)}       `             \n\n‎  `RUST SCRIPT LIFETIME             {len(RUSTSL)}                {len(RUSTSL_USED)}       `                                       \n ‎ `RUST SCRIPT MONTHLY              {len(RUSTSTM)}                {len(RUSTSTM_USED)}       `                                      \n ‎ `RUST SCRIPT WEEKLY               {len(RUSTSTW)}                {len(RUSTSTW_USED)}       `                                      \n\n ‎ `SOT CHEAT MONTHLY                {len(SOTCTM)}                {len(SOTCTM_USED)}       `                                        \n ‎ `SOT CHEAT WEEKLY                 {len(SOTCTW)}                {len(SOTCTW_USED)}       `                                   \n\n———————————————————————————————————",


        color=0x000000,

        )



    hook.send(content="" , embed=embed)


















##def ACTIVE_KEYS(HWIDS_PAGE:dict , Message:str):
##
##    Epoch = int(time.time())
##
##    key = b'QEVnNNCUXbGmYHjV-1-CAO1q-w6eX_qimZH8Mrf9-9w='
##    f = Fernet(key)
##
##
##    if "ALL" in Message:
##
##    else:
##        Message.split("active")[1]
##        
##
##    APEXSTM_INACTIVE = []  
##    APEXSTM_ACTIVE   = []
##
##
##    
##    for X in HWIDS_PAGE.get("APEXSTM"):
##
##        HWID , KEY , KEY_DEADLINE = DECRYPT_HWID(X)
##
##
##        if not (KEY_DEADLINE == "LIFETIME"):
##            
##            if (KEY_DEADLINE-Epoch) <= 0:
##                APEXSTM_INACTIVE.append({"HWID":HWID , "KEY":KEY , "TIME": (KEY_DEADLINE-Epoch)/(24*3600)})
##
##            else:
##                APEXSTM_ACTIVE.append({"HWID":HWID , "KEY":KEY , "TIME": (KEY_DEADLINE-Epoch)/(24*3600)})




            
        






            

        
            

def KEY_ADDER( MESSAGE:str , RESELLER_PAGE:dict):

    KEY_TYPE   = MESSAGE.split("keytype[")[1].split("]")[0].replace(" ", "")
    KEY_AMOUNT = int(MESSAGE.split("amount[")[1].split("]")[0])

    RESELLER_NAME = MESSAGE.split("resellername[")[1].split("]")[0]
    RESELLER_HWID = MESSAGE.split("resellerhwid[")[1].split("]")[0]

    if not (KEY_TYPE in "APEXSL APEXSTM APEXSTW APEXAL APEXATM APEXATW APEXBNDL APEXBNDTM RUSTSL RUSTSTM RUSTSTW RUSTFBL RUSTFBTM RUSTFBTW RUSTCDRL RUSTCDRTM RUSTCDRTW SOTCTM SOTCTW"):
        return (False , "Invalid Key-Type" , False , False)
        
    
        
    FOUND_RESELLER = (False , None)
    for X in range(len(RESELLER_PAGE.get("RESELLERS"))):
        
        if (RESELLER_PAGE.get("RESELLERS")[X].get("RESELLER_HWID") == RESELLER_HWID) and (RESELLER_PAGE.get("RESELLERS")[X].get("DISCORD_NAME") == RESELLER_NAME) :
            FOUND_RESELLER = (True , X)
        


    if not FOUND_RESELLER[0]:
        return (False , "Not-Found" , False , False)

    else:
        ADD_KEYS_LIST = []
        for Y in range(KEY_AMOUNT):
            ADD_KEYS_LIST.append( KEY_CREATOR(KEY_TYPE) )


        for Z in ADD_KEYS_LIST:
            RESELLER_PAGE.get("RESELLERS")[FOUND_RESELLER[1]][KEY_TYPE].append(Z)



        return (RESELLER_PAGE , ADD_KEYS_LIST , KEY_TYPE , RESELLER_NAME)


        






def RESELLER_REGISTERER( MESSAGE:str , RESELLER_PAGE:dict ):
    
    RESELLER_NAME = MESSAGE.split("resellername[")[1].split("]")[0]
    RESELLER_HWID = MESSAGE.split("resellerhwid[")[1].split("]")[0]
    RESELLER_DISK_SERIAL = MESSAGE.split("resellerdisk_serial[")[1].split("]")[0]

    if ('"' in RESELLER_NAME) or ('"' in RESELLER_HWID):
        return (False , "Invalid-Characters")

    for X in range(len(RESELLER_PAGE.get("RESELLERS"))):
        
        if (RESELLER_PAGE.get("RESELLERS")[X].get("RESELLER_HWID") == RESELLER_HWID) and (RESELLER_PAGE.get("RESELLERS")[X].get("DISCORD_NAME") == RESELLER_NAME) :
            return (False , "Already-Exist")



    NEW_RESELLER = { "RESELLER_HWID":RESELLER_HWID ,
                     "DISCORD_NAME":RESELLER_NAME ,
                     "RESELLER_DISK_SERIAL":RESELLER_DISK_SERIAL,

                     "APEXAL"  : [],
                     "APEXATM" : [] ,
                     "APEXATW" : [] ,

                     "APEXSL"  : [] ,
                     "APEXSTM" : [] ,
                     "APEXSTW" : [] ,

                     "APEXBNDTM" : [] ,
                     "APEXBNDL"  : [] ,

                     "RUSTSL"  : [] ,
                     "RUSTSTM" : [] ,
                     "RUSTSTW" : [] ,

                     "RUSTFBL"   : [] ,
                     "RUSTFBTM"  : [] ,
                     "RUSTFBTW"  : [] ,

                     "RUSTCDRL"  : [] ,
                     "RUSTCDRTM" : [] ,
                     "RUSTCDRTW" : [] ,


                     "SOTCTM"  : [],
                     "SOTCTW"  : []
                     }


    


    RESELLER_PAGE.get("RESELLERS").append(NEW_RESELLER)
    return (RESELLER_PAGE , RESELLER_NAME)








def KEY_DELETER_1( MESSAGE:str , RESELLER_PAGE:dict):

    KEY_ID     = MESSAGE.split("keyid[")[1].split("]")[0].replace(" ", "")
    KEY_TYPE   = MESSAGE.split("keyid[")[1].split("]")[0].split("-")[-1].strip().replace(" ", "")

    RESELLER_NAME = MESSAGE.split("resellername[")[1].split("]")[0]
    RESELLER_HWID = MESSAGE.split("resellerhwid[")[1].split("]")[0]

    if not (KEY_TYPE in "APEXSL APEXSTM APEXSTW APEXAL APEXATM APEXATW APEXBNDL APEXBNDTM RUSTSL RUSTSTM RUSTSTW RUSTFBL RUSTFBTM RUSTFBTW RUSTCDRL RUSTCDRTM RUSTCDRTW SOTCTM SOTCTW"):
        return (False , "Invalid Key-Type")

    FOUND_RESELLER = (False , None)
    for X in range(len(RESELLER_PAGE.get("RESELLERS"))):
        
        if (RESELLER_PAGE.get("RESELLERS")[X].get("RESELLER_HWID") == RESELLER_HWID) and (RESELLER_PAGE.get("RESELLERS")[X].get("DISCORD_NAME") == RESELLER_NAME) :
           FOUND_RESELLER = (True , X)



    if not FOUND_RESELLER[0]:
        return (False , "Reseller-Not-Found")


    else:
        try:
            RESELLER_PAGE.get("RESELLERS")[FOUND_RESELLER[1]][KEY_TYPE].remove(KEY_ID)
            return (RESELLER_PAGE , KEY_ID , RESELLER_NAME)

        except (ValueError) as EEE:
            return (False , "Key-Dont-Exist" , EEE) #<---| Catch the error if key don't exist

        





def KEY_DELETER_2( MESSAGE:str , KEYS_PAGE:dict):

    KEY_ID     = MESSAGE.split("keyid[")[1].split("]")[0].replace(" ", "")
    KEY_TYPE   = MESSAGE.split("keyid[")[1].split("]")[0].split("-")[-1].replace(" ", "")

    if not (KEY_TYPE in "APEXSL APEXSTM APEXSTW APEXAL APEXATM APEXATW APEXBNDL APEXBNDTM RUSTSL RUSTSTM RUSTSTW RUSTFBL RUSTFBTM RUSTFBTW RUSTCDRL RUSTCDRTM RUSTCDRTW SOTCTM SOTCTW"):
        return (False , "Invalid Key-Type")

    try:
        KEYS_PAGE[KEY_TYPE].remove(KEY_ID)
        return (KEYS_PAGE , KEY_ID , KEY_TYPE)

    except (ValueError) as EEE:
        return (False , "Key-Dont-Exist" , EEE) #<---| Catch the error if key don't exist




    

def RESELLER_DELETER( MESSAGE:str , RESELLER_PAGE:dict ):

    KEY_TYPE_LIST= ["APEXSL" , "APEXSTM" , "APEXSTW" , "APEXAL" , "APEXATM" , "APEXATW" , "APEXBNDL" , "APEXBNDTM" , "RUSTSL" , "RUSTSTM" , "RUSTSTW" , "RUSTFBL" , "RUSTFBTM" , "RUSTFBTW" , "RUSTCDRL" , "RUSTCDRTM" , "RUSTCDRTW" , "SOTCTM" , "SOTCTW"]       

    RESELLER_NAME = MESSAGE.split("resellername[")[1].split("]")[0]
    RESELLER_HWID = MESSAGE.split("resellerhwid[")[1].split("]")[0]


    FOUND_RESELLER = (False , None)
    for X in range(len(RESELLER_PAGE.get("RESELLERS"))):
        if (RESELLER_PAGE.get("RESELLERS")[X].get("RESELLER_HWID") == RESELLER_HWID) and (RESELLER_PAGE.get("RESELLERS")[X].get("DISCORD_NAME") == RESELLER_NAME) :
            FOUND_RESELLER = (True , X)


    if not FOUND_RESELLER[0]:
        return (False , "Reseller-Not-Found")


    else:
        for X in KEY_TYPE_LIST:
            for Y in RESELLER_PAGE.get("RESELLERS")[FOUND_RESELLER[1]].get(X) :
                if not ("-USED KEY" in Y):
                    return (False , "Reseller-Has-Active-Keys" , Y)


        del RESELLER_PAGE.get("RESELLERS")[FOUND_RESELLER[1]]

        return ( RESELLER_PAGE , RESELLER_NAME )

                












                
        














