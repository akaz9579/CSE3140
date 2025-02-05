import hashlib
import time 
import subprocess


h = hashlib.sha256()
hashed_guess = h.hexdigest()


file = open("HashedPWs", "r")
start = time.time()

fileUser = open("gang", "r")
usernameGang = [line.strip() for line in fileUser]

PWCred = {}
KnownPasswords = ["iloveyou", "12345678", "QLnpsRxA" ]
hashedKnown = {}

#for suffix in 
#   itertools.product("0123456789", repeat=2)

for Pass in KnownPasswords:
    hashedKnown[Pass] = h.update(bytes(Pass, 'utf-8'))

print(hashedKnown)

for line in file:
    user, Password = line.strip().split(",")
    PWCred[user] = Password


for username in usernameGang:
    try:
        PWCred[username]
    except KeyError as e:
        continue

    print(f"Password test for {username}: {hashed_guess}")
    check = subprocess.run(["python3", "Login.pyc", username, hashed_guess], capture_output=True, text=True)

    if "Login successful." in check.stdout:
            print(f"Password found for {username}: {hashed_guess}")
         

end = time.time()
tot  =  end - start
print(f"Time taken:{tot}")