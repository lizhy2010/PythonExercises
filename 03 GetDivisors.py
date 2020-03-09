num = input('Enter a number: ')

divs = range(2, int(num) + 1)

print('\nList of Divisors:')

for div in divs:
    if int(num) % div == 0:
        print(div)