import asyncio
import threading
from telethon import TelegramClient
import csv
import time, os,sys
import csv
from decouple import AutoConfig
import random
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
"""
```
Save your API_ID and API_HASH in Creditential/.env with the following format:
 API_ID="12345678" 
 API_HASH="12345678abcdefghijklmnopqrstuvwxyz" .

 ```
"""      
 
dirname = os.path.dirname(__file__) 
abs_path = os.path.join(dirname, 'Books')
SCOPES = 'https://www.googleapis.com/auth/drive'
Folder='14o8-_gFd1Cslyd1voBojxfctDi9LJEn3'
config = AutoConfig('Credential/.env')
gauth=GoogleAuth()
drive=GoogleDrive(gauth)
#Replace Existing File on Google Drive
#file_id = file['id']
async def upload(FileName):
    print(FileName)
    file1 = drive.CreateFile({"parents":[{"id":Folder}],'title': FileName})
    file1.SetContentFile("{}\\{}".format(abs_path,FileName))
    file1.Upload()
    print("File Uploaded")

API_ID = config('API_ID')
API_HASH = config('API_HASH')
client = TelegramClient('Credential/anon',API_ID,API_HASH)  # your session will be stored in a file called anon.session

#client.start()

loop = asyncio.get_event_loop()



"""
```
@Handlewritecsv: HandleWrite Data to {FileName}.txt file Mode =="w+" or "a+"

```
"""                        
def Handlewritecsv(FileName,FavList,mode,Type=None ):
  print("Writing csv file ")
  if Type ==None:
    for line in FavList:
        file1 = open("{}.txt".format(FileName),"{}".format(mode),encoding="utf-8")
        data= csv.writer(file1,lineterminator="\n")
        data.writerow([line])
        file1.close()
  else:
    file1 = open("{}.txt".format(FileName),"{}".format(mode),encoding="utf-8")
    data= csv.writer(file1,lineterminator="\n")
    data.writerow(FavList)
    file1.close()      

"""
```
@CheckExistancecsv: Check if text Exist in a file trom text file

```
"""    
def CheckExistancecsv(FileName,line,row=None):
  print (line)
  time.sleep(2)
  with open("{}.txt".format(FileName),"r") as data:
    data= csv.reader(data,delimiter=",",lineterminator="\n")
    for lined in data:
      if row==None:
        if lined[0] in line:
          return True
      else:
        if lined[row] in line:
          return True  
    return False    

"""
```
@GetData Retrive Data from {FileName}.txt file and returns it

```
"""        
def GetData(FileName,ReturnType=None,row=None):
  with open("{}.txt".format(FileName),"r") as data:
    data= csv.reader(data,delimiter=",",lineterminator="\n")
    for line in data:
        if ReturnType=="list":
            if line==[]:
                pass
            else:
                return line
        else:      
            if row==None:
                if line==[]:
                    pass
                else:
                    return line[0]
            else:
              return line[row]           
                
"""
```
@main: Starter Function Starts here

```
"""      
async def Starter():
  
   
      try: 
          
            Counter2=0
            print("Starting")
            await client.start()
            print("Started")
            NewmessageID=[]
            MessageID=GetData("Senderid_MessageId","list")
            
            async with client.takeout() as takeout:
                   
                    async for message in takeout.iter_messages(str(MessageID[1]), wait_time=10):
                        if Counter2>=50:
                            NewmessageID.clear()
                            NewmessageID.append(str(message.id))
                            await client.disconnect()
                            break
                               
                        if  message.id>int(MessageID[0]):


                          continue
                        else:
                           
                          try:
                              if(message.media.document.mime_type=="application/pdf"):
                                      Counter2+=1
                                      NewmessageID.clear()
                                      NewmessageID.append(str(message.id))
                                      #print(message.media.document.mime_type)
                                      path = await client.download_media(message.media, abs_path)
                                      #print(message.media.document.attributes[0].file_name,"path:{}".format(path))
                                      print("-------------------------------------------")
                                      print("-------------------------------------------")
                                      await upload(message.media.document.attributes[0].file_name)
                          except:
                              pass
                    Handlewritecsv(FileName="Senderid_MessageId",FavList=[NewmessageID[0],MessageID[1]],mode="w+",Type="list")                     
                      
                    
      except Exception as e:
          try:
              await client.disconnect()  
          except:
              print("diconnected") 
"""                    
```
Run the code forever

```  
"""       

threading.Thread(target=loop.run_until_complete(Starter())).start()
        
                                                                                         
