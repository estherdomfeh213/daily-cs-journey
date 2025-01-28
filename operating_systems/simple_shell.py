import subprocess

def simple_shell():
    while True:
        command = input("shell> ")
        if command.lower() == "exit":
            print("Exiting shell...")
            break
        try:
            # Use subprocess to run the command
            result = subprocess.run(command.split(), check=True)
        except FileNotFoundError:
            print(f"Command not found: {command}")
        except subprocess.CalledProcessError:
            print(f"Error executing command: {command}")

# Run the shell
simple_shell()
