
'''
Given an integer input as the Nth value, the objective is to Find the Fibonacci Series up to the Nth Term using Loops and Recursion. The objective is to print all the number of the Fibonacci series until the Nth term given as an input. Here are some of the methods to solve the above mentioned problem

Method 1: Using Simple Iteration
Method 2: Using Recursive Function
Method 3: Using direct formulae

Method 1: Using Simple Iteration
In this method well use loops to iterate through and form the series up to the integer input N as the range.
To print the series up to the Nth term we start a loop from 2 to 
the Nth term as 0 and 1 are the seed values for forming the series.

# Python program to display the Fibonacci sequence

def fabnn(n):
    n1 = 0
    n2 =  1
#print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(0, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    #print(n3, end=" ")
    return "Fibonacci Series:", n1, n2,
    #return [ n1,n2,n3, ]

'''