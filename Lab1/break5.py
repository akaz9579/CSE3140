import hashlib
import time
import subprocess

#hash function, so we keep testPass in tact
def hash_password(password):
    h = hashlib.sha256()
    h.update(password.encode('utf-8'))
    return h.hexdigest()


#open all files, organize data
with open("HashedPWs", "r") as file:
    PWCred = {line.strip().split(",")[0]: line.strip().split(",")[1] for line in file}

with open("gang", "r") as fileUser:
    #usernameGang = [line.strip() for line in fileUser]
    member = "StarRedWolf267"
    
with open("PwnedPWs100k", "r") as PW100K:
    Commonpass = [line.strip() for line in PW100K]


start = time.time()

# try cracking Passwords
for Pass in Commonpass:
    for i in range(100):  # 00 to 99
        testPass = Pass + f"{i:02d}"  

        # Check for a match in HashedPWs
        if member and PWCred[member] == hash_password(testPass):
                print(f"Password found for {member}: {testPass}")

                check = subprocess.run(["python3", "Login.pyc", member, hash_password(testPass)], capture_output=True, text=True)

                if "Login successful." in check.stdout:
                    print(f"CONFIRMED:{member} used {testPass}")
                break 

end = time.time()
tot  =  end - start
print(f"Time taken:{tot}")