import discord
import asyncio
###############
import random
import base64   #Not sure if base64 works directly like this in linux ...
#################
import requests  # not sure works on linux??
import subprocess
import time
from datetime import datetime,timezone
import re
import json
from helper import KEY_CHECKER , HWID_REGISTER , Key_Encoder , DECRYPT_RESELLER_PAGE , ENCRYPT_RESELLER_PAGE , RESELLER_PAGE_LOAD , KEYS_PAGE_LOAD , HWID_PAGE_LOAD, LOGGER
from command_functions import DISPLAY_KEY_COUNT , KEY_ADDER , RESELLER_REGISTERER , KEY_DELETER_1 , KEY_DELETER_2 , RESELLER_DELETER#, ACTIVE_KEYS









CAN_RUN = True
CAN_RUN_TIMER=0


class MyClient(discord.Client):
    
    
    async def on_ready(self):
        print('Logged on as', str(self.user).split('#')[0])

    async def on_message(self, message):
        global CAN_RUN
        global CAN_RUN_TIMER
 
        #print(message.content)

        if (not CAN_RUN) and (time.perf_counter() - CAN_RUN_TIMER)>60: #<----| In-case it errors and leaves CAN_RUN False
            CAN_RUN = True
            

        
        if "**USED_KEY      :::" in str(message.content):

            if CAN_RUN and (time.perf_counter() - CAN_RUN_TIMER)>0:
                CAN_RUN = False  #Geçişi kapadık
                
                ENCRYPTED_KEY = ""
                KEY  = str(message.content.split("**USED_KEY      ::: **")[1].split("> **Hwid")[0].split("\n")[0])
                HWID = str(message.content.split("**Hwid                  ::: **")[1].split("\n")[0])
            
            
                if len(KEY) > 20 and not("USED KEY" in KEY ):  # Girilen Keyin lenghti 20'den kısaysa checklemeyecek bile. Aynı <20 olayını scripte de ekledim. Eğer 20 haneden küçük bir key girerse zahmet edip bizim bota bile iletmeyecek
     

                    KEYS_PAGE = KEYS_PAGE_LOAD()
                    KEYS_JSON = json.loads(KEYS_PAGE)

                    TYPE = KEY_CHECKER(KEYS_JSON , KEY)
                    if TYPE:#KEY in keys_page_CHECK :
                    
                        await message.channel.send("~~||--------------------------------------------------------------------||~~\n> **Register Process Started**   **` Key is Valid `**\n~~||--------------------------------------------------------------------||~~" )


      ######################      K E Y   R E P L A C E      ######################


                        KEYS_PAGE = KEYS_PAGE.replace(KEY, f"-USED KEY:{KEY}  ||  TIME: {str(datetime.now(timezone.utc)).split('.')[0]}")#Kullanılan keyi sayfada "-USED KEY-" ile değiştiriyoruz.
                     
                        with open(r'KEYS_PAGE/index.html', 'w') as file:
                            file.write(KEYS_PAGE)

                        subprocess.call("BAT_KEYS.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  


                        await message.channel.send("> **1) UPDATED KEYS PAGE**")


                        
        ######################   H W I D   R E G I S T E R   ######################



                        HWIDS_PAGE = HWID_PAGE_LOAD()

                        HWIDS_JSON = json.loads(HWIDS_PAGE)

                        ENCRYPTED_KEY = Key_Encoder(HWID,KEY)

                        TOKEN = HWID_REGISTER(TYPE , ENCRYPTED_KEY)

                        HWIDS_JSON[TYPE].append(TOKEN)
                        
                        HWIDS_JSON = str(HWIDS_JSON).replace("'APEXAL'", '"APEXAL"').replace("'APEXATM'", '"APEXATM"').replace("'APEXATW'", '"APEXATW"').replace("'APEXSL'", '"APEXSL"').replace("'APEXSTM'", '"APEXSTM"').replace("'APEXSTW'", '"APEXSTW"').replace("'RUSTSL'", '"RUSTSL"').replace("'RUSTSTM'", '"RUSTSTM"').replace("'RUSTSTW'", '"RUSTSTW"').replace("'SOTCTM'", '"SOTCTM"').replace("'SOTCTW'", '"SOTCTW"').replace("'APEXBNDL'", '"APEXBNDL"').replace("'APEXBNDTM'", '"APEXBNDTM"').replace("'RUSTFBL'", '"RUSTFBL"').replace("'RUSTFBTM'", '"RUSTFBTM"').replace("'RUSTFBTW'", '"RUSTFBTW"').replace("'RUSTCDRL'", '"RUSTCDRL"').replace("'RUSTCDRTM'", '"RUSTCDRTM"').replace("'RUSTCDRTW'", '"RUSTCDRTW"')                                                        

                        with open(r'HWIDS_PAGE/index.html', 'w') as file:    
                            file.write( HWIDS_JSON )

                        subprocess.call("BAT_HWIDS.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  

                        await message.channel.send(f"||**@everyone**||\n> **2) REGISTERED USER TO THE HWID PAGE**\n\n> **HWID :** `{HWID}`\n> **KEY :** `{KEY}`\n> **ENCRYPTED_KEY :** `{TOKEN}`")






    ########################   R E S E L L E R   P A G E   U P D A T E   #################################


                        RESELLER_PAGE = RESELLER_PAGE_LOAD()

                        RESELLER_PAGE = DECRYPT_RESELLER_PAGE( RESELLER_PAGE )  #<---| SAYFADAN GELEN TEXTİ DECRYPE EDİYOR  



                        pc_username = message.content.split("**Pc_username  :::** ")[1].split("\n>")[0].replace("[", "").replace("]","").replace("KEYS_LAST","").replace("KEY_","")    #  <------------ MAKING SURE PC_USERNAME AND PC_REAL_NAME DOESNT HAVE THESE CHARACTERS
                        pc_realname = message.content.split("**Pc_real_name :::** ")[1].split("\n>")[0].replace("[", "").replace("]","").replace("KEYS_LAST","").replace("KEY_","")    #                      CAUSE IF THEY DO THEN RESELLER APP'S STRING SORTING SYSTEM WILL CUT THE STRING FROM THESE PARTS AND WILL CAUSE IT TO NOT SHOW SOME OF THE KEYS(SOLD OR NOT SOLD DOESNT MATTER, THEY BOTH STORED SİDE BY SİDE SO THAT'S A PROBLEM TO HANDLE
                       
                        RESELLER_PAGE = RESELLER_PAGE.replace(KEY,  f"-USED KEY || TIME: {str(datetime.now(timezone.utc)).split('.')[0]} || {pc_username} || {pc_realname} || {HWID} || {KEY} "  )   #ADDING BUYER INFORMATIN NEXT TO THE REMOVED KEY SO OUR RESELLER APP CAN PICK IT UP AND PRESENT AS "USED: ....HWID // PC_NAME // TIME ...."           


                        RESELLER_PAGE_ENCRYPTED = ENCRYPT_RESELLER_PAGE( RESELLER_PAGE )
            



                        with open(r'RESELLER_PAGE/index.html', 'w') as file:
                            file.write(str(RESELLER_PAGE_ENCRYPTED))

    
                        subprocess.call("BAT_RESELLER.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  
                        

                        await message.channel.send(f"> **3) UPDATED RESELLER PAGE **\n~~||--------------------------------------------------------------------||~~")





                 ##############################    W A I T I N G   P R O C E S S    ##############################


      
                        CAN_RUN_TIMER = time.perf_counter() + 10
                        CAN_RUN = True
                        await message.channel.send("`I wont answer your commands for next 20 seconds to make sure websites are updated`") 
                        LOGGER(LOG_REASON="MEMBER REGISTERATION" , RESELLER_PAGE=True , HWIDS_PAGE=True , KES_PAGE=True)
                        



                        
                            

                    else:  #<----| "Girilen Key KEYS_PAGE'de yoksa uyar //
                        await message.channel.send("@everyone\n||~~----------------------------------------------------------------------------------------------------------~~||" + "\n" + F"> **THIS IS NOT A REGISTERED KEY IN RUINER DATABASE** \n> **KEY ::: {KEY} ** \n> ||`( Or it Doesn't have key type inside it; APEXSL/APEXSM/RUSTSL etc.etc.)`||" +  "\n" +  "||~~----------------------------------------------------------------------------------------------------------~~||")
                      
                                                                                                                                                                                



                else:  #<----| Key yanlış girilirse uyar // 
                    if len(KEY) < 20 :
                        await message.channel.send("||~~----------------------------------------------------------------------------------------------------------~~||" + "\n" + F"> **@everyone KEY IS SHORTER THAN 20 CHARS,  KEY ::: {KEY} **" +  "\n" +  "||~~----------------------------------------------------------------------------------------------------------~~||**")
     

                    elif ("USED KEY" in KEY ):
                        await message.channel.send("||~~----------------------------------------------------------------------------------------------------------~~||" + "\n" + F"> **@everyone KEY CONTAINS 'USED KEY' ,  KEY ::: {KEY} **" +  "\n" +  "||~~----------------------------------------------------------------------------------------------------------~~||**")
      
                CAN_RUN = True



            else:
                if not CAN_RUN:
                    print(f"ANOTHER MESASGE IS PROCESSING RIGHT NOW | DID NOT REGISTER THE USER WITH HWID : " + "\n" + "{HWID}")
                    await message.channel.send(f"**@everyone ANOTHER MESASGE IS PROCESSING RIGHT NOW | DID NOT REGISTER THE USER WITH HWID : **" + "\n" + "{HWID} **")


                elif (time.perf_counter() - CAN_RUN_TIMER)<0:
                    await message.channel.send(f"> `I can't Register You, Currently Waiting to make sure websites are updated before registering somebody else.   Cooldown:{int(abs(time.perf_counter() - CAN_RUN_TIMER))} Seconds`")










        elif ("/m give_keys" in str(message.content)) and ("amount[" in str(message.content)) and ("keytype[" in str(message.content)) and ("resellername[" in str(message.content)) and ("resellerhwid[" in str(message.content)) :

            if CAN_RUN and (time.perf_counter() - CAN_RUN_TIMER)>0:
                CAN_RUN = False  #Geçişi kapadık


                RESELLER_PAGE = RESELLER_PAGE_LOAD()


                RESELLER_PAGE = DECRYPT_RESELLER_PAGE( RESELLER_PAGE )  #<---| SAYFADAN GELEN TEXTİ DECRYPE EDİYOR  
                RESELLER_PAGE = json.loads( RESELLER_PAGE )


                RESPONSE = KEY_ADDER( str(message.content) , RESELLER_PAGE )
                
                if RESPONSE[0]!=False:
                    RESPONSE_DICT = str(RESPONSE[0]).replace("'", '"') #<---| Json doesn't support '''
                    RESELLER_PAGE_ENCRYPTED = ENCRYPT_RESELLER_PAGE( RESPONSE_DICT )
                    with open(r'RESELLER_PAGE/index.html', 'w') as file:
                        file.write(str(RESELLER_PAGE_ENCRYPTED))
                    subprocess.call("BAT_RESELLER.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)         

        
                    KEYS_PAGE = KEYS_PAGE_LOAD()
                    KEYS_JSON = json.loads(KEYS_PAGE)


                    for X in RESPONSE[1]:
                        KEYS_JSON[RESPONSE[2]].append(X)
                    #print(KEYS_JSON)

                    KEYS_JSON = str(KEYS_JSON).replace("'", '"') 
                    with open(r'KEYS_PAGE/index.html', 'w') as file:
                        file.write(str(KEYS_JSON))
                    subprocess.call("BAT_KEYS.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                        

     
                    await message.channel.send(f"**@everyone \nSuccessfully Gave Keys to {RESPONSE[3]} \nGIVEN KEYS:**") 
                    for Z in RESPONSE[1]:
                        await message.channel.send(f"**`{Z}`**")
                    await message.channel.send("||`I wont answer your commands for next 20 seconds to make sure websites are updated`||") 
                    CAN_RUN_TIMER = time.perf_counter() + 10
                    LOGGER(LOG_REASON="Key Added to a Reseller" , RESELLER_PAGE=True , HWIDS_PAGE=True , KES_PAGE=True)


                else:
                    if RESPONSE[1]=="Not-Found":
                        await message.channel.send(f"**@everyone No Reseller Found that matches this Name and HWID in our DataBase **")

                    elif RESPONSE[1]=="Invalid Key-Type":
                        await message.channel.send(f"**@everyone The Key-Type you input is not a Valid one, Dumb nigga **")

                CAN_RUN = True  #Geçişi Açtık

            else:
                await message.channel.send(f"`I Can't Answer Right Now,  Waiting to make sure all websites are updated.  Cooldown:{int(abs(time.perf_counter() - CAN_RUN_TIMER))} Seconds`") 






        elif ("/m register_reseller" in str(message.content)) and ("resellername[" in str(message.content)) and ("resellerhwid[" in str(message.content)) and ("resellerdisk_serial[" in str(message.content)) :
            
            if CAN_RUN and (time.perf_counter() - CAN_RUN_TIMER)>0:
                CAN_RUN = False  #Geçişi kapadık

                RESELLER_PAGE = RESELLER_PAGE = RESELLER_PAGE_LOAD()

                RESELLER_PAGE = DECRYPT_RESELLER_PAGE( RESELLER_PAGE )  #<---| SAYFADAN GELEN TEXTİ DECRYPE EDİYOR  
                RESELLER_PAGE = json.loads( RESELLER_PAGE )

                RESPONSE = RESELLER_REGISTERER(str(message.content) , RESELLER_PAGE)


                if RESPONSE[0]!= False:
                    RESPONSE_DICT = str(RESPONSE[0]).replace("'", '"') #<---| Json doesn't support ''' 
                    RESELLER_PAGE_ENCRYPTED = ENCRYPT_RESELLER_PAGE( RESPONSE_DICT )
                    with open(r'RESELLER_PAGE/index.html', 'w') as file:
                        file.write(str(RESELLER_PAGE_ENCRYPTED))
                    subprocess.call("BAT_RESELLER.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  

                    await message.channel.send(f"**@everyone \nSuccessfully Registered Reseller with name : {RESPONSE[1]} **") 
                    await message.channel.send("||`I wont answer your commands for next 20 seconds to make sure websites are updated`||") 
                    CAN_RUN_TIMER = time.perf_counter() + 10
                    LOGGER(LOG_REASON="Reseller Registeration" , RESELLER_PAGE=True , HWIDS_PAGE=True , KES_PAGE=True)

                else :
                    if RESPONSE[1] == "Already-Exist" :
                        await message.channel.send(f"**@everyone Same Hwid & Named Reseller/person already rergistered as Reseller **")

                    elif RESPONSE[1] == "Invalid-Characters" :
                        await message.channel.send(f"**@everyone Resellername & RESELLER_HWID Shouldn't Contain the character ' \" ' **")

                CAN_RUN = True  #Geçişi Açtık

            else:
                await message.channel.send(f"`I Can't Answer Right Now,  Waiting to make sure all websites are updated.  Cooldown:{int(abs(time.perf_counter() - CAN_RUN_TIMER))} Seconds`") 






        elif ("/m delete_key" in str(message.content)) and ("keyid[" in str(message.content)) and ("resellername[" in str(message.content)) and ("resellerhwid[" in str(message.content)) :
            
            if CAN_RUN and (time.perf_counter() - CAN_RUN_TIMER)>0:
                CAN_RUN = False  #Geçişi kapadık
                
                RESELLER_PAGE = RESELLER_PAGE = RESELLER_PAGE_LOAD()

                RESELLER_PAGE = DECRYPT_RESELLER_PAGE( RESELLER_PAGE )  #<---| SAYFADAN GELEN TEXTİ DECRYPE EDİYOR  
                RESELLER_PAGE = json.loads( RESELLER_PAGE )


                KEYS_PAGE = KEYS_PAGE_LOAD()
                KEYS_PAGE = json.loads(KEYS_PAGE)


                RESPONSE_1 = KEY_DELETER_1(str(message.content) , RESELLER_PAGE)
                RESPONSE_2 = KEY_DELETER_2(str(message.content) , KEYS_PAGE)

                
                if (RESPONSE_1[0]!= False) and (RESPONSE_2[0]!= False):

                    RESPONSE_DICT_1 = str(RESPONSE_1[0]).replace("'", '"') #<---| Json doesn't support ''' 
                    RESELLER_PAGE_ENCRYPTED = ENCRYPT_RESELLER_PAGE( RESPONSE_DICT_1 )
                    with open(r'RESELLER_PAGE/index.html', 'w') as file:
                        file.write(str(RESELLER_PAGE_ENCRYPTED))
                    subprocess.call("BAT_RESELLER.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  



                    KEYS_JSON = str(RESPONSE_2[0]).replace("'", '"') 
                    with open(r'KEYS_PAGE/index.html', 'w') as file:
                        file.write(str(KEYS_JSON))
                    subprocess.call("BAT_KEYS.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  


                    await message.channel.send(f"**@everyone \nSuccessfully Deleted Key: `{RESPONSE_1[1]}` From Reseller Named: `{RESPONSE_1[2]}`**") 
                    await message.channel.send("||`I wont answer your commands for next 20 seconds to make sure websites are updated`||") 
                    CAN_RUN_TIMER = time.perf_counter() + 10
                    LOGGER(LOG_REASON="Key Deletion" , RESELLER_PAGE=True , HWIDS_PAGE=True , KES_PAGE=True)

                else :
                    if RESPONSE_1[1] == "Reseller-Not-Found" :
                        await message.channel.send(f"**@everyone No Resellers Found with the Given Name ...**")

                    elif RESPONSE_1[1] == "Invalid Key-Type":
                        await message.channel.send(f"**@everyone The Key You input is Invalid!  It Doesn't Have a valid *KEY_TYPE* `(APEXSL/APEXSM/RUSTSL etc.etc.)`**")
                    elif RESPONSE_1[1] == "Key-Dont-Exist" :
                        await message.channel.send(f"**@everyone The Key You input Does not exist under The name Given Reseller**")
                    elif RESPONSE_2[1] == "Key-Dont-Exist" :
                        await message.channel.send(f"**@everyone The Key You input is registered to Given Reseller, But Doesn't Exsist in KEYS_PAGE \nThere must been an Error while registering this key in past**")

                CAN_RUN = True  #Geçişi Açtık

            else:
                await message.channel.send(f"`I Can't Answer Right Now,  Waiting to make sure all websites are updated.  Cooldown:{int(abs(time.perf_counter() - CAN_RUN_TIMER))} Seconds`") 






        elif ("/m delete_reseller" in str(message.content)) and ("resellername[" in str(message.content)) and ("resellerhwid[" in str(message.content)) :

            if CAN_RUN and (time.perf_counter() - CAN_RUN_TIMER)>0:
                CAN_RUN = False  #Geçişi kapadık
                
                RESELLER_PAGE = RESELLER_PAGE = RESELLER_PAGE_LOAD()

                RESELLER_PAGE = DECRYPT_RESELLER_PAGE( RESELLER_PAGE )  #<---| SAYFADAN GELEN TEXTİ DECRYPE EDİYOR  
                RESELLER_PAGE = json.loads( RESELLER_PAGE )

                RESPONSE = RESELLER_DELETER(str(message.content) , RESELLER_PAGE)

                print("RESPONSE ===++++=== " , RESPONSE)
                if (RESPONSE[0]!= False):
                    RESPONSE_DICT = str(RESPONSE[0]).replace("'", '"') #<---| Json doesn't support ''' 
                    RESELLER_PAGE_ENCRYPTED = ENCRYPT_RESELLER_PAGE( RESPONSE_DICT )
                    with open(r'RESELLER_PAGE/index.html', 'w') as file:
                        file.write(str(RESELLER_PAGE_ENCRYPTED))
                    subprocess.call("BAT_RESELLER.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  

                    await message.channel.send(f"**@everyone \nSuccessfully Deleted Reseller with name : {RESPONSE[1]} **") 
                    await message.channel.send("||`I wont answer your commands for next 20 seconds to make sure websites are updated`||") 
                    CAN_RUN_TIMER = time.perf_counter() + 10
                    LOGGER(LOG_REASON="Reseller Deletion" , RESELLER_PAGE=True , HWIDS_PAGE=True , KES_PAGE=True)

                else :
                    if RESPONSE[1] == "Reseller-Not-Found" :
                        await message.channel.send(f"**@everyone No Resellers Found with the Given Name ...**")

                    elif RESPONSE[1] == "Reseller-Has-Active-Keys" :
                        await message.channel.send(f"**@everyone Reseller Has Active Keys, Delete All the Active Keys Before Deleting Reseller... \nActive key = `{RESPONSE[2]}`**")

                CAN_RUN = True  #Geçişi Açtık

            else:
                await message.channel.send(f"`I Can't Answer Right Now,  Waiting to make sure all websites are updated.  Cooldown:{int(abs(time.perf_counter() - CAN_RUN_TIMER))} Seconds`") 




        elif "/m display_Resellers" == str(message.content):
            RESELLER_PAGE = RESELLER_PAGE = RESELLER_PAGE_LOAD()

            RESELLER_PAGE = DECRYPT_RESELLER_PAGE( RESELLER_PAGE )  #<---| SAYFADAN GELEN TEXTİ DECRYPE EDİYOR  
            RESELLER_PAGE = json.loads( RESELLER_PAGE )


            print(RESELLER_PAGE)

            print("\n\n\n1+++++++++++++++++++++++++\n\n\n")

####
####            for X in RESELLER_PAGE.get("RESELLERS"):
####                X["RUSTFBL"]  = []
####                X["RUSTFBTM"] = []
####                X["RUSTFBTW"] = []
####
####                X["RUSTCDRL"]  = []
####                X["RUSTCDRTM"] = []
####                X["RUSTCDRTW"] = []
####
####
####            print(RESELLER_PAGE)
####
####
####            RESPONSE_DICT = str(RESELLER_PAGE).replace("'", '"') #<---| Json doesn't support ''' 
####            RESELLER_PAGE_ENCRYPTED = ENCRYPT_RESELLER_PAGE( RESPONSE_DICT )
####            with open(r'RESELLER_PAGE/index.html', 'w') as file:
####                file.write(str(RESELLER_PAGE_ENCRYPTED))
####            subprocess.call("BAT_RESELLER.bat", shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  
####





        elif "/m all_keys" == str(message.content):
            KEYS_PAGE = requests.get("kwordss.netlify.app").text

            try:
                KEYS_PAGE = (KEYS_PAGE).split("<body>")[1].split("</body>")[0]
            except:
                pass  
            
            KEYS_JSON = json.loads(KEYS_PAGE)

            DISPLAY_KEY_COUNT(KEYS_JSON)  






        elif "/m keys active" in str(message.content):

            HWIDS_PAGE = requests.get("realhworrrddss.netlify.app").text

            try:
                HWIDS_PAGE = (HWIDS_PAGE).split("<body>")[1].split("</body>")[0]
            except:
                pass  
            
            HWIDS_JSON = json.loads(HWIDS_PAGE)

            ACTIVE_KEYS(HWIDS_JSON , str(message.content))



 

        elif "/m LOG" in str(message.content):
            
            LOGGER(LOG_REASON="MANUAL" , RESELLER_PAGE=True , HWIDS_PAGE=True , KES_PAGE=True)





                

client = MyClient()
        
client.run('MTAxMTY2MjczNDkyMTgzODYyMg.Gui3Iu.HXe04GhhVwe09dTtVPBsQ-P4_a33V2MYtkdeiU')

