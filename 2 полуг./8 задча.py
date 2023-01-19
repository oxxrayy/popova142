count=0
from itertools import product
for a, b, c, d, e in product(range(1,8), range(8), range(8), range(8),range(8)): 
    s=str(a)+str(b)+str(c)+str(d)+str(e)
    if s.count('7')==1 and s.index('7')==len(s)-1 and int(s[len(s)-2])%2!=0: count+=1
    if s.count('7')==1 and s.index('7')==0 and int(s[1])%2!=0: count+=1
    if s.count('7')==1 and s.index('7')<len(s)-1 and s.index('7')>0 and int(s[s.index('7')-1])%2!=0 and int(s[s.index('7')+1])%2!=0:
        count+=1
print(count)
