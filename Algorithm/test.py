import sys

mylist = range(0,10000)
print(sys.getsizeof(mylist))

x = [i for i in range(0,10000)]
print(sys.getsizeof(x))