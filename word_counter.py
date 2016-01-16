#-*-coding:utf8;-*-
#qpy:2
#qpy:console
#Prasith Lakshan 08/10/2014

import string 

print "\nA simple word and char counter for text files\n"
print "Please enter the path of the file. \neg : exmplefolder/example.txt\n>"
path = raw_input("Press enter to input path: ")
 
#opening file with read only mode
text = open(path, 'r')
#getting the content of the file
data = text.read()

# initializing variables
lnum = lnum1 = 0
chrn = word = 0
nchr = 0
print '\n\n'

# printing the content in the console
# and doing counts for each line
for ln in string.split(data,'\n'):
    print ln
    
    #line count
    #with empty lines
    lnum1 = lnum1 + 1
    if ln != "":
        lnum = lnum + 1
    
    #char count with spaces
    ch = len(ln)
    chrn = ch + chrn
    #char count without spaces
    nospace = string.count(ln," ")
    nchr = nchr + nospace
    
    #word count
    for p in string.split(ln," "):
        if p != "":
            word = word + 1
# printing the results            
print "\nLines (including empty lines) :",lnum1, \
      "%-30s :" %("\nLines (without empty lines)"),lnum, \
      "%-30s :" %("\nChars (including spaces)"),chrn, \
      "%-30s :" %("\nChars (without spaces)"),chrn-nchr,\
      "%-30s :" %("\nWords"),word
    
