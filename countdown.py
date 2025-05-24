# countdown.py

import time 

n = int(input("Entrez un nombre pour le compte à rebours : "))

while n > 0 :
    print(n)
    n -= 1
    time.sleep(1)
    
decollage_msg = "Décollage !"
print(decollage_msg) 