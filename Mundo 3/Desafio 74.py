# Crie um programa que gere 5 números aleatórios e coloque-os numa tupla.
# Depois, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.

import random

r1 = random.randint(1,100)
r2 = random.randint(1,100)
r3 = random.randint(1,100)
r4 = random.randint(1,100)
r5 = random.randint(1,100)
comp_random = (r1, r2, r3, r4, r5)
  
print(f"Os números sorteados foram: {comp_random}")
print(f"O maior valor foi {max(comp_random)}")
print(f"O menor valor foi {min(comp_random)}")
