
import re
LOG_PATH= input("lOG PATHİNİ GİRİNİZ:\n")
uniq = {}
with open(LOG_PATH, 'r') as l:
    for line in l:
        
        m = re.search("GET /favicon.ico",line)
    
        if(m is not None):

        
            uniq[(line[:m.start()]).split(' ')[0]] = True
            

for u in uniq:
    print(u)