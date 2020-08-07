#coding:utf-8

#calcul de la moyenne des devoirs de maison
moyenne_devoirs=input("Saisissez votre moyenne de devoirs :")

moyenne_devoirs=float(moyenne_devoirs)

def calcul_moyenne_devoirs(moyenne_devoirs,per=0.4):

	resultat1=moyenne_devoirs*per

	return resultat1

print(calcul_moyenne_devoirs(moyenne_devoirs,0.4))


#calcul de la moyenne d'examen

note_examen=input("Saisissez votre note d'examen :")

note_examen=float(note_examen)

def calcul_moyenne_exam(note_examen,perc=0.6):

	resultat2=note_examen*perc

	return resultat2

print(calcul_moyenne_exam(note_examen,0.6))

input()

resultat1=moyenne_devoirs*0.4

resultat2=note_examen*0.6

print("MOYENNE TOTALE OBTENUE :")

def calcul_moyenne_totale(resultat1,resultat2):

	return resultat1+resultat2

print(calcul_moyenne_totale(resultat1,resultat2))


print("DECISION :")

#Décision (admis ou non)

if resultat1+resultat2>=10:

	print("Vous êtes admis(es)")

else:

	print("Désolé, vous n'êtes pas admis(es)")
	