# question one: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of code has been defined as below. 
def hello_name(user_name):
    """This prints out hello_USERNAME"""
    print("hello_" + user_name.upper() + "!")
hello_name("username")

# question two: Write a python function, first_odds that prints the odd numbers from 1-100 and retruns nothing.
def first_odds():
    """Prints out the odd numbers to 100"""
    # create a range from 1 to 100 and set step to skip
    x = range(1,101,2)
    # for loop to print out odds
    for i in x:
        print(i)
first_odds()

# question three: Please write a Python function, max_num_in_list to retrun the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """Prints out the max number in a list"""
   # set a varible to start at the beginning of a list
    maximum = a_list[0]
    # create a loop to check all of the numbers
    for num in a_list:
        # create an if statement 
        if num > maximum:
            maximum = num
            #need it to return the value
    return maximum
print(max_num_in_list([1,654,849864,24168,25,3416]))

# Question 4: Write a function to return if the given year is a leap year. A leap year is divisble by 4 but not divisbile by 100 unless it is also divisivle by 400. The retrun should be boolean type. 
def is_leap_year(a_year):
    """Tells you if a year is a leap year."""
    if (a_year % 4) == 0:
        if(a_year % 100) ==0:
            if(a_year % 400) == 0:
                print(True)
            else:
                print(False)
    return(a_year)

is_leap_year(2000) #2000 was a leap year!! 

# Question five: Write a function to check to see if all numbers in list are consecutive numbers. For example [2,3,4,5,6] are consecutive. The return should be boolean.
def is_consecutive(a_list):
    """This will tell if a list is consecutive"""
    maximum = max(a_list)
    if sum(a_list) == maximum * (maximum+1) /2:
        return True
    else:
        return False
numbers = [1,2,3,4,5,6,10,15]
print(is_consecutive(numbers))