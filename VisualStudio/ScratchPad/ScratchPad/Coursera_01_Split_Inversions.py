import numpy as np
import pylab as pl
import matplotlib.pyplot as plot

print (24*60)
t = pl.linspace(0,60,60)
np.random.seed(5)
test = np.random.rand(60)

stack_a = []
stack_b = []

def stack_push(value):
    stack_a.append(value)

def stack_b_push():
    stack_b.append(stack_a.pop())

def stack_pop():
    return stack_a.pop()

def dequeue():
    ret_val = stack_b.pop()
    stack_a.append(stack_b.pop())
    stack_a.append(stack_b.pop())

def fac(n):
    if n <= 0:
        return 1
    return n * fac(n-1)

def fib(n):
    print('entering fib(%s)' % n)
    if n < 3:
        print ("leaving fib(%s) returning 1" % n)
        return 1
    test = (fib(n-1) + fib(n-2))
    print ("leaving fib(%s) returning %d" % (n, test))
    return test

class FibCounter(object):
    def __init__(self):
        self.count = 0
    def get_count():
        return count


test = fib(4)
test2 = fac(4)
test3 = fib(1)

def get_products_of_all_ints_except_at_index(int_array):
    products_of_all_ints_before_index = [1] * len(int_array)
    product = 1
    i = 0
    while i < len(int_array):
        products_of_all_ints_before_index[i] *= product
        product *= int_array[i]
        i += 1
    product = 1
    i = len(int_array) - 1
    while i >= 0:
        products_of_all_ints_before_index[i] *= product
        product *= int_array[i]
        i -= 1
    return products_of_all_ints_before_index

def highest_product(int_array):
    if (len(int_array) < 3):
        raise Exception('less than three items')
    highest = max(int_array[0], int_array[1])
    lowest = min(int_array[0], int_array[1])
    highest_product_of_2 = int_array[0] * int_array[1]
    lowest_product_of_2 = int_array[0] * int_array[1]
    highest_product_of_three = int_array[0] * int_array[1] * int_array[2]
    for element in int_array[2:]:
        highest_product_of_three = max(highest_product_of_three, element * highest_product_of_2, element * lowest_product_of_2)
        highest_product_of_2 = max(highest_product_of_2, element * highest, element * lowest)
        lowest_product_of_2 = min(lowest_product_of_2, element * highest, element * lowest)
        highest = max(highest, element)
        lowest = min(lowest, element)
    return highest_product_of_three  



def count_inversions(a):
  res = 0
  counts = [0]*(len(a)+1)
  rank = { v : i+1 for i, v in enumerate(sorted(a)) }
  for x in reversed(a):
    i = rank[x] - 1
    while i:
      res += counts[i]
      i -= i & -i
    i = rank[x]
    while i <= len(a):
      counts[i] += 1
      i += i & -i
  return res

list_of_lists = []
with open('IntegerArray2.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split('\n')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
        list_of_lists.append(int(inner_list[0]))


import bisect
def solution(A):
    sorted_left = []
    res = 0
    for i in range(1, len(A)):
        bisect.insort_left(sorted_left, A[i-1])
        # i is also the length of sorted_left
        res += (i - bisect.bisect(sorted_left, A[i]))
    return res


def get_second_biggest(numberList):
    candidates = get_candidates(numberList)
    second_biggest = get_max(candidates[1:])
    return second_biggest
    
def get_candidates(numberList):
    split_index = len(numberList) // 2
    if split_index == 0:
        return numberList
    listOne = get_candidates(numberList[:split_index])
    listTwo = get_candidates(numberList[split_index:])
    a = listOne[0]
    b = listTwo[0]
    if a > b:
        listOne.append(b)
        return listOne
    else:
        listTwo.append(a)
        return listTwo

def get_max(numberList):
    biggest = numberList[0]
    for k in numberList[1:]:
        if k > biggest:
            biggest = k
    return biggest

test_list = [123,6,3,2,4,5]
test000 = get_second_biggest(test_list)
kkkk = 1

def mergesort(lst):
    print("running for %s" %lst)
    if len(lst) <= 1:
        return lst, 0
    middle = len(lst) // 2 
    left, a = mergesort(lst[:middle])
    right, b = mergesort(lst[middle:])
    result, c = merge_count_split_inversions(left, right)
    return result, (a + b + c)

def merge_count_split_inversions(left, right):
    result = []
    split_inversions, left_index, right_index = 0, 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            split_inversions += len(left) - left_index
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    print("counted %s inversions for %s and %s" %(split_inversions, left, right))
    return result, split_inversions        


test0 = mergesort(test_list)
test1 = merge_count_inversion(test_list)
test00 = mergesort(list_of_lists)
test2 = count_inversions(list_of_lists)
#test4 = merge_sort(list_of_lists)
test5 = solution(list_of_lists)
test6 = merge_count_inversion(list_of_lists)

test_array = [1,7,3,4]
test = get_products_of_all_ints_except_at_index(test_array)
array_of_ints = [1, 10, -5, 1, -100]
test = highest_product(array_of_ints)

stack_push('a')
stack_push('b')
stack_push('c')
stack_b_push()
stack_b_push()
stack_b_push()
dequeue()
stack_push('d')

#plot.plot(t, test)
#plot.show()
#pl.matplotlib(t,test)