import os
def rmdir(directory):
    try:
        os.rmdir(directory)
        print(f"Directory '{directory}' removed successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory}' does not exist.")
    except OSError:
        print(f"Directory '{directory}' is not empty.")
    except Exception as e:
        print(f"Error: {e}")
