n= int(input("Ingrese el número de asteriscos de la base de los triangulos: "))
F = []
for i in range(n):
  string = ""
  for j in range(i):
    string += (" ")
  for j in range(n - i):
    string += ("* ")
  for j in range(i):
    string += (" ")
  F.append(string)

for i in range(n):
  print(F[n-i-1] + F[i])