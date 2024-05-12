#In this snippet we read the content of a file using a simple function

def read_file():
    file_name = 'file.txt'
    text = open(file_name, 'r')
    content = text.read()

    # print the contents of the file
    return print(content)

read_file()