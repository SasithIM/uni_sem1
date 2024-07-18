# a) if m < 3 let m = m + 12 and let y = y - 1
# b) let a = 2m + 6 (m + 1) / 10
# c) let b = y + y/4 – y/100 + y/400
# d) let f1 = d + a + b +1
# e) let f = f1 mod 7
# f) stop

# days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()

y,m,d = list(map(int,input().split(' ')))

if m < 3:
    m+=12
    y-=1

a = 2*m + 0.6*(m+1)

b = y+ y/4 - y/100 + y/400

f1 = d + a + b + 1

f = f1 % 7

print(int(f))

### MISSES A DAY (TUESDAY) WHEN GOING FROM 2003 6 30 TO 2003 7 1