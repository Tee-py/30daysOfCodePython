#opens the ordered file and disordered file
init_file = open('ordered.txt')
output_file = open('disordered.txt','w')
#read each lines of the ordered file and assign it to a variable
init_file_content_list = init_file.readlines()
#The loop variable i which is the number of lines in the ordered file -1
i=len(init_file_content_list)-1
while i>=0:
#reverse each lines in the ordered file and write it to another file
    reversed_text = orderd_file_lines[i][::-1]
    output_file.write(reversed_text)
    i-=1
output_file.close()
output_file = open('disordered.txt')
content = output_file.read()
print(content)