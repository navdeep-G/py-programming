# sorts.py
#    Implementations of selection sort and merge sort.

def selSort(lst):
    n = len(lst)
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1,n):
            if lst[i] < lst[mp]:
                mp = i
        lst[bottom], lst[mp] = lst[mp], lst[bottom]

def merge(lst1, lst2, lst3):
    # merge sorted lists lst1 and lst2 into lst3
    # these indexes keep track of current position in each list
    i1 = i2 = i3 = 0
    n1, n2 = len(lst1), len(lst2)

    # Loop while both pieces have data
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:     # copy from lst1
            lst3[i3] = lst1[i1]     
            i1 = i1 + 1
        else:                       # copy from list2
            lst3[i3] = lst2[i2]     
            i2 = i2 + 1
        i3 = i3 + 1                 # item added to lst3

    # Here either lst1 or lst2 is done, One of the following loops will
    # execute to finish up the merge.
    
    # Copy remaining items (if any) from lst1
    while i1 < len(lst1):
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    # Copy remaining items (if any) from lst2
    while i2 < len(lst2):
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

def mergeSort(lst):
    # Put items of lst in ascending order
    n = len(lst)
    # Do nothing is lst contains 0 or 1 items
    if n > 1:
        # split into two sublists
        m = n // 2
        lst1, lst2 = lst[:m], lst[m:]
        # recursively sort each piece
        mergeSort(lst1)
        mergeSort(lst2)
        # merge the sorted pieces
        merge(lst1, lst2, lst)


## Functions for timing sorts
        
## Example:
## >>> from sorts import *
## >>> timingCurve(mergeSort, 1000, 2000, 5000, 5)
## List size:  1000
## 0
## 1
## 2
## 3
## 4
## avg = 0.2
## List size:  3000
## 0
## 1
## 2
## 3
## 4
## avg = 0.8
## [0.234578800201, 0.765318417549]

import random, time

def genList(n):
    # RETURNS a list of n random floats
    xs = []
    for i in range(n):
        xs.append(random.random())
    return xs

def timeSort(sortFn, n):
    # RETURNS the time it takes to sort a random list of size n
    #    using the given sorting function sortFn
    xs = genList(n)
    t1 = time.time()
    sortFn(xs)
    t2 = time.time()
    return t2 - t1

def timingCurve(sortFn, start, inc, stop, trials):
    # RETURNS a list representing the average time required to sort
    #     lists of sizes start, start+inc, start+2*inc, ..., stop.
    times = []
    for n in range(start, stop, inc):
        print("List size: ", n)
        sum = 0.0
        for i in range(trials):
            print(i)
            sum = sum + timeSort(sortFn,n)
        avg = sum / trials
        print("avg = {0:0.1f}".format(avg))
        times.append(avg)
    return times

