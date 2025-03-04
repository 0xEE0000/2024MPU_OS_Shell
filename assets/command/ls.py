import os

def ls(path="."):
    try:
        # 获取目录内容
        items = os.listdir(path)
        if not items:
            print("Directory is empty.")
        else:
            for item in items:
                print(item)
    except FileNotFoundError:
        print(f"Directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"'{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"Error: {e}")
