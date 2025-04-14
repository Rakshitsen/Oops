import subprocess

subprocess.run(["mkdir", "project_folder"])
subprocess.run(["touch", "project_folder/main.py", "project_folder/README.md"])
subprocess.run(["ls", "-l", "project_folder"])
