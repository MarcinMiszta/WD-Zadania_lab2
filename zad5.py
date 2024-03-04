count = 0
for number in range(1, 1000):
    d = []
    s = 0
    for divider in range(1, number):
        if number % divider == 0:
            d.append(divider)
    for k in range(0, len(d)):
        s += d[k]
    if number == s:
        count += 1
print(count)
