file_path ="C:\Users\\torraken000\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\myFile.txt"
try:
    stream = open(file_path)
    stream.write('This is the first message!\n')
    stream.write('This is the second message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)

##YOUDO rest of the program for reading and printing to the console
##remember pass in file_path to open 