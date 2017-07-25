
def is_palindrome(value):
    return value == int(str(value)[::-1])

max_pal = 0
max_a = 0
max_b = 0

for a in range (999, 99, -1):
        for b in range(a, 99, -1):
            result = a*b
            if is_palindrome(result) and result > max_pal:
                max_pal = result
                max_a = a
                max_b = b
            if max_b > b:
                break
    
print('Maximal palindrome is %d with next values:\n %d \n %d' % (max_pal, max_a, max_b))
