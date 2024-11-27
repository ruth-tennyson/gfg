arr=list(map(int,input().split()))
n=len(arr)
m=(n//2) #if want to sort from a position, then m=position eg:6
for i in range(m,n):
    for j in range(m,m+(n-i-1)):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)