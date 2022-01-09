def entrans(p,k):
    c=''
    b=len(p)
    while b%k>0:
        p=p+'x'
    b=len(p)
    n=b//k
    for i in range (k) :
        for j in range (n) :
            c=c+p[i+j*k]
    return c

# print(entrans ('pelitabangsa', 3))

def detrans(c,k):
    b=len(c)
    k=b//k
    p=''
    n=b//k
    for i in range (k) :
        for j in range (n) :
            p=p+c[i+j*k]
    return p

# print(detrans ('pibgetaslana', 3))