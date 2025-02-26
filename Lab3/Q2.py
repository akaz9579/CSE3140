import hashlib
import subprocess
import os

#Storing the hash as var to easily check
with open('Q2hash.txt', 'r') as file:
    q2 = file.read()


#change dir to access all .exe files 
os.chdir('/home/cse/Lab3/Q2files')
files = os.listdir('.')

#Hash function to translate code 
def hash(content):
    h = hashlib.sha256()
    h.update(content)  
    return h.hexdigest()

#loop thru all files, hashing the content and checking for a match
for f in files:
    with open(f, 'rb') as file:
        content = file.read()
    h = hash(content)
    
      
    if h == q2:
        print(f"{f} is the match.")
        break
    else:
        continue




