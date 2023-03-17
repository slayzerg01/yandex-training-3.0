from collections import deque

class Stack:
    stack = deque()

    def push_back(self, item):
        self.stack.append(item)
        print('ok')

    def push_front(self, item):
        self.stack.appendleft(item)
        print('ok')

    def pop_front(self):
        if len(self.stack) > 0:
            return self.stack.popleft()
        else:
            return 'error'

    def pop_back(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return 'error'

    def front(self):
        if len(self.stack) > 0:
            return self.stack[0]
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
        self.stack.clear()
        print('ok')


with open('input.txt', 'r') as file:
    text = file.read().split()
    stack = Stack()
    i = 0
    while i < len(text):
        if text[i] == 'push_back':
            stack.push_back(int(text[i+1]))
            i += 1
        elif text[i] == 'push_front':
            stack.push_front(int(text[i + 1]))
            i += 1
        elif text[i] == 'pop_front':
            print(stack.pop_front())
        elif text[i] == 'pop_back':
            print(stack.pop_back())
        elif text[i] == 'front':
            print(stack.front())
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