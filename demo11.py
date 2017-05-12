# coding:utf-8
# Basics Sorting - 基础排序算法
# 算法 --- 排序
# 算法分析
# 1.时间复杂度-执行时间（比较交换次数）
# 2.空间复杂度-所消耗的额外内存空间
# 使用小堆栈或表
# 使用链表或指针、数组索引来代表数据
# 排序数据的副本

# 对具有重键的数据（同一数组按不同键多次排序）进行排序时，需要考虑排序方法的稳定性，在非稳定性排序算法中需要稳定性时可考虑加入小索引

# 稳定性：如果排序后文件中拥有相同键的项的相对位置不变，这种排序方式是稳定的。

# 常见的排序算法根据是否需要比较可以分为如下几类：
# 1.Comparison Sorting
# Bubble Sort
# Selection Sort
# Insertion Sort
# Shell Sort
# Merge Sort
# Quck Sort
# Heap Sort

# 2.Bucket Sort
# 3.Counting Sort
# 4.Radix Sort

# 从稳定性角度考虑可分为：稳定、非稳定

# 七大经典排序算法

# 一、冒泡排序 BubbleSort
# 介绍：重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来
# 步骤：
# 1.比较相邻的元素。如果第一个比第二个大，就交换他们两个
# 2.对第0个到第n-1个数据做同样的工作，这时，最大的数就“浮”到了数组最后的位置上
# 3.针对所有的元素重复以上的步骤，除了最后一个
# 4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较

def bubble_sort(arry):
    n = len(arry)
    for i in range(n):  # 0-n-1
        for j in range(1, n - i):
            if arry[j - 1] > arry[j]:
                arry[j - 1], arry[j] = arry[j], arry[j - 1]
    return arry


# 优化1：某趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了，用一个标记记录这个状态即可

def bubble_sort2(arry):
    n = len(arry)
    for i in range(n):
        flag = 1  # 标记
        for j in range(1, n - i):
            if arry[j - 1] > arry[j]:
                arry[j - 1], arry[j] = arry[j], arry[j - 1]
                flag = 0
        if flag:  # flag=0全排好序了，直接跳出
            break
    return arry


# 优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。因此通过记录最后发生数据交换的位置就可以确定下次循环的范围

def bubble_sort3(arry):
    n = len(arry)
    k = n
    for i in range(n):
        flag = 1
        for j in range(1, k):
            if arry[j - 1] > arry[j]:
                arry[j - 1], arry[j] = arry[j], arry[j - 1]
                k = j
                flag = 0
        if flag:
            break
    return arry


# 二、选择排序SelectionSort
# 步骤：
# 1.在未排序序列中找到最小(大)元素，存放到排序序列起始位置
# 2.再从剩余未排序元素中继续寻找最小(大)元素，然后放到已排序序列的末尾
# 3.以此类推，知道所有元素均排序完毕

def select_sort(ary):
    n = len(ary)
    for i in range(0, n):
        min = i  # 最小元素下标标记
        for j in range(i + 1, n):
            if ary[j] < ary[min]:
                min = j  # 找到最小值的下标
        ary[min], ary[i] = ary[i], ary[min]  # 交换
    return ary


# 三、插入排序InsertionSort
# 工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
# 步骤：
# 1.从第一个元素开始，该元素可以认为已经被排序
# 2.取出下一个元素，在已经排序的元素序列中从后向前扫描
# 3.如果被扫描的元素（已排序）大于新元素，将该元素后移一位
# 4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 5.将新元素插入到该位置后
# 6.重复步骤2-5

def insert_sort(ary):
    n = len(ary)
    for i in range(1, n):
        if ary[i] < ary[i - 1]:
            temp = ary[i]
            index = i  # 待插入的下标
            for j in range(i - 1, -1):  # 从i-1循环到0（包括0）
                if ary[j] > temp:
                    ary[j + 1] = ary[j]
                    index = j  # 记录待插入的下标
                else:
                    break
            ary[index] = temp
    return ary


# 四、希尔排序ShellSort
# 希尔排序也称递减增量排序算法，实质是分组插入排序，是非稳定排序算法
# 基本思想：将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长，列数更少）来进行。最后整个表就只有一列。算法本身还是使用数组进行排序

def shell_sort(ary):
    n = len(ary)
    gap = round(n / 2) #初始步长，用round四舍五入取整

    while gap > 0:
        for i in range(gap, n):
            temp = ary[i]
            j = i
            while (j >= gap and ary[j - gap] > temp):
                ary[j] = ary[j - gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap / 2)
    return ary
