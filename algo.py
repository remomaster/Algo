import random as rand

#Algorithmus wurde extra ((x,y),z) geklammert, damit keine durch null Rechnung entsteht
def SollFunktion(x):
	return (x[0] / x[1]) - x[2]		

#testen der lösung
def generierterAgorithusTesten(input,anleitung1,anleitung2):
	for x in input:
		berechnetResultat = anleitung2(anleitung1(x[0],x[1]),x[2]) 		#  output von generiertem Algorithmus berechnen
		if SollFunktion(x) != berechnetResultat:						#  prüfen ob berechnetes Resultat korrekt ist.
			return False
	return True
		
		
# algo repetoir festlegen
repetoir1 = {
			 'add' : lambda x,y : x+y, \
			 'sub' : lambda x,y : x-y, \
			 'mul' : lambda x, y : x*y, \
			 'div' : lambda x,y : x/y if y != 0 else -1
			}

algo = []
inputs = [[rand.randint(1,10),rand.randint(1,10),rand.randint(1,10)] for x in range(10)]				#test input generieren


#algorithmus finden
while algo == []:
	next = [list(repetoir1.keys())[rand.randint(0,len(repetoir1)-1)], list(repetoir1.keys())[rand.randint(0,len(repetoir1)-1)]]		#algorithmus generieren
	if generierterAgorithusTesten(inputs,repetoir1[next[0]],repetoir1[next[1]]):													#algorithmus testen
		algo = next

print(' '.join(algo))