count = 0
for number in range(1, 10000):
    d = []
    s = 0
    for divider in range(1, (number//2)+1):
        if number % divider == 0:
            d.append(divider)
    for k in range(0, len(d)):
        s += d[k]
    if number == s:
        count += 1
print(count)
