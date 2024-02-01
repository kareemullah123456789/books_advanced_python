# Write your code here :-)

a_section =open(r'H:\xx.txt')
see_output = a_section.readlines()
a_section.close()

print('\n\n content available of the file is:\n\n',see_output)

see_output.sort()

sortedlist2 = open(r'H:\new_A.txt','w')

sortedlist2.writelines(see_output)

sortedlist2.close()
print('\n\n Sorted content is :\n\n',see_output)
