n = int(input())
train = []

for i in range(n):
    operation = input().split()

    if operation[0] == 'add':
        count, product = int(operation[1]), operation[2]
        train.extend([(product, count)])
    elif operation[0] == 'delete':
        count = int(operation[1])
        while count > 0 and train:
            if count >= train[-1][1]:
                count -= train.pop()[1]
            else:
                train[-1] = (train[-1][0], train[-1][1]-count)
                count = 0
    elif operation[0] == 'get':
        product = operation[1]
        count = sum([item[1] for item in train if item[0] == product])
        print(count)
