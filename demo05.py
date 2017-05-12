# coding:utf-8
# Queue是一个FIFO的数据结构，并发中使用的较多，可以安全地将对象从一个任务传给另一个任务
# Queue和Stack在Python中都是有list，[]实现的。在python中list是一个dynamic array，可以通过append在list尾部添加元素，通过pop()在list的尾部弹出元素实现Stack的FILO，如果是pop(0)则弹出头部的元素实现Queue的FIFO

queue = []  # same as list()
size = len(queue)
queue.append(1)  # insert
queue.append(2)
print(queue)  # [1,2]
queue.pop(0)  # remove
print(queue)  # [2]

print(queue[0])  # 2

# Priority Queue - 优先队列
# 应用程序常常需要处理带有优先级的业务，优先级最高的业务首先得到服务。因此优先队列这种数据结构应运而生。优先队列中的每个元素都有各自的优先级，优先级最高的元素最先得到服务；优先级相同的元素按照其在优先队列中的顺序得到服务。
# 优先队列可以使用数组或链表实现，从时间和空间复杂度来说，往往用二叉树来实现

# python中提供heapq的lib来实现priority queue，提供push和pop两个基本操作和heapify初始化操作

# \        methods              time complexity
# enqueue  heapq.push(queue,e)  O(log n)
# dequeue  heapq.pop(queue)     O(log n)
# init     heapq.heapify(queue) O(nlog n)
# peek     queue[0]             O(1)

# Deque - 双端队列
# 双端队列（deque,double-ended queue）可以在任何一端添加或者移除元素，因此它是一种具有队列和栈性质的数据结构

# python的list就可以执行类似于deque的操作，但是效率过于慢。为了提升数据的处理效率，一些高效的数据结构放在了collections中。在collections中提供了deque的类，如果需要多次对list执行头尾元素的操作，请使用deque
# dq = collections.deque();

# \             methods           time complexity
# enqueue left  dq.appendleft(e)  O(1)
# enqueue right dq.append(e)      O(1)
# dequeue left  dq.popleft()      O(1)
# dequeue right dq.pop()          O(1)
# peek left     dq[0]             O(1)
# peek right    dq[-1]            O(1)
