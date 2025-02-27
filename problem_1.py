"""
If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 100.
"""

def sum_of_multiples_of_3_or_5(num_range):
    sum = 0
    for i in range(num_range):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        else:
            continue

    return sum

sum = sum_of_multiples_of_3_or_5(1000)
print(sum)