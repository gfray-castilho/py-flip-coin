import random

cara_coroa = ["cara", "coroa"]
trials = 10000
qtd_caras = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

for i in range(trials):
    cara = 0
    for i in range(0, 10):
        sorte = random.choice(cara_coroa)
        if sorte == "cara":
            cara += 1

    qtd_caras[cara] += 1

for key in qtd_caras:
    porcentagem = (qtd_caras[key] / 10000) * 100
