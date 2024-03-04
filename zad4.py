number = int(input('Enter a number: '))
count = 0
for i in range(2, number-1):
    if number % i == 0:
        count += 1
if count == 0:
    print('Prime number')
else:
    print('Not Prime number')