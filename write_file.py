#In this snippet we are going to write some text to a file

def write_file():
    print('Enter a huge load of text:')
    user_input = input()
    file_name = 'written.txt'
    file = open(file_name, 'w')
    return file.write(user_input)


#This function reads the content just written into the file
def read_file():

    #we first call the function that writes the file
    write_file()
    file = open('written.txt', 'r')
    content = file.read()

    print('\n\nThis is the content in the file:')
    return print(content)

read_file()