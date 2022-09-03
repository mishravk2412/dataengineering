pos = -1
def search(list1,n):
    i=0
    for i in range(0,len(list1)):
        if list1[i] == n:
            globals()['pos']=i
            return True
    return False

if __name__ == "__main__":

    list1 = [1, 10, 11, 12, 38, 45]
    n = 12
    if search(list1, n):
        print("found at", pos)
    else:
        print("Not found")