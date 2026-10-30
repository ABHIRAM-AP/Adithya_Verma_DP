def print_lc_string(a,b,m,n):
    ans=[]
    dp=[[0]*(n+1)for _ in range(m+1)]


    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1] + 1
            else:
                dp[i][j]= max(
                    dp[i-1][j],
                    dp[i][j-1]
                )
    i,j=m,n
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            ans.append(a[i-1])
            i-=1
            j-=1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                j-=1
            else:
                i-=1
    ans_str="".join(reversed(ans))
    return ans_str 


a="aggtab"
b="gxtxayb"

print(print_lc_string(a,b,len(a),len(b)))