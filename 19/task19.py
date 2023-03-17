def push_heap(heap, x):
    heap.append(x)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos-1)//2]:
        heap[pos], heap[(pos-1)//2] = heap[(pos-1)//2], heap[pos]
        pos = (pos-1)//2


def pop_heap(heap):
    ans = heap[0]
    heap[0] = heap[-1]
    pos = 0
    while pos*2 + 2 < len(heap):
        max_son_index = pos * 2 + 1
        if heap[pos * 2 + 2] > heap[max_son_index]:
            max_son_index = pos * 2 + 2
        if heap[pos] < heap[max_son_index]:
            heap[pos], heap[max_son_index] = heap[max_son_index], heap[pos]
            pos = max_son_index
        else:
            break
    heap.pop()
    return ans


with open('input.txt', 'r') as file:
    n = int(file.readline())
    stack = []
    for i in range(n):
        line = file.readline()
        if line[0] == '0':
            line = line.split()
            push_heap(stack, int(line[1]))
        else:
            print(pop_heap(stack))