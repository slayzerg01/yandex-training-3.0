text = open('input.txt', 'r').read()
text = text.replace(' ','')
text = text.replace('\n','')
set_text = sorted(set(text))
col = []
for item in set_text:
    col.append(text.count(item))
for i in range(max(col)):
    for j in range(len(set_text)):
        if max(col)-i<=col[j]:
            print("#", end='')
        else:
            print(" ", end='')
    print()
print(''.join(set_text))