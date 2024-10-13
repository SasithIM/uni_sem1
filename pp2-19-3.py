n = 3

for i in range(2**n):
    vals = [i//(2**(n-j))%2 for j in range(1,n+1)]
    out = vals[0] ^ vals[1]
    for k in vals[2:]:
        out = out ^ k
    
    print(vals,out)