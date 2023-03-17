text = input()
slov = sorted(set(text))
i = 0
for symbol in slov:
    start = -1
    sum = 0
    while True:
        start = text.find(symbol, start + 1)
        if start == -1:
            break
        sum += len(text[0:start+1]) * len(text[start:len(text)])
    i += 1
    if i == len(slov):
        print(f"{symbol}: {sum}", end='')
    else:
        print(f"{symbol}: {sum}")