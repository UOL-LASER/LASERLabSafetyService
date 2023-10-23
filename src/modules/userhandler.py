import threading
from modules.eventlogger import EventLogger
from datetime import datetime, timedelta
import time

from socket import socket 

clientlist = {}
clientlist_lock = threading.Lock()

class UserHandling(threading.Thread):
    def __init__(self, fullname, studentid, discordclientid):
        threading.Thread.__init__(self)
        
        self.fullname = fullname
        self.studentid = studentid
        self.discordclientid = discordclientid
        
        self.labtimer = datetime.now()
        self.el = EventLogger(self.fullname + " " + self.labtimer)
        self.el.LoggingInit
       
    def run(self):
        
        self.el.LOGEVENTS_INFO(f"User: {self.fullname} Student-ID: {self.studentid} has entered lab")
        
        while (datetime.now() != self.labtimer + timedelta(hours=1)) :
            
       

                    