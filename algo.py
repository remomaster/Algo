import random as rand

#testen der lösung
def tester(input,anleitung1,anleitung2):
	for x in input:
		result = (x[0] + x[1]) / x[2]							#  'naive' lösung zum testen
		berechnet = anleitung2(anleitung1(x[0],x[1]),x[2]) 		#  'algo'  output berechnen
		if result != berechnet:
			return False
	return True
		
		
# algo repetoir festlegen
repetoirname = ['add','sub','mul','div']
repetoir1 = [lambda x,y : x+y,lambda x,y : x-y,lambda x,y : x*y,lambda x,y : x/y if y != 0 else -1]

algo = []
inputs = [[rand.randint(1,10),rand.randint(1,10),rand.randint(1,10)] for x in range(10)]				#test input generieren


#algorithmus finden
while algo == []:
	next = [repetoir1[rand.randint(0,len(repetoir1)-1)],repetoir1[rand.randint(0,len(repetoir1)-1)]]	#algorithmus generieren
	if tester(inputs,next[0],next[1]):																	#algorithmus testen
		algo = repetoirname[repetoir1.index(next[0])],repetoirname[repetoir1.index(next[1])]

print(' '.join(algo))