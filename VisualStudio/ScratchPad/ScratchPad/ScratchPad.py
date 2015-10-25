import random

m = 0

class CounterClass(object):
    def __init__(self):
        self.counter = 0
    def add_counter(self):
        self.counter+=1
    def get_counter(self):
        return self.counter

def partition(array, begin, end):
    pivot = begin
    m += end - begin - 1
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i] = array[pivot]
            array[pivot] = array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

#alist = [9, 4, 3, 1, 6, 8, 2, 0]
#quicksort(alist)
#print("----O-u-t-p-u-t-----")
#print(alist)

list_of_lists = []
with open('IntegerArray2.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split('\n')]
        list_of_lists.append(int(inner_list[0]))

quicksort(list_of_lists)
print ("and this is ")
print(m)
