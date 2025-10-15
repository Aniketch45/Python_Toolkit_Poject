def text_analyzer():
    filename = input("Enter filename :- ")
    try:
        with open(filename, 'r') as file:
            text = file.read()          #read the file
            words = text.split()       
            chars = len(text)            #count characters
            aniket=len(words)              #count words
            lines = len(text.splitlines())  #count lines
            unique_words = set(words)       #find unique words.
            #to find the frequency of word
            frequency = {}
            for a in words:
                frequency[a] = frequency.get(a, 0) + 1    # dict.get(key, default)
            print(f"Characters :- {chars}")
            print(f"Words :- {aniket}")
            print(f"Lines :- {lines}")
            print(f"Unique Words :- {unique_words}")
            print(f"Word Frequency :- {frequency}")
    except FileNotFoundError:
        print("File Not Found")
    except TypeError:
        print("File type invalid")