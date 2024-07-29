from itertools import combinations
import time

def check(a,b):
	if (a+b)%2!=0:
		return True
	_bool = { a: True , b: True}
	while a!=b:
		if a>b:
			a-=b
			b*=2
		else:
			b-=a
			a*=2
		if _bool.get(a,False):
			return True
		else:
			_bool[a] = True
			_bool[b] = True
	return False

def solve(pair,l1):
	
	
 

def solution(l):
	l1 = l
	pair = []
	removed = []
	ptr =1		
	while ptr<len(l1):
		if l1[ptr] == l1[0]:
			continue
		if check(l1[0],l1[ptr]):
			pair.append([l1[0],l1[ptr]])
			removed.append(l1[0])
			removed.append(l1[ptr])
			l1.pop(ptr)
			l1.pop(0)
			ptr = 0
		ptr +=1	
	print(solve(pair,l1))
			

l = [1,7,3,21,13,19]
t = time.time()
solution(l)
print(time.time()-t)