
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


if __name__ == "__main__":
    array = [5,3,4,1,2]
    bubble_sort_v2(array)
    print(array)