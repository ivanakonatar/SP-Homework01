n = int(input("Unesi red kvadratne matrice: "))
X = []

zbir_glavne_dijagonale = zbir_sporedne_dijagonale= 0

prvi_element = 1
for i in range(n):

    X.append([])

    for j in range(n):
        X[i].append(prvi_element)

        if i == j:
            zbir_glavne_dijagonale += prvi_element


        if i+j == n-1:
            zbir_sporedne_dijagonale += prvi_element

        prvi_element += 1

for i in range(n):
    print(X[i])

print("Zbir elemenata u glavnoj dijagonali je: " + str(zbir_glavne_dijagonale)) # zbir_sporedne_dijagonale se moze odrediti
                                                                                # i na sl nacin: n**2+(n-1)**2

print('Zbir elemenata u sporednoj dijagonali je: ' + str(zbir_sporedne_dijagonale) )
