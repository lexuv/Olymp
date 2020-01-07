#  1) Mushrooms

total = int(input())
mushka = 0
knopka = 0
odd = True
while (mushka + knopka) // 1.5 + (mushka + knopka) != total:
    if odd:
        mushka += 1
        odd = False
    else:
        knopka += 1
        odd = True
print(total - mushka - knopka, mushka, knopka)
