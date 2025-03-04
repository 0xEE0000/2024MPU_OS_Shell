Group Members:
1.鲍睿 BAO RUI P2321323
2.谢松琦 XIE SONGQI p2321396
3.程心远 CHENG XINYUAN p2321089
# About the shell

## Entrance

For the entrance, we start from `Enter command`. In here, users have 1 types of command:

1. `shell` + `argument`

### Interactive

For the `shell interactive` , it will direct to `interactive_shell` which allows users to put command in. For the `interactive_shell`, there are couple of command provided:

- no command: Do nothing but won't be interrupted.
- quit / `Ctrl` + `D`: quit this program, and this command can also be used in **Entrance**.
- pwd: `pwd` print current path.
- cd: `cd` change the current path.If ` ` exists in your path, you should use`""` to wrapp up the path
  - `cd /enter/your/path` directs to a global(absolute) path.
  - `cd ./your/path` directs to a local path. `./` means the current path. You can also use `cd path` to direct to only the next-level path locally.
- mkdir: creates a new folder by using `mkdir folderName`.
- rmdir: delete an old folder by using `rmdir folderName`.
- rm: delete an old file by using `rm fileName`(should also type the Filename Extension).
- cat: display a file by using `cat filName`(should also type the Filename Extension). In addition, command like `cat another/path/file.txt` is also allowed.
- ls: display the content of input path. `ls` mean current. 
  - `ls /enter/your/path` dispay the content of a global path
  - `ls ./your/path` dispay the content of a local path
- cp: copy the content of filename1 to filename2. The command format: `cp filename1 filename2`(should also type the Filename Extension).
- echo: input content to a file, if the file does not exit, it will create the file.
  - the command format: `echo "Your input" > filename`(should also type the Filename Extension).
- createfile: create a new file in current path. If the file already exist, clear it else create a new one.
  - the command format: `createfile filename`(should also type the Filename Extension).


### Batch

For the `shell batch` , it will direct to `batch_mode` which allows users to put command in. For the `batch_mode`, there are couple of command provided:

- no command: Do nothing but won't be interrupted.
- quit: quit this program, and this command can also be used in **Entrance**.
- pwd: `pwd` print current path.
- cd: `cd` change the current path.If ` ` exists in your path, you should use`""` to wrapp up the path
  - `cd /enter/your/path` directs to a global(absolute) path.
  - `cd ./your/path` directs to a local path. `./` means the current path. You can also use `cd path` to direct to only the next-level path locally.
- mkdir: creates a new folder by using `mkdir folderName`.
- rmdir: delete an old folder by using `rmdir folderName`.
- rm: delete an old file by using `rm fileName`(should also type the Filename Extension).
- cat: display a file by using `cat filName`(should also type the Filename Extension). In addition, command like `cat another/path/file.txt` is also allowed.
- ls: display the content of input path. `ls` mean current. 
  - `ls /enter/your/path` dispay the content of a global path
  - `ls ./your/path` dispay the content of a local path
- cp: copy the content of filename1 to filename2. The command format: `cp filename1 filename2`(should also type the Filename Extension).
- echo: input content to a file, if the file does not exit, it will create the file.
  - the command format: `echo "Your input" > filename`(should also type the Filename Extension).
- createfile: create a new file in current path. If the file already exist, clear it else create a new one.
  - the command format: `createfile filename`(should also type the Filename Extension).  