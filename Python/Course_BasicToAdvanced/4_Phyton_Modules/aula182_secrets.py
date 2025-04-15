# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr


# print(s.ascii_letters, s.digits, s.punctuation)
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))


random = secrets.SystemRandom()

# print(secrets.randbelow(5))
# print(secrets.choice([10, 11, 12]))

# Funções:

# seed
#   -> NÂO FAZ NADA QUANDO SE USA O SECRETS!!!!
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(time.time())
# print(time.time())

# random.seed(10)


# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print(r_range)


# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)


# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)


# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Carlos', 'Maria', 'Joana', 'José']
# random.shuffle(nomes)
print(nomes)


# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=len(nomes))
print(novos_nomes)
print(nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=2)
print(novos_nomes)
print(nomes)


# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
