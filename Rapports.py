import schedule
from datetime import datetime
import os
import time

temps = datetime.fromtimestamp((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()+86400).strftime('%Y-%m-%d %H-%M-%S')



def cree_rapport():
    with open(r"C:\Users\HP\Desktop\Ecole\12-09\repertoiresource"+temps + ".txt","w")as f:
        f.write(temps)

def cree_5_rapport():
        for i in range (0,432000,86400):
             temps = datetime.fromtimestamp((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()+i).strftime('%Y-%m-%d %H-%M-%S')
             with open(r"C:\Users\HP\Desktop\Ecole\12-09\repertoiresource"+temps+".txt","w")as f:
                f.write("1")
            
schedule.every().day.at("17:50").do(cree_5_rapport)

while True:
    schedule.run_pending()
    time.sleep(60)
