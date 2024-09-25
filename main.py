import random
from statistics import mean
# print('uzduotis 1')
# print()
# vardas = 'Monika'
# pavard = 'S'
# metai = 1991
# print(f'As esu {vardas} {pavard}, man yra {2024-metai} metai')


# print('uzduotis 2')
# print()
# sk = random.randint(0,4)
# print(sk)
# sk2 = random.randint(0,4)
# print(sk2)
# if sk > sk2:
#     if sk2 == 0:
#         print('Dalyba is nulio negalima')
#     else:
#         print(sk, '/', sk2, '=', round(sk / sk2, 2))
# if sk2 > sk:
#     if sk == 0:
#         print('Dalyba is nulio negalima')
#     else:
#         print(sk2, '/', sk, '=', round(sk2 / sk, 2))
# if sk == sk2:
#     print('skaiciai yra lygus')

# print('uzduotis 3')
# print()
# sk = random.randint(0,25)
# print(sk)
# sk2 = random.randint(0,25)
# print(sk2)
# sk3 = random.randint(0,25)
# print(sk3)
# if sk > sk2 > sk3 or sk3 > sk2 > sk:
#     print('Vidurinis skaicius yra', sk2)
# if sk2 > sk > sk3 or sk3 > sk > sk2:
#     print('Vidurinis skaicius yra', sk)
# if sk2 > sk3 > sk or sk > sk3 > sk2:
#     print('Vidurinis skaicius yra', sk3)

# print('uzduotis 4')
# print()
# a = random.randint(0,10)
# print(a)
# b = random.randint(0,10)
# print(b)
# c = random.randint(0,10)
# print(c)
# if a + b > c and a + c > b and b + c > a:
#     print('Trikampi sudaryti galima')
# else:
#     print('Trikampio sudaryti negalima')

# print('uzduotis 5')
# print()
# sk = random.randint(0,2)
# print(sk)
# sk2 = random.randint(0,2)
# print(sk2)
# sk3 = random.randint(0,2)
# print(sk3)
# sk4 = random.randint(0,2)
# print(sk4)
# skaiciai = [sk, sk2, sk3, sk4]
# nulis = skaiciai.count(0)
# vienas = skaiciai.count(1)
# du = skaiciai.count(2)
# print('Buvo', nulis, 'nuliu')
# print('Buvo', vienas, 'vienetu')
# print('Buvo', du, 'dvejetu')

# print('uzduotis 6')
# print()
# sk = random.randint(-10,10)
# if sk > 0:
#     print('{', sk, '}')
# if sk == 0:
#     print(f'({sk})')
# if sk < 0:
#     print(f'[{sk}]')
# sk2 = random.randint(-10,10)
# if sk2 > 0:
#     print('{', sk2, '}')
# if sk2 == 0:
#     print(f'({sk2})')
# if sk2 < 0:
#     print(f'[{sk2}]')
# sk3 = random.randint(-10,10)
# if sk3 > 0:
#     print('{', sk3, '}')
# if sk3 == 0:
#     print(f'({sk3})')
# if sk3 < 0:
#     print(f'[{sk3}]')

# print('uzduotis 7')
# print()
# sk = random.randint(5,3000)
# print(sk)
# if sk > 2000:
#     print('Bus pritaikyta 4% nuolaida ir reikes sumoketi', round(sk * 0.96, 2), 'EUR')
# elif sk > 1000:
#     print('Bus pritaikyta 3% nuolaida ir reikes sumoketi', round(sk * 0.97, 2), 'EUR')
# else:
#     print('Nuolaidos pritaikyta nebus ir reikes sumoekti', sk, 'EUR')

# print('uzduotis 8')
# print()
# sk = random.randint(0,100)
# print(sk)
# sk2 = random.randint(0,100)
# print(sk2)
# sk3 = random.randint(0,100)
# print(sk3)
# vidurk = (sk + sk2 + sk3)/3
# print('Aritmetinis vidurkis:', round(vidurk))
# eilute = [sk, sk2, sk3]
# if sk < 10 or sk > 90:
#     eilute.remove(sk)
# if sk2 < 10 or sk2 > 90:
#     eilute.remove(sk2)
# if sk3 < 10 or sk3 > 90:
#     eilute.remove(sk3)
# vidurk2 = mean(eilute)
# print('Vidurkis atmetus skaicius mazesnius uz 10 arba didesnius uz 90:', round(vidurk2))

print('uzduotis 9')
print()
vala = random.randint(0,23)
print(vala)
minu = random.randint(0,59)
print(minu)
seku = random.randint(0,59)
print(seku)
print(f'{vala}:{minu}:{seku}')
randoms = random.randint(0,300)
print(randoms)
if (seku + randoms) <= 59:
    print(f'naujas laikas su pridetom {randoms} sekundem: {vala}:{minu}:{seku + randoms}')
elif (seku + randoms) > 59:
    min2 = (randoms // 60) + minu
    sek2 = (randoms + seku) % 60
    print(f'naujas laikas su pridetom {randoms} sekundem: {vala}:{min2}:{sek2}')

