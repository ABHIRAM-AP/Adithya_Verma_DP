def recursive_lcs(s1,s2,m,n):
 
    if n==0 or m==0:
        return 0
    
    if s1[m-1]==s2[n-1]:
        return recursive_lcs(s1,s2,m-1,n-1) + 1
    else:
        return max(
            recursive_lcs(s1,s2,m-1,n),
            recursive_lcs(s1,s2,m,n-1),
        )





def dp_lcs(s1,s2,m,n):
    dp=[[0] *(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j]=dp[i-1][j-1]  + 1
            else:
                dp[i][j]=max(
                    dp[i-1][j],
                    dp[i][j-1],
                )
    return dp[m][n]


s1="pmjghexybyrgzczy"
s2="hafcdqbgncrcbihkd"
m,n=len(s1),len(s2)
print(dp_lcs(s1,s2,m,n))