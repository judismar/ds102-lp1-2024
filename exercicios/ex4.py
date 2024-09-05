from random import randint

r1 = randint(1, 10)
r2 = randint(1, 10)
r3 = randint(1, 10)

if r1 < 5 and r2 < 5 and r3 < 5:
    print("Você venceu!")
else:
    print("Você perdeu.")
