from lcs import dp_lcs
def shortest_common_supersequence(a,b,m,n):


    return m+n - dp_lcs(a,b,m,n)

a="aggtab"
b="gxtxayb"
print(shortest_common_supersequence(a,b,len(a),len(b)))