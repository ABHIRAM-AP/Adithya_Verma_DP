def lcs(a,b,m,n):
    dp=[[0] * (n+1)for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                dp[i][j]=dp[i-1][j-1] + 1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]


def lps(a):
    s=a[::-1]
    return lcs(a,s,len(a),len(s))
def min_operations(a):
    return len(a) - lps(a,len(a))

a="abhi"
print(min_operations(a))