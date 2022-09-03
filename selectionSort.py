def selectionSort(list1):
    n=len(list1)
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if list1[j] < list1[min]:
                min=j
        if min != i:
            tmp = list1[i]
            list1[i]=list1[min]
            list1[min]=tmp

    return list1

if __name__ == "__main__":
    list1 = [1000, 999, 101, 608, 333, 456, 88, 10, 11, 0, 1, -1, -11]
    print(selectionSort(list1))