def printmatrix(dp,m,n):
     for i in range(m+1):
        for j in range(n+1):
            print(dp[i][j],end=' ')
        print()

def longest_common_substring(a,b,m,n):
    dp=[[-1] *(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0]=0
    for j in range(n+1):
        dp[0][j]=0
    ans=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                dp[i][j]=dp[i-1][j-1] +1
                ans=max(ans,dp[i][j])
            else:
                dp[i][j]=0
    return ans


a="aggtab"
b="gxtxayb"
print(longest_common_substring(a,b,len(a),len(b)))