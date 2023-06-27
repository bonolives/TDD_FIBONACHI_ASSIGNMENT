# Defining the Fibonacci Function to run the sequence

def fibonacci(num):
# Fibonacci sequence is a list
    sequence = []
# defining the variables 
    var_1 = 0
    var_2 = 1
    while len(sequence)< num:
        sequence.append(var_1)
        var_1,var_2 = var_2, var_1 + var_2
    return sequence
        