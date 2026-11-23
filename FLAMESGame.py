prenom1 = str(input("Entrez le premier prénom : "))
prenom2 = str(input("Entrez le deuxieme prénom :"))
upper_prenom1 = prenom1.upper()   
upper_prenom2 = prenom2.upper()
list1 = list(upper_prenom1)
list2 = list(upper_prenom2)
for letter in list1 [:] :
   if letter in list2 :
     removed_letter = list1.remove (letter)
     removed_letter = list2.remove (letter)
compteur = len(list1) + len(list2)
FLAMES = ["F","L","A","M","E","S"]
while len(FLAMES) >1 :
    tour = 0
    position = 0
    while tour < compteur :
       position : int= position + 1
       if position >= len(FLAMES) :
            position= 0
       tour = tour + 1
    FLAMES.remove(FLAMES[position])
    if position >= len(FLAMES):
       position = 0  
if FLAMES [0] == "F" :
   print ("you are friends")
elif FLAMES [0] == "L" :
  print ("you are in love")
elif FLAMES [0] == "A" :
   print("you have affection for each other")
elif FLAMES [0] == "M" : 
  print ("you are married")
elif FLAMES [0] == "E" :
   print ("you are enemies")
else :
   print ("you are siblings")

