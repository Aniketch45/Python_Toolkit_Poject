from text_utils import text_analyzer                #import text_analyzer from text_utils
from math_utils import prime_checker, factorial_calculator, fibonacci, gcd_lcm
from file_utils import read_file, write_file, copy_file
from list_utils import list_op, dictionary_op

def main_menu():
    while True:
        print("\n -- Python Utility Toolkit -- \n")
        print("1. Text Analyzer")
        print("2. Math Tool")
        print("3. File Manager")
        print("4. Data Conversion (CSV OR JSON)")
        print("5. List & Dictionary Manager")
        print("0. Exit")

        choice = input("Enter your choice :- ")

        if choice == '1':
            text_analyzer()
        elif choice == '2':
            math_tool_menu()
        elif choice == '3':
            file_menu()
        # elif choice == '4':
        # #operation to be perform
        elif choice == '5':
            list_dict_menu()
        elif choice == '0':
            print("You are Exiting... Thank you..!")
            break
        else:
            print("Invalid Choice .. Try again with correct choice .. !")

def math_tool_menu():
    print("\n Math Tools")
    print("1. Prime number checker")
    print("2. Factorial Calculator ")
    print("3. Fibonacci Series")
    print("4. GCD/LCM Calculator")
    choice = input("Choose your option from above :- ")
    if choice == '1':
        prime_checker()
    elif choice == '2':
        factorial_calculator()
    elif choice == '3':
        fibonacci() 
    elif choice == '4':
        gcd_lcm()
    else:
        print("Invalid Choice for math tool...")

def file_menu():
    print("\n File Manager")
    print("1. Read File")
    print("2. Write File")
    print("3. Copy File")
    choice = input("Choose your option for the operation on file :- ")
    if choice == '1':
        read_file()
    elif choice == '2':
        write_file()
    elif choice == '3':
        copy_file()
    else:
        print("Invalid choice for file operations.")

def list_dict_menu():
    print("\n List & Dictionary Manager")
    print("1. List Operations ")
    print("2. Dictionary Operation5 ")
    choice = input("Choose you option from above :- ")
    if choice == '1':
        list_op()
    elif choice == '2':
        dictionary_op()
    else:
        print("Invalid choice for list & dictionary operation")

#controller to control the project or other files
if __name__ == "__main__":
    main_menu() 