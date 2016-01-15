#-*-coding:utf8;-*-
#qpy:2
#qpy:console
#Prasith Lakshan 08/10/2014

import string 

print "\nA simple word and char counter for text files\n"
print "Please enter the path of the file. \neg : exmplefolder/example.txt\n>"
path = raw_input("Press enter to input path: ")
 

text = open(path, 'r')
data = text.read()

lnum = lnum1 = 0
chrn = word = 0
nchr = 0
print '\n\n'

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
            
print "\nLines (including empty lines) :",lnum1, \
      "%-30s :" %("\nLines (without empty lines)"),lnum, \
      "%-30s :" %("\nChars (including spaces)"),chrn, \
      "%-30s :" %("\nChars (without spaces)"),chrn-nchr,\
      "%-30s :" %("\nWords"),word
    
