import heapq
from heapq import heappush, heappop, heapify

data = {3:'White', 2:'Red', 1:'Green', 5:'Orange', 4:'Yellow', 7:'Purple', 0:'Magenta'}

heap = []
heapq.heapify(heap)

for key, value in data.items():
    heapq.heappush(heap, (key, value))

heapq.heappush(heap, (6, 'Teal'))
heap.sort()

for item in heap:
    print('Key: ', item[0], 'Value: ', item[1])

print('Item 3 contains: ', heap[3][1])
print('The maximum item is: ', heap.nlargest())