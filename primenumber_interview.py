# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:55:25 2026

@author: bar8s
"""

import math 
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = []
for num in range(500, 600):
    if is_prime(num):
        prime_numbers.append(num)
        
prime_str = ", ".join(map(str, prime_numbers))
print(f"{prime_str} are the 3 digits prime numbers that start with 5")

