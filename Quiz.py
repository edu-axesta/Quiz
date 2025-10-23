print("Vilken huvudstad har Norge?\n1. Oslo\n2. Stockholm\n3. Köpenhamn")
antal_rätt=0
stad=int(input(""))

if stad==1 or stad==1:
    print(f"Ditt svar: {stad} \nRätt!")
    antal_rätt+=1
elif stad==3:
    print(f"Ditt svar: {stad} \nFel!")
elif stad ==2:
    print(f"Ditt svar: {stad} \nFel")
print()


print("Vilket år började andra världskriget?\n1. 1914\n2. 1939\n3. 1945")
år=int(input(""))
if år==1:
    print(f"Ditt val: {år}\nFel!")
elif år ==2:
    print(f"Ditt val {år}\nRätt!")
    antal_rätt+=1
elif år==3:
    print(f"Ditt val {år}\nFel!")
print()
print(f"Du fick {antal_rätt} av 2 rätt.")