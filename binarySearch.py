pos=-1
def search(list1,n):
    upper=len(list1)-1
    lower=0
    while lower == upper:
        mid = int((lower + upper) / 2)
        if list1[mid] == n:
            globals()['pos']=mid
            return True
        elif list1[mid] < n:
            lower=mid
        elif list1[mid] > n:
            upper=mid
    return False

if __name__ == "__main__":

    list1 = [1, 10, 11, 12, 38, 45]
    n = 100
    if search(list1, n):
        print("Found at list index ",pos)
    else:
        print("Not found")