import shlex
import os
import subprocess

from assets.command import cd, quit, pwd, mkdir, rmdir, rm, cat, cp, ls

MAX_CHARS = 512

def process_execute(commands,processes):
    for cmd in commands:
        tokens = shlex.split(cmd)

        if not tokens:
            continue

        if tokens[0] == "quit":
            quit.quit()

        if tokens[0] == "pwd":
            pwd.pwd()
            continue

        if tokens[0] == "cd":
            cd.cd(tokens)
            ADDR = os.getcwd()
            continue

        if tokens[0] == "mkdir":
            if len(tokens) == 2:
                mkdir.mkdir(tokens[1])
            else:
                print("Invalid arguments:> " + str(tokens[2]))
            continue

        if tokens[0] == "rmdir":
            if len(tokens) == 2:
                rmdir.rmdir(tokens[1])
            else:
                print("Invalid arguments:> " + str(tokens[2]))
            continue

        if tokens[0] == "rm":
            if len(tokens) == 2:
                rm.rm(tokens[1])
            else:
                print("Invalid arguments:> " + str(tokens[2]))
            continue

        if tokens[0] == "cat":
            if len(tokens) == 2:
                cat.cat(tokens[1])
            else:
                print("Invalid arguments:> " + str(tokens[2]))
            continue

        if tokens[0] == "cp":
            if len(tokens) == 3:
                cp.cp(tokens[1], tokens[2])
            else:
                print("Invalid arguments:> " + str(tokens[3]))
            continue

        if tokens[0] == "ls":
            if len(tokens) == 1:
                ls.ls()
            elif len(tokens) == 2:
                ls.ls(tokens[1])
            else:
                print("Invalid arguments:> " + str(tokens[2]))
            continue

        if tokens[0] == "echo":
            if len(tokens) >= 3 and tokens[-2] == ">":
                filename = tokens[-1]
                content = " ".join(tokens[1:-2])

                with open(filename, 'a') as f:  
                    f.write(content + "\n")
                print(f"File '{filename}' echo successfully.")
            else:
                print("Invalid echo syntax. Use: echo [text] > [filename]")
            continue

        if tokens[0] == "createfile":
            if len(tokens) == 2:
                filename = tokens[1]
                with open(filename, 'w') as f:  
                    pass  
                print(f"File '{filename}' created successfully.")
            else:
                print("Invalid arguments:> createfile [filename]")
            continue

        try:
            process = subprocess.Popen(tokens)
            processes.append(process)
        except Exception as e:
            print(f"Failed to start command '{cmd}': {e}")

 
    for process in processes:
        process.wait()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Current working directory: {os.getcwd()}")
    while True:
        try:
            command = input("Enter command: ").lower()
            command = shlex.split(command)

            if not command:
                continue
            elif command[0] == "quit":
                quit.quit()
            elif command[0] == "shell":
                if command[1] == "interactive":
                    interactive_shell()
                elif command[1] == "batch":
                    batch_mode()
                else:
                    print("Invalid arguments for shell")
            else:
                print("Invalid command.")
                 
        except EOFError:  
            quit.quit()
        except KeyboardInterrupt:
            print()
            continue


def interactive_shell():
    ADDR = os.getcwd()
    while True:
        try:
            ADDR = os.getcwd()
            print(ADDR + "> ", end="")
            line = input().lower()
            if len(line) > MAX_CHARS:
                print("Command too long.")
                continue
            else:
                commands = [cmd.strip() for cmd in line.split(';') if cmd.strip()]

            processes = []
            process_execute(commands,processes)

        except EOFError:
            quit.quit()
        except KeyboardInterrupt:
            print()
            continue

def batch_mode():
    filename = input("Enter batch file name: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"Successfully opened file: {filename}")
            for line in file:
                line = line.strip().lower()
                if not line or line.startswith('#'):
                    continue  

                commands = [cmd.strip() for cmd in line.split(';') if cmd.strip()]
                processes = []
                process_execute(commands,processes)

    except FileNotFoundError:
        print(f"Batch file '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()