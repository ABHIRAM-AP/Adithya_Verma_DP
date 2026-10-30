def rod_cutting(lengths,price,N):

    t=[[0]*(N+1) for _ in range(len(lengths)+1)]
    for i in range(1,len(lengths)+1):
        for j in range(1,N+1):
            if lengths[i-1]<=j:
                t[i][j]=max(prices[i-1]+t[i][j-lengths[i-1]],
                t[i-1][j]        
                    )
            else:
                t[i][j]=t[i-1][j]
    return t[len(lengths)][N]


lengths=[1,2,3,4,5,6,7,8]
prices=[1,5,8,9,10,17,17,20]
N=8
print(rod_cutting(lengths,prices,N))