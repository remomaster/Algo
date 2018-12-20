'''
Autor: Remo Spichtig
Datum: 20.12.2018
Zweck: Magische Quadrate finden... langsamer Algorithmus
'''

from itertools import permutations as ps 

# Seitenlänge des Quadrates
n = 4
nq = n**2
sz = (n**3+n)//2

# Testet ob ein Quadrat horizontal,vertikal und diagonal die gleiche summe aufweist
def test(a):
	for i in range(n):
		if sum(a[i*n:(i+1)*n]) != sz:
			return False
	for i in range(n):
		if sum(a[i:nq:n]) != sz:
			return False
	if sum(a[0:nq:(n+1)]) != sz:
		return False
	if sum(a[(nq-n):(n-2):(1-n)]) != sz:
		return False
	return True
		
	
# Printet die Quadrate schön
def print_m(a):
	for i in range(n):
		print(' '.join(map(str,a[i*n:(i+1)*n])))
	print()
		
z = []
for i in ps(range(1,nq+1 )):
	if(test(i)):
		print_m(i)
		z.append(i)
		
t = open('matri.txt','w')

for i in z:
	for j in range(n):
		t.write(' '.join(map(str,i[j*n:(j+1)*n])))
		t.write('\n')
	t.write('\n')
	
t.close()