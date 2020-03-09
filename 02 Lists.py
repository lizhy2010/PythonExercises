listA = []
listB = []

finish = False

while not finish:
    listA.append(input("List a number: "))
    
    if input("Add another number? (y/n): ") == 'n':
        finish = True
    
        
for num in listA:
    if int(num) < 5:
        listB.append(num)
        
print("Here are the numbers less than 5:")
print(listB)