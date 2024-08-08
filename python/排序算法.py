
def bubble_sort_v1(array:list):
    n = len(array)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if array[i-1] > array[i]:
                flag = True
                array[i-1], array[i] = array[i], array[i-1]
    
def bubble_sort_v2(array:list):
    n = len(array)
 
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]


def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)


def quick_sort_v2(a, l, r):
    low = l
    high = r
    mid = a[low]
    while low < high:
        while low < high and a[high] > mid:
            high -= 1
        a[low] = a[high]
        while low < high and a[low] < mid:
            low += 1
        a[high] = a[low]
    a[low] = mid
    quick_sort_v2(a, l, low-1)
    quick_sort_v2(a, low+1, r)

if __name__ == "__main__":
    array = [5,3,4,1,2,9,3,5,6,8]
    # bubble_sort_v2(array)
    quick_sort(array, 0, len(array)-1)
    print(array)