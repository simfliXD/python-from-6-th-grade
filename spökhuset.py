# spökhuset
from random import randint
print('spökhuset')
känner_mod = True
poäng = 0
while känner_mod:
   spökdörr = randint(1, 3)
   print('Tre dörrar framför dig...')
   print('Bakom en dörr finns det ett spöke.')
   print('Vilken dörr väljer du?')
   dörr = input('1, 2 eller 3?')
   dörr_num = int(dörr)
   if dörr_num == spökdörr:
    print('ETT SPÖKE!')
    känner_mod = False
   else:
       print('Inget spöke!')
       print('Du går in i nästa rum.')
print('Spring!')
print('Spelet är över! Din poäng:', poäng)
