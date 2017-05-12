# coding:utf-8
# Stack - 栈
# 栈是一种LIFO（Last In First Out）的数据结构，常用方法有添加元素，取栈顶元素，弹出栈顶元素，判断栈是否为空

stack = []
len(stack)  # size of stack

# more efficient stack
import collections

stack = collections.deque()

# list作为最基本的python数据结构之一，可以很轻松的实现stack。如果需要更高效的stack，建议使用deque

# len(stack) !=0 --- 判断stack是否为空
# stack[-1] --- 取栈顶元素，不移除
# pop() --- 移除栈顶元素并返回该元素
# append(item) --- 向栈顶添加元素

