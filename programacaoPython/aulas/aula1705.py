nome = "Ana"
nota = 10

nomes = ["ana", "marcos"]

print(nomes)
nomes[1] = "afonso"
print(nomes)
print(len(nomes))

nomes.append("jose")
print(nomes)

nomes.insert(1, "juju")
print(nomes)

nomes.sort()
print(nomes)

nomes.remove("afonso")
print(nomes)

del nomes[2]

print(nomes)

for n in nomes:
  print(n)