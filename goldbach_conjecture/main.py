# -*- coding: UTF-8 -*-

"""
Python 3
"""

print("2보다 큰 짝수 입력", end=" ")
v = input()
# Assert is statement. not a function in python 3
assert int(v) % 2 == 0, "짝수를 입력하세요."

Q = list(range(2,int(v)))

# Sieve of Eratosthenes
for i in Q:
	for j in Q:
		if i < j:
			if j % i == 0:
				Q.pop(Q.index(j))

# Ordered pair of solutions
sol = list()
for i in reversed(range(len(Q))):
	a = Q[i]
	for n in Q:
		if n + a == int(v):
			if n <= a :
				sol.append((n,a))

print(sol)