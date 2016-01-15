# an app to calculate the 'n'th Fibonacci number as an exercise 
# by Prasith 
#-*-coding:utf8;-*-

def main():
   
    print
    print "This app will calculate the 'n'th Fibonacci number. "
    main2()
def main2():
    print
    n = int(raw_input("Please enter the value of'n': "))
    print
    x=1L
    y=0L 
    for i in range((n+1)/2):
        x = x + y
        y = x + y
    if n % 2 == 0:    
        print y
        print
    else:
        print x
        print

    inp = raw_input("to try again type 'y', to exit just press enter: ")
    if inp == 'y':
        main2()
    else:
       print
       print "Goodbye then! "
       print
main()
