
def count_subset_sum(arr,n,target):
    t = [[-1] * (target + 1) for _ in range(n + 1)]

    for i in range(n+1):
        for j in range(target+1):
            if j==0:
                t[i][j]=1
            elif i==0:
                t[i][j]=0


    for i in range(1,n+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    
    return t[n][target]

arr=[2,3,5,8,6,10]
n=len(arr)
target=10
print(count_subset_sum(arr,n,target))