def reverse(arr):
    n=len(arr)
    l,r=0,n-1
    while l < r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
arr=list(map(int,input("Enter the numbers")).split())
print(reverse(arr))
