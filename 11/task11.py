from collections import deque

class Stack:
    stack = deque()

    def push(self, item):
        self.stack.append(item)
        print('ok')

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return 'error'

    def back(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 'error'

    def size(self):
        return len(self.stack)

    def clear(self):
        while len(self.stack) > 0:
            self.stack.pop()
        print('ok')


with open('input.txt', 'r') as file:
    text = file.read().split()
    stack = Stack()
    i = 0
    while i < len(text):
        if text[i] == 'push':
            stack.push(int(text[i+1]))
            i += 1
        elif text[i] == 'pop':
            print(stack.pop())
        elif text[i] == 'back':
            print(stack.back())
        elif text[i] == 'size':
            print(stack.size())
        elif text[i] == 'clear':
            stack.clear()
        elif text[i] == 'exit':
            print('bye')
            break
        i += 1