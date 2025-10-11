def read_file():
    filename = input("Enter the file name for the operation :- ")
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")

def write_file():
    filename = input("Enter filename to write :- ")
    text = input("Enter text to write into the file :- ")
    with open(filename, 'w') as f:
        f.write(text)
    print("Text written successfully...!")

def copy_file():
    source = input("Enter source file name from where we have to copyt the data :- ")
    dest = input("Eneter the destination filename where we have to copyt the data :- ")
    try:
        with open(source, 'r') as f:
            data = f.read()
        with open(dest, 'w') as f:
            f.write(data)
        print("File copied successfully...!")
    except FileNotFoundError:
        print("Source file not found")