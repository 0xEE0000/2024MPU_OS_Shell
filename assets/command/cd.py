import os

def cd(tokens):
    try:
        os.chdir(tokens[1])
    except IndexError:
        print("No directory specified.")
    except FileNotFoundError:
        print("Directory not found.")
        return os.getcwd()
    except ValueError as ve:
        print(ve)
        return os.getcwd()