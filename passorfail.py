import time
from time import sleep

def quitA():
    quitA = str(input('do you want to go futher (yes) or (no)'))
    if quitA == 'yes' or quitA == 'Yes':
        return()
    elif quitA == 'no' or quitA == 'No':
        quit()
    else:
        print ('Invalid input, please enter yes or no ')
        quitA()

print('Welcome to Bolton University grading system for computing \n')
quitA()
sleep(2)
print('The purpose of this application is to calculate your grade \n')
quitA()
print('You can Quit this application at anytime')
quitA()
marks = int(input('please insert the marks you recived \n'))
if marks < 40:
    print('you have failed' )
    quitA()
elif marks >= 40:
    print('you have passed ' )
    quitA()
else:
    print("invalid input ")
    quitA()









    
# step 1 welcome them to the grading system
# step 2 tell them to press something to repeat the steps or contine to the next part of the system
# ask them their name 
# ask them for their mark if it is less than 40 print name has failed
# if theu have 40 and over they have passed
# type writer
