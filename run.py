from telethon.sync import TelegramClient
from telethon import functions, types
import random, time, requests
from os import system
api_id="2368323"
api_hash="5f4a5bd7985e44446e184b71172b704a"
phone="+905314088885"
database_encryption_key="changename1234"
name=phone

f=open("yeni.txt","r")
k=open("key.txt","r")
key=k.read().strip()
k.close()
key=int(key)

def kontrol(m):
   if "phone=" in m:
      return True
   return False
s=0
with TelegramClient(name, api_id, api_hash) as client:
  for no, i in enumerate(f):

           i=i.strip()
           i=i+ "+90531"+ i   
           result = client(functions.contacts.ImportContactsRequest(
           contacts=[types.InputPhoneContact(
           client_id=random.randrange(-2**63, 2**63),
            phone=i,
            first_name='denemer',
            last_name='denemd',
        )]
    ))
      
           if kontrol(result.stringify()):
               system("echo " + i + " >> users.txt")

           print(no)
           system("echo " + str(no) + " > key.txt")
           s+=1
           print(no+1)
  
ff.close()
f.close()
             
