import sys

def coinChange(self, coins: list[int], amount: int) -> int:
    n=len(coins)
    INF=sys.maxsize -1 
    t=[[-1]*(amount+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]=0
    for j in range(amount+1):
        t[0][j]=INF
    
    for i in range(1,n+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                t[i][j]=min(t[i][j-coins[i-1]]  + 1 , t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return -1 if t[n][amount] == INF else t[n][amount]