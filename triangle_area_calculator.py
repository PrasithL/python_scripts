# programme to calculate the Area of a triangle as an exercise 
# by Prasith 

#qpy:console
#qpy:2 

import math

def main():
    print
    print "This app will Calculate the Area of a triangle based on the lengths of it's sides."
    print
    a, b, c = input("Please enter the lengths of the sides separated by a coma (a,b,c): ")
    s = (a + b + c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    A = format(A, '.3f')
    print "The area of the triangle is",A
    print
    inp = raw_input('Wanna try again (y/n)? ')
    if inp == 'y':
      main()
    
main()
