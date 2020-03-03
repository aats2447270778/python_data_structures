
# 拼接
def test1():
    list1 = []
    for i in range(1000):
        list1 = list1 + [i]

# append方式
def test2():
    list1 = []
    for i in range(1000):
        list1.append(i)

# 列表的推导式
def test3():
    list1 = [i for i in range(1000)]


def test4():
    list1 = list(range(1000))

from timeit import Timer

t1 = Timer('test1()','from __main__ import test1')
print('contact',t1.timeit(number=1000),'毫秒')
t2 = Timer("test2()", "from __main__ import test2")
print("append",t2.timeit(number=1000), "毫秒")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "毫秒")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "毫秒")



# list的操作测试
# def test1():
#    l = []
#    for i in range(1000):
#       l = l + [i]
# def test2():
#    l = []
#    for i in range(1000):
#       l.append(i)           #O(1)
# def test3():
#    l = [i for i in range(1000)]
# def test4():
#    l = list(range(1000))
#
# from timeit import Timer
#
# t1 = Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "seconds")
# t2 = Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000), "seconds")
# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000), "seconds")
# t4 = Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000), "seconds")
#
# # ('concat ', 1.7890608310699463, 'seconds')
# # ('append ', 0.13796091079711914, 'seconds')
# # ('comprehension ', 0.05671119689941406, 'seconds')
# # ('list range ', 0.014147043228149414, 'seconds')
# x = range(2000000)
# pop_zero = Timer("x.pop(0)","from __main__ import x")
# print("pop_zero ",pop_zero.timeit(number=1000), "seconds")
# x = range(2000000)
# pop_end = Timer("x.pop()","from __main__ import x")
# print("pop_end ",pop_end.timeit(number=1000), "seconds")
#
# # ('pop_zero ', 1.9101738929748535, 'seconds')
# # ('pop_end ', 0.00023603439331054688, 'seconds')


