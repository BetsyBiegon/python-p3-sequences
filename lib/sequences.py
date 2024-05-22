#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return

    fibonacci = [0]
    if length > 1:
        fibonacci.append(1)
        for i in range(2, length):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci)
