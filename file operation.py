names = "C:/Users/CareersIT/Desktop/Names.txt" #Path to file name, 
output = "C:/Users/CareersIT/Desktop/Output.txt"

#reading file and displaying result
with open(names, 'r') as file: #This is a way of accessing file in python, r is for reading
    text= file.read() #We are reading this using the read method
    wordCount = len(text.split()) #declare another inter variable, split to ensure it prints each word 
    print(text) 
    print("word count:  ", wordCount)

#writing to a file
with open(output, 'w') as file: #w to write to a file
    line1 = file.write('Careers IT\n')
    line2 = file.write('System Developers\n') #\n means you will write or print on the new line, \t for tab
    line3 = file.write('Assessor - Mr Masiya')
    file.close()