# coding:utf-8
# Linked List

# 链表是线性表的一种。线性表是最基本、最简单、也是最常见的一种数据结构。线性表中数据元素之间的关系是一对一的关系，即除了第一个和最后一个数据元素之外，其它数据元素都是首尾相接的。线性表有两种存储方式，一种是顺序存储结构，另一种是链式存储结构。常用的数组就是一种典型的顺序存储结构。

# 相反，链式存储结构就是两个相邻的元素在内存中可能不是相邻的，每一个元素都有一个指针域，指针域一般是存储着到下一个元素的指针。这种存储方式的优点是定点插入和定点删除的时间复杂度为O(1)，不会浪费太多内存，添加元素的时候才会申请内存，删除元素的时候会释放内存。缺点是访问的时间复杂度最坏为O(n)

# 顺序表的特性是随机读取，也就是访问一个元素的时间复杂度是O(1)，链式表的特性是插入和删除的时间复杂度为O(1)

# 链表就是链式存储的线性表。根据指针域的不同，链表分为单向链表、双向链表、循环链表

# 编程实现
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 链表的基本操作
# 反转链表
# 单向链表
# 链表的基本形式是：1->2->3->null，反转需要变成3->2->1->null，这里需要注意：
# 访问某个节点curt.next时，要检验curt是否为null
# 要把反转后的最后一个节点指向null

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    # in python next is a reversed word
    def reverse(self, head):
        prev = None
        while head:  # if head not null,then continue
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


# 双向链表
# 和单向链表的区别在于：双向链表的反转核心在于next和prev域的交换，还需要注意的是当前节点和上一个节点的递推

class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt


# 删除链表中的某个节点
# 删除链表中的某个节点一定要知道这个点的前继节点，所以需要一直有指针指向前继节点。还有一种删除是伪删除，是指复制一个和要删除节点值一样的节点，然后删除，这样就不必知道其真正的前继节点了
# 然后只需要把prev->next=prev->next->next即可。但是由于链表表头可能在这个过程中产生变化，导致我们需要一些特别的技巧去处理这种情况，Dummy Node

# 链表指针的鲁棒性
# 综合上面讨论的来年各种基本操作，链表操作时的鲁棒性问题主要包含两个情况：
# 当访问链表中的某个节点curt.next时，一定要判断curt是否为null
# 全部操作结束后，判断是否有环；若有环，则置其中一端为null

# Dummy Node
# Dummy node是链表问题中一个重要的技巧，中文翻译叫“哑节点”或者“假人头结点”
# Dummy node是一个虚拟节点，也可以认为是标杆节点。Dummy node就是在链表表头head前加一个节点指向head，即dummy->head。Dummy node的使用多针对但链表没有前向指针的问题，保证链表的head不会在删除操作中丢失。除此之外，还有一种用法比较少见，就是使用dummy node来进行head的删除操作，比如Remove Duplicates From Sorted List II，一般的方法current=current.next是无法删除head元素的，所以这个时候如果有一个dummy node在head的前面。

# 所以，当链表的head有可能变化（被修改或者删除）时，使用dummy node可以很好的简化代码，最终返回dummy.next即新的链表

# 快慢指针
# 快慢指针也是一个可以用于很多问题的技巧。所谓快慢指针中的快慢指的是指针向前移动的步长，每次移动的步长较大即为快，步长较小即为慢，常用的快慢指针一般是在单链表中让块指针每次向前移动2，慢指针则每次向前移动1.快慢指针都从链表头开始遍历，于是快指针到达链表末尾的时候慢指针刚好到达中间位置，于是可以得到中间元素的值。快慢指针在链表相关问题中主要有两个应用：

# 快速找出未知长度单链表的中间节点，设置两个指针*fast、*slow都指向单链表的头节点，其中*fast的移动速度是*slow的2倍，当*fast指向末尾节点的时候，*slow就正好在中间了

# 判断单链表是否有环。利用快慢指针的原理，同样设置两个指针*fast、*slow都指向单链表的头节点，其中*fast的移动速度是*slow的2倍。如果*fast=NULL，说明该单链表以NULL结尾，不是循环链表；如果*fast=*slow，则快指针追上慢指针，说明该链表是循环链表

class NodeCircle:
    def __init__(self, val):
        self.val = val
        self.next = None

    def has_circle(self, head):
        slow = head
        fast = head
        while (slow and fast):
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
        if fast and slow and (fast == slow):
            return True
        else:
            return False
