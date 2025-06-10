
entry1=str(input('Enter text to the file: '))


file1=open('output.txt','w')
writing=file1.write(entry1)
print('Data successfully written to output.txt')
file1.close()


entry2=str(input('Enter additional text to append:'))

file1=open('output.txt','a')
appending=file1.write('\n'+entry2)
print('Data successfully appended.')
file1.close()

file1=open('output.txt','r')
readingfile=file1.read()
print(readingfile)
file1.close()