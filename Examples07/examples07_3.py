#数据结构

#队列(Queue)
from queue import Queue

queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())  # 输出: 1
print(queue.get())  # 输出: 2
print(queue.get())  # 输出: 3