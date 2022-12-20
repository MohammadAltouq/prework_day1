# question1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("hello_" + user_name)
    return

# question2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for x in range(1,101):
        if x % 2 != 0:
            print(x)
    return

# question3 Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    num = max(a_list)
    return num

# question4 Write a function to return if the given year is a leap year. (boolean)
def is_leap_year(a_year):
    leap = False
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            leap = True
        elif a_year % 400 ==0:
            leap = True
    return leap

# question5 Write a function to check to see if all numbers in list are consecutive numbers.(boolean)
def is_consecutive(a_list):
    j = 0
    consecutive = True
    for i in range(1 , len(a_list)):   
        if a_list[j] + 1 != a_list[i]:
            consecutive = False
        j =j + 1
    return consecutive
  