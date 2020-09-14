    #     Fake Multiplication Table
    #
    # Rohan Das is a fraud by nature.
    # Rohan Das wrote a python function to print a multioplication table of a given number and
    # put one of the values (randomly generated) as wrong. Rohan Das did this to fool his clasmates
    # and make them commit a mistake in a test. You cannot tolerate this ! So you decided to use python
    # skills to counter Rohan's actions by writing a program that validates rohan's multiplication
    #
    # Your function should be able to find wrong values in Rohan's table and expose Rohan Das as a fraud.
    #
    # Note : Rohan's function returns a list of numbers
    #
    # Input :
    # rohan_multiplications(6)
    # Output :
    # [6, 12, 18, 26, ... , 60]

import random
def rohanmultiplication(number):
    wrong = random.randint(0,9)
    table = [i * number for i in range(1,11)]
    table[wrong] = table[wrong] + random.randint(1,8)
    return table

def iscorrect(table, number):
    for i in range(1,11):
        if table[i-1] != i*number:
            return i-1

    return None
if __name__ == '__main__':
   # print(rohanmultiplication(7)
    number = int(input("Enter a number: "))
    myTable = rohanmultiplication(number)
    print(myTable)
    wrongIndex = iscorrect(myTable, number)
    print(f"the table is wrong at index {wrongIndex}")
    
