# print('uzduotis 1')
# print()
# vardas = 'Monika'
# pavard = 'S'
# metai = 1991
# print(f'As esu {vardas} {pavard}, man yra {2024-metai} metai')
import random

print('uzduotis 1')
print()
sk = random.randint(0,4)
print(sk)
sk2 = random.randint(0,4)
print(sk2)
if sk > sk2:
    if sk2 == 0:
        print('Dalyba is nulio negalima')
    else:
        print(sk, '/', sk2, '=', round(sk / sk2))
if sk2 > sk:
    if sk == 0:
        print('Dalyba is nulio negalima')
    else:
        print(sk2, '/', sk, '=', round(sk2 / sk))
if sk == sk2:
    print('skaiciai yra lygus')

