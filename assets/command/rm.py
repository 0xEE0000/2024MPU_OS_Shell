import shutil
import os

def rm(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' removed successfully.")
        elif os.path.isdir(path):  
            shutil.rmtree(path)  
            print(f"Directory '{path}' removed successfully.")
        else:
            print(f"Path '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")
