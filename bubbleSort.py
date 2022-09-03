def bubbleSort(list1):
    i=len(list1)
    while i > 0:
        for j in range(0,i-1):
            if list1[j] > list1[j+1]:
                tmp = list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=tmp
        i=i-1
    return list1

if __name__ == "__main__":

    list1 =[1000,999,101,608,333,456,88,10,11,0,1,-1,-11]
    print(bubbleSort(list1))