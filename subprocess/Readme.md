 What is subprocess?
The subprocess module lets you run shell or terminal commands from within your Python script.

import subprocess

subprocess.run(["echo", "Hello, Rakshit!"])





Why use subprocess.run() instead of os.system()?
os.system() is old, limited, and doesn’t capture output well.

subprocess.run() gives full control (output, errors, return codes)



The problem:
subprocess.run(["cd","project_folder"])


won’t actually change the current directory for the next command (ls) — because each subprocess runs in its own shell session, and the cd change doesn't persist.


Mini Lesson: cd won't persist
Each subprocess.run(...) is like opening a new terminal, typing a command, and closing it. So cd doesn’t carry over.

To run multiple shell commands in sequence, use:

subprocess.run("cd folder && some_command", shell=True)



Why capture output?
You might want to:

Store results (like filenames, versions, logs)

Check for success/failure programmatically

Automate responses based on command output

import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print("Output:")
print(result.stdout)






What is stdout and stderr?
They’re both output streams — channels that your program uses to communicate with the outside world.

stdout = Standard Output
This is where normal output goes.

If a command runs successfully and prints something — it goes to stdout.

ls Prints the list of files → stdout



stderr = Standard Error
This is where error messages go.

If a command fails, its message goes to stderr — not stdout.

Example:ls nonexistent

ls: cannot access 'nonexistent': No such file or directory


Why does this matter?
You can separate normal results from errors.

You can log them to different files.

In subprocess, you can access both like this:
result.stdout  # normal output
result.stderr  # error messages



Getting the Return Code
print("Return code:", result.returncode)
0 = success

Non-zero = error
