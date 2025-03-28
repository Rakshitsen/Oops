try:
    file = open("data.txt", "r")
    content=file.read()
    print(content)

except FileNotFoundError:
    print("Error: File not found!")

finally:
    print("Closing file (if opened)...")
    try:
        file.close()  # Attempt to close the file safely
    except NameError:
        print("File was never opened.")
