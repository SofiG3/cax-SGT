
frutas=["aguacate","melon","tomate"]

print(frutas)

print(len(frutas))
print(frutas[2])

frutas.append("papaya")
print(frutas)

frutas.append("sandia")
print(frutas)

compra=input("ingresa una fruta:")
frutas.append(compra)

print(frutas)
print(dir(frutas))