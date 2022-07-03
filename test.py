def gridtravel(m,n,memo):
    k=str(m)+","+str(n)
    if k in memo :
        return memo[k]
    if n==0 or m==0:
        return 0
    if m==1 and n ==1:
        return 1
    else:
        memo[k]=gridtravel(m-1,n,memo)+gridtravel(m,n-1,memo)
        return memo[k]
memo={}
print(gridtravel(18,18,memo))