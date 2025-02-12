import hashlib
import itertools
import subprocess
import time

start = time.time()

# Load gang members
with open("/home/cse/Lab1/Q6/gang", "r") as f:
    gang_members = {line.strip() for line in f}

# Load salted passwords
salted_pw_dict = {}  # { user: (salt, hashed_pw) }
with open("/home/cse/Lab1/Q6/SaltedPWs", "r") as f:
    for line in f:
        user, salt, hashed_pw = line.strip().split(",")
        if user in gang_members:
            salted_pw_dict[user] = (salt, hashed_pw)

# Load common passwords
with open("/home/cse/Lab1/Q6/PwnedPWs100k", "r") as f:
    base_passwords = [line.strip() for line in f]

recovered_credentials = {}

# Try password cracking
for base_pw in base_passwords:
    for d in range(10):  # Append single-digit combos (0-9)
        candidate_pw = f"{base_pw}{d}"

        for user, (salt, stored_hash) in salted_pw_dict.items():
            hashed_guess = hashlib.sha256((salt + candidate_pw).encode("utf-8")).hexdigest()

            if hashed_guess == stored_hash:
                recovered_credentials[user] = candidate_pw
                print(f"Recovered password for {user}: {candidate_pw}")

verified_credentials = {}

# Verify credentials using Login.pyc
for user, password in recovered_credentials.items():
    check = subprocess.run(["python3", "Login.pyc", user, password], capture_output=True, text=True)
    if "Login successful." in check.stdout:
        verified_credentials[user] = password
        print(f"Confirmed login for {user} with password: {password}")

output_file = "/home/cse/Lab1/Q6/cracked_passwords.txt"
with open(output_file, "w") as f:
    for user, password in verified_credentials.items():
        f.write(f"{user},{password}\n")

end = time.time()
print(f"Total execution time: {end - start:.2f} seconds")

# Print the first verified credential for submission
if verified_credentials:
    user, password = next(iter(verified_credentials.items()))
    print(f"Submit this: {user}, {password}")