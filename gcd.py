# def gcd(x,y):
#     if x == 0:
#         return y
#     else:
#         return gcd(y%x,x)
    
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x
    
# print(gcd(34024234385785786674674746767474938742347932048230842038027234248,13048018343445345345435435342985792239840234204375273234234))