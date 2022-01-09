def encrypt(p,k):
    c=''
    b=len(p)
    for i in range(0,b):
        if p[i]==' ':
            ct=' '
        else :
            ca=(ord(p[i])-65+k)%26
            y=ca+65
            ct=chr(y)
        c=c+ct
    return c

# print (encrypt('aku kau kua', 3))

def decrypt(c,k):
    p=''
    b=len(c)
    for i in range(0,b):
        if c[i]==' ':
            pt=' '
        else :
            pa=(ord(c[i])-97-k)%26
            y=pa+97
            pt=chr(y)
        p=p+pt
    return p

# print (decrypt('JTD TJD TDJ', 3))