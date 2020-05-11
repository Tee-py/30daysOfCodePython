"""This is a python function that takes a txt file as an argument and reverse the lines
and each text in the line and write it to another file named 'disordered.txt'"""

def reverse_file_lines(file):
    try:
        #opens the ordered file and disordered file
        orderd_file = open(file)
        disordered_file = open('disordered.txt','w')
        #read each lines of the ordered file and assign it to a variable
        orderd_file_lines = orderd_file.readlines()
        #The loop variable i which is the number of lines in the ordered file -1
        i=len(orderd_file_lines)-1
        while i>=0:
            #reverse each lines in the ordered file and write it to another file
            disordered_file.write(orderd_file_lines[i][::-1])
            i-=1
        disordered_file.close()
        disordered_file = open('disordered.txt')
        content = disordered_file.read()
        return content
    except:
        return 'An error occured. Either you passed an invalid argument or your file does not exist in the specified path'

print(reverse_file_lines('ordered.txt'))

