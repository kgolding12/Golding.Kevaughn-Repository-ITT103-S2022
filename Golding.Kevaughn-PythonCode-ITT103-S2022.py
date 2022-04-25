"""JamEx Limited requires a program to calculate and print the commission received by a
salesperson. The program should process an undetermined number of salespersons and
appropriately terminate by a predefined input. The commission rate is based on two factors,
the amount of sales and the class to which a salesperson belongs. The input will be the
salesperson number, sales amount and class. The commission rate will be based on the
following criteria:

Class=1
If sales is equal to or less than $1000, the rate is 6 percent.
If sales is greater than $1000 but less than $2000, the rate is 7 percent.
If the sales is $2000 or greater, the rate is 10 percent.

Class=2
If the sales is less than $1000, the rate is 4 percent.
If the sales is $1000 or greater, the rate is 6 percent.

Class=3
The rate is 4.5 percent for all sales amount

Class=any other value
Output an appropriate error message.
"""

"""
Author: Kevaughn Golding
Date Created: 03/28/2022
Course: ITT103
Purpose: To calculate and output the commission received by an undefined number of salespersons based 
on certain input and criteria. 
"""

class1a_rate = 0.06 # if sales is equal to or less than $1000
class1b_rate = 0.07 # if sales is greater than $1000 but less than $2000
class1c_rate = 0.10 # if the sales is $2000 or greater
class2a_rate = 0.04 # if the sales is less than $1000
class2b_rate = 0.06 # if the sales is $1000 or greater
class3_rate = 0.045 # rate for all sales amount in class 3

commission_rate = 0 #initialization

def output_results(number, salesclass, amount, rate):   
    """
    This is a function used to output the commission rate and 
    other relevant details of the salesperson. It also rounds the 
    commission rate to 2 decimal places.
    """
    print("------------------------------------------")
    print("\nSalesperson Number: " + number)
    print("Salesperson Class: " + str(salesclass))
    print("Salesperson Sales Amount: $" + str(amount))
    print("Salesperson Commission Rate: $" + str(round(rate, 2)))
    print("\n------------------------------------------")
    
while True:
    while True: # loop created for input validation
        message = input("If you would like to stop, enter exit. To continue, enter 1: ")
        if message == '1':
            break           
        elif message == 'Exit' or message == 'exit':
            print("Program has ended.")
            break
        else:
            print("Incorrect input! Try again.\n")
    
    if message == 'Exit' or message == 'exit':
        break # this breaks out of the outermost loop if exit is entered
    
    salesperson_number = input("\nPlease enter the salesperson\'s number: ")
    sales_amount = int(input("\nPlease enter their sales amount: "))
    
    while True:
        try:
            salesperson_class = int(input("\nPlease enter their class: "))      
        except ValueError:
            print("Invalid input! Try again.")
            # returns to the start of the loop because of wrong input
            continue
        if salesperson_class < 1 or salesperson_class > 3:
            print("Enter one value! 1, 2 or 3.")  
        else:    
            # sales was successfully parsed! exit the loop
            break
        
    if salesperson_class == 1:
        if sales_amount <= 1000:
            commission_rate = class1a_rate * sales_amount
        elif sales_amount > 1000 and sales_amount < 2000:
            commission_rate = class1b_rate * sales_amount
        elif sales_amount >= 2000:
            commission_rate = class1c_rate * sales_amount

    if salesperson_class == 2:
        if sales_amount < 1000:
            commission_rate = class2a_rate * sales_amount
        elif sales_amount >= 1000:
            commission_rate = class2b_rate * sales_amount

    if salesperson_class == 3:
        commission_rate = class3_rate * sales_amount
    
    output_results(salesperson_number, salesperson_class, sales_amount, commission_rate)
