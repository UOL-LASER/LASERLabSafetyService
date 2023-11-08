import threading
from modules.eventlogger import EventLogger
from datetime import datetime, timedelta

from socket import socket 

clientlist = {}
clientlist_lock = threading.Lock()

class UserHandling(threading.Thread):
    def __init__(self, fullname, studentid, discordclientid):
        threading.Thread.__init__(self)
        
        self.fullname = fullname
        self.studentid = studentid
        self.discordclientid = discordclientid
        self.user = client.get_user(self.discordclientid)
        
        self.labtimer = datetime.now()
        self.el = EventLogger(self.fullname + " " + self.labtimer)
        self.el.LoggingInit
       
    async def run(self):
        n = 1
        self.el.LOGEVENTS_INFO(f"User: {self.fullname} Student-ID: {self.studentid} has entered lab")
        try:
            while (self.discordclientid in threadingevents and not threadingevents[self.discordclientid].is_set()) :
            
                if (datetime.now() >= self.labtimer + timedelta(hours=1)):
                    if self.user.dm_channel is None:
                        await self.user.send("Please respond so I can confirm you are still alive within the lab.")
                        await client.wait_for('message', timeout=300)
                    n += 1
                else:
                    pass
                    
        except KeyError:
            print(f"Event not found for key {self.discordclientid}")
            self.join()
            
       

                    