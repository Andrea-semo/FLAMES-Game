prenom1 = str(input("Entrez le premier prénom : "))
prenom2 = str(input("Entrez le deuxieme prénom :"))
upper_prenom1 = prenom1.upper()   
upper_prenom2 = prenom2.upper()
list1 = list(upper_prenom1)
list2 = list(upper_prenom2)
for letter in list1 [:] :
   if letter in list2 :
     list1.remove (letter)
     list2.remove (letter)
compteur = len(list1) + len(list2)
FLAMES = ["F","L","A","M","E","S"]
while len(FLAMES) >1 :
    tour = 1
    position = 0
    while tour < compteur :
       position : int= position + 1
       if position >= len(FLAMES) :
            position= 0
       compteur: int = compteur + 1
    FLAMES.remove(FLAMES[position])
    if position >= len(FLAMES):
       position = 0  
print(FLAMES [0])
if FLAMES [0] == "F" :
   print ("friends")
elif FLAMES [0] == "L" :
  print ("lovers")
elif FLAMES [0] == "A" :
   print("Affection")
elif FLAMES [0] == "M" : 
  print ("Marriage")
elif FLAMES [0] == "E" :
   print ("Enemies")
else :
   print ("Siblings")

