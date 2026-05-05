import turtle
import random
namn = input("Vad heter du?") #spelarens namn
print("hej " + namn) # säger hej till de namnet du valde

def kontrollera_gissning(gissning, svar): # vad som händer om du väljer rätt svar
    global poäng
    gissa_fortfarande = True
    försök = 0
    while gissa_fortfarande and försök < 2:
        if gissning.lower() == svar.lower():
            print("rätt svar" + namn + "!")
            poäng = poäng + 3 - försök
            gissa_fortfarande = False
        else: # du svarar fel och får några till försök
            if försök< 2:
                gissning = input("tyvär, fel svar. Försök igen. ")
            försök = försök + 1

    if försök == 2: # om du svarar fel för många gånger
        print(" rätt svar är " + svar + " " + namn + " du kan göra det!")

poäng = 0 # sätter poäng till 0 vid start av spelet

print("Dags att slå quizet! " + namn + "?") # välkomnar (namn) till quizet
# quiz frågor
gissning1 = input("Är Elon Musk en alien. Sant, falskt eller han är en apa? ")
kontrollera_gissning(gissning1, "Sant")

gissning2 = input("Är du trevlig? \n A] JA! :D \n B] nej :C")
kontrollera_gissning(gissning2, "a")

gissning3 = input("Vilken liten fågel kan stå stilla i luften?")
kontrollera_gissning(gissning3, "Kolibri")

gissning4 = input("Vad heter du")
kontrollera_gissning(gissning4, namn)
print(namn + ". Yea I know your name :-D")

print("Du fick " + str(poäng) + "\n poäng bra jobbat!")
if poäng == 12:
    print("\n du fick max poäng bra jobbat här har du en lossas bokal.")

else:
    print("eftersom " + poäng + " poäng så får du inte en bokal")
