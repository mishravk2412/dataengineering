def insertionSort(list1):
    n=len(list1)
    for i in range(1,n):
        for j in range(i+1,n):
            temp=list1[j]
            if list1[i] > list1[j]:
                list1[i] = list1[j]


    return list1

if __name__ == "__main__":
    list1 = [1000, 999, 101, 608, 333, 456, 88, 10, 11, 0, 1, -1, -11]
    print(insertionSort(list1))