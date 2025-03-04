import os

def cat(file):
    try:
        file_path = os.path.join(os.getcwd(), file)
        with open(file_path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File '{file}' does not exist in {os.getcwd()}.")
    except Exception as e:
        print(f"Error: {e}")
