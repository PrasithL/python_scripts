# age counter
# by prasith 11/09/2014

import time

def main():
    
    print ("\n\nThis programme will calculate your age.\n(Accuracy: +/- 1 Day)")
    main2()
    
def main2():

    print ("\nEnter your birth year, month and date seperated by commas. eg:1999,5,21: ")
    Y1 , M1 , D1 = input(">")
    if Y1 < 1914:
        print ("\nWoah, Are you a ghost!!!??\nanyway here's your age, ")
        
    if Y1 > int((time.strftime("%Y"))) :
        print ("\nGreetings! Time traveller...! \nbut sorry,no calculations for you. Next!")
        main2()
        
    if M1<0 or M1>13:
        print ("\nThere are only 12 months! \nplease try again. ")
        main2()
      
    if D1<0 or D1>31:
        print ("\nThe date you entered is incorrect. \nPlease try again. ")
        main2()
    
    Y2 = int((time.strftime("%Y")))
    M2 = int((time.strftime("%m")))
    D2 = int((time.strftime("%d")))
   
    #calculate Years
    Y = Y2 - Y1
    
    #calculate months
    if M1 > M2:
       M = (13 - M1) + ( M2 - 1)
       Y = Y - 1
    else:
       M = M2 - M1
       
    #calculate days
    if D1 > D2:
     if M2 == 3:
       D = (28 - D1) + (D2)
     else:
       D = (30 - D1) + ( D2)
       
     if M > 0:
           M = M - 1
           
     else:
           M = 11
           Y = Y - 1
    else:
       D = D2 - D1
   
    # The above calculations were made assuming
    # a month only has 30 days(28 for February).
    
    print "\n",Y, "Years", M, "Months", D,"Days\n"
    inp = raw_input("type 'y' to Check another or press 'enter' to exit: ")
    if inp == 'y':
        main2()
main()
