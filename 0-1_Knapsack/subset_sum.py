
def subset_sum(arr,target,n):
    t=[[False]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if j==0:
                t[i][j]=True
            elif i==0:
                t[i][j]=False

    for i in range(1,n+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]

    return t[n][target]


arr=[2,3,7,8,10]
target=11
n=len(arr)

# print(subset_sum(arr,target,n))