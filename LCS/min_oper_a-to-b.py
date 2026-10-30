def min_operations(a,b,m,n):
    dp=[[0] *(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1] + 1
            else:
                dp[i][j]=max(
                    dp[i-1][j],
                    dp[i][j-1]
                )
    deletions=m-dp[m][n]
    insertions=n-dp[m][n]
    return [insertions,deletions]
a="horse"
b="ros"
m,n=len(a),len(b)

print(min_operations(a,b,m,n))