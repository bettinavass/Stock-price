# with open("/Users/Betka/Desktop/PythonTeaching/Week5/test.txt", "r") as f:
    
#     print(f.read() + " Betka")

# with open("/Users/Betka/Desktop/PythonTeaching/Week5/test.txt", "r") as f:
    
#     f_contents = f.read()
#     f_contents = f_contents.replace("\n","")
#     f_contents = f_contents.replace(" ", "")

#     print(f_contents)
longest_line = ""
longest_length = 0

with open("/Users/Betka/Desktop/PythonTeaching/Week5/test.txt", "r") as f:
    for line.strip() in f.readlines():
        length = len(line.strip())
        if length > longest_length:
            longest_line = line
            longest_length = len(line)

print("Longest word is '{0}' of length {1}".format(longest_line, longest_length))
