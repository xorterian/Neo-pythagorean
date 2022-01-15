import math

# 8-bit int -> int reversion
def rev(n):
  return int('{:08b}'.format(n)[::-1], 2)


# (real, real) -> real Xoration based on real r arity
def xor(x,y,r):
 Z=[]
 while x >= 1 or y >= 1:
  Z.append((x+y) % r)
  x=x//r
  y=y//r
 Z=Z[::-1]
 z=0
 #ref=0
 for i in range(len(Z)):
  z+=Z[i]*r**(len(Z)-i-1)
 return z

# (real, real) -> real Andation based on real r arity
def and(x,y,r):
 Z=[]
 while x >= 1 or y >= 1:
  Z.append(min(x,y) % r)
  x=x//r
  y=y//r
 Z=Z[::-1]
 z=0
 #ref=0
 for i in range(len(Z)):
  z+=Z[i]*r**(len(Z)-i-1)
 return z

# (real, real) -> real Oration based on real r arity
def or(x,y,r):
 Z=[]
 while x >= 1 or y >= 1:
  Z.append(max(x,y) % r)
  x=x//r
  y=y//r
 Z=Z[::-1]
 z=0
 #ref=0
 for i in range(len(Z)):
  z+=Z[i]*r**(len(Z)-i-1)
 return z

# returns the dict of (divisors, multilicity) or the int n
def divs(n):
 Divs=[]
 Res={}
 d=1
 while n>1:
  d+=1
  while n % d == 0:
   n=n//d
   if not d in Divs:
    Divs.append(d)
    Res[d]=1
   else:
    Res[d]+=1
 return Res

# returns the superated representation of a rational number n
def surep(n,eps=10**-6):
 k=0
 while n % 1 > eps:
  k+=1
  n*=10
  n=round(n,6)
 #print(n)
 rep=divs(round(n))
 if 2 in rep.keys():
  rep[2]-=k
 else:
  rep[2]=-k
 if 5 in rep.keys():
  rep[5]-=k
 else:
  rep[5]=-k
 return rep

# a kind of superated xoration
# E.g. suxor(1.5, 2.5, 2) = 15 because 1.5 = 3/2, 2.5 = 5/2 and 2**((-1) ^ (-1)) * 3^(1 ^ 0) * 5^(0 ^ 1) = 1 * 3 * 5 = 15.
def suxor(x,y,r):
 A, B, C = surep(x), surep(y), {}
 P=set(list(A.keys())+list(B.keys()))
 z=1
 for p in P:
  if p in A:
   a=A[p]
  else:
   a=0
  if p in B:
   b=B[p]
  else:
   b=0
  C[p]=xor(a,b,r)
  z*=p**C[p]
 return z
