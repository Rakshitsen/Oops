import subprocess

# Valid folder
result = subprocess.run(["ls", "-l", "project_folder"], capture_output=True, text=True)

# Invalid folder
result1 = subprocess.run(["ls", "-l", "project_folder1"], capture_output=True, text=True)

print("\n[Valid Folder Output]")
print(result.stdout)
print("Return code:", result.returncode)
print("Error (if any):", result.stderr)

print("\n[Invalid Folder Output]")
print("Return code:", result1.returncode)
print("Error:", result1.stderr)

