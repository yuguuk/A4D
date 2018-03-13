import queue

MyQ = queue.Queue(3)

print("Queue is empty: ", MyQ.empty())

MyQ.put(1)
MyQ.put(2)
MyQ.put(3)
print("Queue full: ", MyQ.full())

print("Popping: ", MyQ.get())
print("Queue full: ", MyQ.full())

print("Popping: ", MyQ.get())
print("Popping: ", MyQ.get())
print("Queue empty: ", MyQ.empty())