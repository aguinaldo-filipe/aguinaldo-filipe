nome = input("Qual é o nome do paciente? ")
idade = input("Qual é o idade do paciente? ")
genero = input("Qual é o genero do paciente? ")

#print(f"\nNome do paciente é {nome}, tem {idade} anos e é do genero {genero}")
# Criação de uma Lista
pacientes = ["Roberto", "leixo", "Julia", "Robertinho", "xande", "bertinho", "Roberta", "Ana", "bertinha", "Alixo", "berta", "Alexander", "Robertinha", "Alex", "berto", "Alexo", "Aleixo", "lexandre", "Alexandre", "Analtina", "lixandre", "Alixo", "Anacleta", "lixo", "Alexandra","Alícia", "Bali", "Baba", "Bianca", "Bruna"]

#print(f"\n pacientes")
print(pacientes[4],pacientes[9]) 
print(f"{pacientes[0]} e a {pacientes[2]}")
print(pacientes)
a=5; b=5; c=a+b; 
print(a),print(c)
print(c),print(b)
print(b),print(a)
i = 2
f = 2.75
c = 2 + 3j
print(i),print(c)
print(f),print(i)
print(c),print(f)
# deletar pacientes na lista
pacientes.remove("Anacleta")

pacientes.append("Aguinaldo")
print(pacientes)

# Dicionário
dict = {"name":"Aguinalda", 
        "surname":"Filipe de Morais", 
        "age":1, 
        "sex": "F"}
print(dict)
# nome = input("Qual é o nome do paciente? ")
print(f)