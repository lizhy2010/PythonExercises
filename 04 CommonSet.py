import random

listA = []
listB = []
listC = []

print("\nThis program lists common numbers between list A and B.\n")

for num in range(random.randint(0, 25)):
    listA.append(random.randint(0, 50))
    
for num in range(random.randint(0, 25)):
    check = random.randint(0, 50)
    listB.append(check)
    if check in listA and check not in listC:
        listC.append(check)
        
print("Set A: %s" % listA)
print("Set B: %s" % listB)
print("A n B : %s" % listC)
    
    
