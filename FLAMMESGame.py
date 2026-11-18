prenom1 = str(input("Entrez le premier prénom : "))
prenom2 = str(input("Entrez le deuxieme prénom :"))
upper_prenom1 = prenom1.upper()   
upper_prenom2 = prenom2.upper()
list1 = list(upper_prenom1)
list2 = list(upper_prenom2)
for letter in list1 :
   if letter in list2 :
     list1.remove (letter)
     list2.remove (letter)
compteur = len(list1) + len(list2)
FLAMES = ["F","A","M","E","S"]
while len(FLAMES) >1 :
    compteur = 1
    while compteur < len(FLAMES) :
       position = 0
       position : int= position + 1
       if position >= len(FLAMES) :
            position= 0
       compteur: int = compteur + 1
    FLAMES.remove(FLAMES[position])
    if position >= len(FLAMES):
       position = 0  
print("FLAMES [0]")

