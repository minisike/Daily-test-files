import time
import threading

class Aa(threading.Thread):
    def run(self):
        self.login()
        for i in range(5):
            print(self.name)
    def login(self):
        for i in range(2):
            print(len(self.name))

            
if __name__ =="__main__":
    t =Aa()
    t.start()
