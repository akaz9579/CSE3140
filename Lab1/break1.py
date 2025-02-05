import time 
import subprocess

file = open("MostCommonPWs", "r")
start = time.time()
username = "SkyRedFalcon914"
pw = [line.strip() for line in file]

for password in pw:
    print(f'Testing {password}')

    check = subprocess.run(["python3", "Login.pyc", username, password], capture_output=True, text=True)
    if "Login successful." in check.stdout:
        print(f"Password found: {password}")
        break

end = time.time()
tot  =  end - start
print(f"Time taken:{tot}")

    
    

