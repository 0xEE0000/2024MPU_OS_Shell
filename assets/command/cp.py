import shutil
import os

def cp(source, destination):
    try:
        if os.path.isfile(source):  
            shutil.copy(source, destination)
            print(f"File '{source}' copied to '{destination}'.")
        elif os.path.isdir(source):  
            shutil.copytree(source, destination) 
            print(f"Directory '{source}' copied to '{destination}'.")
        else:
            print(f"Source '{source}' does not exist.")
    except FileExistsError:
        print(f"Destination '{destination}' already exists.")
    except Exception as e:
        print(f"Error: {e}")
